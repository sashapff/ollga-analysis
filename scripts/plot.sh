#!/bin/bash -i

python3 plot.py --lam logn --q 1_div_6e
python3 plot.py --lam logn --q logn_div_n
python3 plot.py --lam logn --q 0
python3 plot.py --lam logn --q 1

python3 plot.py --lam logn_div_2 --q 1_div_6e
python3 plot.py --lam logn_div_2 --q logn_div_n
python3 plot.py --lam logn_div_2 --q 0
python3 plot.py --lam logn_div_2 --q 1
#
python3 plot.py --lam sqrtn --q 1_div_6e
python3 plot.py --lam sqrtn --q logn_div_n
python3 plot.py --lam sqrtn --q 0
python3 plot.py --lam sqrtn --q 1
#
