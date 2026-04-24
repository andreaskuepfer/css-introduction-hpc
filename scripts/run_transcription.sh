#!/bin/bash
#SBATCH --job-name=whisperx_transcription
#SBATCH --account=kurs00100
#SBATCH --partition=kurs00100
#SBATCH --reservation=kurs00100
#SBATCH --time=0-00:05:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=8G
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.err
#SBATCH --gres=gpu:1

export HF_HOME="/home/kurse/kurs00100/models/"
export TORCH_HOME="/home/kurse/kurs00100/models/torch"
export NLTK_DATA="/home/kurse/kurs00100/models/nltk_data"
export HF_HUB_DISABLE_XET=1
export DEVICE="cuda"

source /home/kurse/kurs00100/miniforge3/etc/profile.d/conda.sh
conda activate /home/kurse/kurs00100/env_whisperx

python transcription.py
