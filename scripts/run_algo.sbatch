#! /bin/bash
#SBATCH --job-name="."
#SBATCH --cpus-per-task=10
#SBATCH --time=72:00:00
#SBATCH --mem=20G
#SBATCH --output="slurm_output/"%A.out
#SBATCH --qos=high_cpu

python3 main.py --n_deg 5 --lam n_div_2 --algo lea --q 0 --fitness leading_ones
python3 main.py --n_deg 5 --lam n_div_2 --algo lea --q logn_div_n --fitness leading_ones
python3 main.py --n_deg 5 --lam n_div_2 --algo lea --q 1_div_6e --fitness leading_ones
python3 main.py --n_deg 5 --lam n_div_2 --algo ollga --q 0 --fitness leading_ones
python3 main.py --n_deg 5 --lam n_div_2 --algo ollga --q logn_div_n --fitness leading_ones
python3 main.py --n_deg 5 --lam n_div_2 --algo ollga --q 1_div_6e --fitness leading_ones

#python3 main.py --n_deg 7 --k 3 --q 0 --algo ollga --lam sqrtn_pow_k_minus_1_div_sqrt_k_pow_k --fitness jump --p sqrt_k_div_n --c sqrt_k_div_n
#python3 main.py --n_deg 7 --k 3 --q 0 --algo lea --lam 1 --fitness jump
#python3 main.py --n_deg 7 --k 3 --q 0 --algo lea --lam logn --fitness jump
#python3 main.py --n_deg 7 --k 3 --q logn_div_n --algo ollga --lam sqrtn_pow_k_minus_1_div_sqrt_k_pow_k --fitness jump --p sqrt_k_div_n --c sqrt_k_div_n
#python3 main.py --n_deg 7 --k 3 --q logn_div_n --algo lea --lam 1  --fitness jump
#python3 main.py --n_deg 7 --k 3 --q logn_div_n --algo lea --lam logn --fitness jump
#python3 main.py --n_deg 7 --k 3 --q 1_div_6e --algo ollga --lam sqrtn_pow_k_minus_1_div_sqrt_k_pow_k --fitness jump --p sqrt_k_div_n --c sqrt_k_div_n
#python3 main.py --n_deg 7 --k 3 --q 1_div_6e --algo lea --lam 1  --fitness jump
#python3 main.py --n_deg 7 --k 3 --q 1_div_6e --algo lea --lam logn --fitness jump


#python3 main.py --n_deg 3 --k 2 --q 0 --algo ollga --lam sqrtn_div_2 --fitness jump --p sqrt_2_div_n --c sqrt_2_div_n
#python3 main.py --n_deg 3 --k 2 --q 0 --algo lea --lam 1 --fitness jump
#python3 main.py --n_deg 3 --k 2 --q 0 --algo lea --lam logn --fitness jump
#python3 main.py --n_deg 3 --k 2 --q logn_div_n --algo ollga --lam sqrtn_div_2 --fitness jump --p sqrt_2_div_n --c sqrt_2_div_n
#python3 main.py --n_deg 3 --k 2 --q logn_div_n --algo lea --lam 1  --fitness jump
#python3 main.py --n_deg 3 --k 2 --q logn_div_n --algo lea --lam logn --fitness jump
#python3 main.py --n_deg 3 --k 2 --q 1_div_6e --algo ollga --lam sqrtn_div_2 --fitness jump --p sqrt_2_div_n --c sqrt_2_div_n
#python3 main.py --n_deg 3 --k 2 --q 1_div_6e --algo lea --lam 1  --fitness jump
#python3 main.py --n_deg 3 --k 2 --q 1_div_6e --algo lea --lam logn --fitness jump


#python3 main.py --algo tlea --n_deg 11 --lam logn_div_2 --q 0 
#python3 main.py --algo tlea --n_deg 11 --lam logn_div_2 --q logn_div_n
#python3 main.py --algo tlea --n_deg 11 --lam logn_div_2 --q 1_div_6e
#python3 main.py --algo tlea --n_deg 11 --lam logn --q 0
#python3 main.py --algo tlea --n_deg 11 --lam logn --q logn_div_n
#python3 main.py --algo tlea --n_deg 11 --lam logn --q 1_div_6e
#python3 main.py --algo tlea --n_deg 11 --lam sqrtn --q 0
#python3 main.py --algo tlea --n_deg 11 --lam sqrtn --q logn_div_n
#python3 main.py --algo tlea --n_deg 11 --lam sqrtn --q 1_div_6e
#python3 main.py --algo tlea --n_deg 11 --lam logn_div_2 --q 1
#python3 main.py --algo tlea --n_deg 11 --lam logn --q 1
#python3 main.py --algo tlea --n_deg 11 --lam sqrtn --q 1












