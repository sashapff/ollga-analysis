#! /bin/bash
#SBATCH --job-name="tlea"
#SBATCH --cpus-per-task=10
#SBATCH --time=72:00:00
#SBATCH --mem=20G
#SBATCH --output="slurm_output/"%A.out
#SBATCH --qos=high_cpu

python3 main.py --algo tlea --n_deg 11 --lam logn_div_2 --q 0 --data_path data
python3 main.py --algo tlea --n_deg 11 --lam logn_div_2 --q logn_div_n --data_path data
python3 main.py --algo tlea --n_deg 11 --lam logn_div_2 --q 1_div_6e --data_path data
python3 main.py --algo tlea --n_deg 11 --lam logn --q 0 --data_path data
python3 main.py --algo tlea --n_deg 11 --lam logn --q logn_div_n --data_path data
python3 main.py --algo tlea --n_deg 11 --lam logn --q 1_div_6e --data_path data
python3 main.py --algo tlea --n_deg 11 --lam sqrtn --q 0 --data_path data
python3 main.py --algo tlea --n_deg 11 --lam sqrtn --q logn_div_n --data_path data
python3 main.py --algo tlea --n_deg 11 --lam sqrtn --q 1_div_6e --data_path data
python3 main.py --algo tlea --n_deg 11 --lam logn_div_2 --q 1 --data_path data
python3 main.py --algo tlea --n_deg 11 --lam logn --q 1 --data_path data
python3 main.py --algo tlea --n_deg 11 --lam sqrtn --q 1 --data_path data
