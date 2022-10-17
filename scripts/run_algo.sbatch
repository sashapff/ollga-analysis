#! /bin/bash
#SBATCH --job-name="tlea9"
#SBATCH --cpus-per-task=10
#SBATCH --time=72:00:00
#SBATCH --mem=20G
#SBATCH --output="slurm_output/"%A.out

python3 main.py --algo tlea --n_deg 9 --lam logn --q logn_div_n