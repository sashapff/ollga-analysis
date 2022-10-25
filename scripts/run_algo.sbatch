#! /bin/bash
#SBATCH --job-name="run"
#SBATCH --cpus-per-task=10
#SBATCH --time=72:00:00
#SBATCH --mem=20G
#SBATCH --output="slurm_output/"%A.out
#SBATCH --qos=high_cpu

python3 main.py --algo ollga --n_deg 7 --lam 10 --q 0 --data_path lambda_data
