#!/bin/bash -i

python3 optimal_lambdas_plot.py --algo ollga --q 1_div_6e
python3 optimal_lambdas_plot.py --algo lea --q 1_div_6e
python3 optimal_lambdas_plot.py --algo tlea --q 1_div_6e

python3 optimal_lambdas_plot.py --algo ollga --q logn_div_n
python3 optimal_lambdas_plot.py --algo lea --q logn_div_n
python3 optimal_lambdas_plot.py --algo tlea --q logn_div_n

python3 optimal_lambdas_plot.py --algo ollga --q 0
python3 optimal_lambdas_plot.py --algo lea --q 0
python3 optimal_lambdas_plot.py --algo tlea --q 0
