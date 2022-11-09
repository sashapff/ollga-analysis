#!/bin/bash -i

python3 plot.py --algo_1 ollga --algo_2 lea --algo_3 lea --lam logn --q 0 --fitness leading_ones
python3 plot.py --algo_1 ollga --algo_2 lea --algo_3 lea --lam logn --q logn_div_n --fitness leading_ones
python3 plot.py --algo_1 ollga --algo_2 lea --algo_3 lea --lam logn --q 1_div_6e --fitness leading_ones

python3 plot.py --algo_1 ollga --algo_2 lea --algo_3 lea --lam logn_div_2 --q 0 --fitness leading_ones
python3 plot.py --algo_1 ollga --algo_2 lea --algo_3 lea --lam logn_div_2 --q logn_div_n --fitness leading_ones
python3 plot.py --algo_1 ollga --algo_2 lea --algo_3 lea --lam logn_div_2 --q 1_div_6e --fitness leading_ones

python3 plot.py --algo_1 ollga --algo_2 lea --algo_3 lea --lam sqrtn --q 0 --fitness leading_ones
python3 plot.py --algo_1 ollga --algo_2 lea --algo_3 lea --lam sqrtn --q logn_div_n --fitness leading_ones
python3 plot.py --algo_1 ollga --algo_2 lea --algo_3 lea --lam sqrtn --q 1_div_6e --fitness leading_ones


#python3 plot.py --k 3 --algo_1 ollga --algo_2 lea --algo_3 lea --lam1 sqrtn_pow_k_minus_1_div_sqrt_k_pow_k --lam2 1 --lam3 logn --q 0 --fitness jump
#python3 plot.py --k 3 --algo_1 ollga --algo_2 lea --algo_3 lea --lam1 sqrtn_pow_k_minus_1_div_sqrt_k_pow_k --lam2 1 --lam3 logn --q logn_div_n --fitness jump
#python3 plot.py --k 3 --algo_1 ollga --algo_2 lea --algo_3 lea --lam1 sqrtn_pow_k_minus_1_div_sqrt_k_pow_k --lam2 1 --lam3 logn --q 1_div_6e --fitness jump
#python3 plot.py --k 2 --algo_1 ollga --algo_2 lea --algo_3 lea --lam1 sqrtn_div_2 --lam2 1 --lam3 logn --q 0 --fitness jump
#python3 plot.py --k 2 --algo_1 ollga --algo_2 lea --algo_3 lea --lam1 sqrtn_div_2 --lam2 1 --lam3 logn --q logn_div_n --fitness jump
#python3 plot.py --k 2 --algo_1 ollga --algo_2 lea --algo_3 lea --lam1 sqrtn_div_2 --lam2 1 --lam3 logn --q 1_div_6e --fitness jump


#python3 plot.py --lam logn --q 1_div_6e
#python3 plot.py --lam logn --q logn_div_n
#python3 plot.py --lam logn --q 0
#python3 plot.py --lam logn --q 1
#
#python3 plot.py --lam logn_div_2 --q 1_div_6e
#python3 plot.py --lam logn_div_2 --q logn_div_n
#python3 plot.py --lam logn_div_2 --q 0
#python3 plot.py --lam logn_div_2 --q 1
#
#python3 plot.py --lam sqrtn --q 1_div_6e
#python3 plot.py --lam sqrtn --q logn_div_n
#python3 plot.py --lam sqrtn --q 0
#python3 plot.py --lam sqrtn --q 1

