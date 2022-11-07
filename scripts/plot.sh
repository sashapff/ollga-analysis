#!/bin/bash -i

python3 plot.py --algo_1 ollga --algo_2 lea --algo_3 lea --lam1 sqrtn_div_2 --lam2 1 --lam3 logn --q 0 --fitness jump
python3 plot.py --algo_1 ollga --algo_2 lea --algo_3 lea --lam1 sqrtn_div_2 --lam2 1 --lam3 logn --q logn_div_n --fitness jump
python3 plot.py --algo_1 ollga --algo_2 lea --algo_3 lea --lam1 sqrtn_div_2 --lam2 1 --lam3 logn --q 1_div_6e --fitness jump
#
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

