# From Desktop to Cluster
## Scaling Computational Social Science with High-Performance Computing

**COMPTEXT 2026 Workshop | April 23, 2026 | University of Birmingham**

**Instructor:** Andreas Kuepfer (TU Darmstadt)

---

## About This Workshop

This 3-hour workshop introduces researchers in Computational Social Science (CSS) to High-Performance Computing (HPC). It is designed for participants with basic familiarity with R or Python, and no prior HPC experience is required.

The workshop covers everything from motivation to practice: why desktop computing hits a wall with modern CSS data and methods, how HPC clusters are structured, and how to actually connect, submit jobs, and scale typical computational social scientist workflows.

---

## Workshop Structure

| Block | Topic |
|-------|-------|
| **Block 1** | Why HPC? Motivation & big picture |
| **Block 2** | HPC architecture: nodes, cores, memory |
| **Block 3** | Connecting & navigating an HPC cluster |
| *Break* | |
| **Block 4** | Job schedulers: writing & submitting jobs (SLURM) |
| **Block 5** | Monitoring, debugging & best practices |
| **Block 6** | Workflow managers & outlook |

---

## Repository Contents

| File | Description |
|------|-------------|
| [`COMPTEXT26_WORKSHOP_KUEPFER_HPC.pdf`](COMPTEXT26_WORKSHOP_KUEPFER_HPC.pdf) | Slide deck (PDF) |

### [`scripts/`](scripts/)

Example scripts for audio transcription with speaker diarization using [WhisperX](https://github.com/m-bain/whisperX), ready for SLURM job submission on [Lichtenberg HPC](https://www.hrz.tu-darmstadt.de/hlr/hochleistungsrechnen/index.en.jsp) in Darmstadt, Germany.

| File | Description |
|------|-------------|
| [`transcription.py`](scripts/transcription.py) | Transcribe a single hardcoded video file (transcription + alignment + diarization) |
| [`transcription_array.py`](scripts/transcription_array.py) | Same pipeline, but accepts the video path as a command-line argument (for array jobs) |
| [`run_transcription.sh`](scripts/run_transcription.sh) | SLURM job script to run `transcription.py` on a GPU node |
| [`run_transcription_array.sh`](scripts/run_transcription_array.sh) | SLURM array job script to process multiple videos in parallel |
| [`transcription.sh`](scripts/transcription.sh) | Minimal local wrapper to run `transcription.py` without SLURM |

---

## Contact

**Andreas Kuepfer** (TU Darmstadt)

- 📧 [andreas.kuepfer@tu-darmstadt.de](mailto:andreas.kuepfer@tu-darmstadt.de)
- 🌐 [andreaskuepfer.github.io](https://andreaskuepfer.github.io)
- 🦋 [ankuepfer.bsky.social](https://bsky.app/profile/ankuepfer.bsky.social)
