import argparse
from algorithms import ollga, oplea
import math


def option_parse(n, option):
    if option == 'logn':
        return math.log(n)
    if option == '1_div_6e':
        return 1 / 6 / math.e
    if option == 'logn_div_n':
        return math.log(n) / n


def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--algo', type=str)
    parser.add_argument('--n_deg', type=int)
    parser.add_argument('--lam', type=str)
    parser.add_argument('--q', type=str)
    parser.add_argument('--threads', type=int)
    parser.add_argument('--runs', type=int)
    args = parser.parse_args()

    algo = args.algo
    n = 1 << args.n_deg
    lam = int(option_parse(n, args.lam))
    q = option_parse(n, args.q)
    n_threads = args.threads
    n_runs = args.runs

    algo_dict = {
        'ollga': ollga,
        'oplea': oplea
    }

    return algo, algo_dict[algo], args.n_deg, n, args.lam, lam, args.q, q, n_threads, n_runs