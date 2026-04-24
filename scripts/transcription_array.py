import os
import whisperx
from whisperx.diarize import DiarizationPipeline
from tqdm import tqdm
import torch
import sys

video_file = sys.argv[1]

device = os.environ.get("DEVICE", "cpu")
compute_type = "float16" if device == "cuda" else "int8"
language = "en"

# Output directory
results_dir = "results"
os.makedirs(results_dir, exist_ok=True)
base_name = os.path.splitext(os.path.basename(video_file))[0]

# 1. Transcribe
print("Loading model...", flush = True)
model = whisperx.load_model("large-v2", device, compute_type=compute_type, language=language)

print("Transcribing...", flush = True)
audio = whisperx.load_audio(video_file)
result = model.transcribe(audio, batch_size=32, print_progress=True)

# 2. Align
print("Aligning...", flush = True)
model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)

segments = result["segments"]
aligned_segments = []
with tqdm(total=len(segments), desc="Aligning segments") as pbar:
    for segment in segments:
        aligned = whisperx.align([segment], model_a, metadata, audio, device, return_char_alignments=False)
        aligned_segments.extend(aligned["segments"])
        pbar.update(1)

result["segments"] = aligned_segments

# 3. Diarize
print("Diarizing...", flush = True)
diarize_model = DiarizationPipeline(
    model_name="pyannote/speaker-diarization-community-1",
    device=device
)
diarize_segments = diarize_model(audio)
result = whisperx.assign_word_speakers(diarize_segments, result)

# 4. Save segment-level transcript
segment_path = os.path.join(results_dir, f"{base_name}_transcript.txt")
with open(segment_path, "w") as f:
    for segment in result["segments"]:
        speaker = segment.get("speaker", "UNKNOWN")
        start = segment["start"]
        end = segment["end"]
        text = segment["text"].strip()
        line = f"[{start:.2f}s - {end:.2f}s] {speaker}: {text}"
        print(line, flush = True)
        f.write(line + "\n")

print(f"\nSegment transcript saved to {segment_path}")

# 5. Save word-level transcript
word_path = os.path.join(results_dir, f"{base_name}_words.txt")
with open(word_path, "w") as f:
    for segment in result["segments"]:
        speaker = segment.get("speaker", "UNKNOWN")
        for word in segment.get("words", []):
            start = word.get("start", "?")
            end = word.get("end", "?")
            text = word.get("word", "").strip()
            start_fmt = f"{start:.2f}s" if isinstance(start, float) else start
            end_fmt = f"{end:.2f}s" if isinstance(end, float) else end
            line = f"[{start_fmt} - {end_fmt}] {speaker}: {text}"
            print(line, flush = True)
            f.write(line + "\n")

print(f"Word transcript saved to {word_path}", flush = True)
