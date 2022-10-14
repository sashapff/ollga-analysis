import argparse
import math

from algorithms import ollga, lea, tlea

data_path = 'data/'
plots_path = 'plots/'

algo_dict = {
    'ollga': ollga,
    'lea': lea,
    'tlea': tlea
}

algo_tex_dict = {
    'ollga': '$(1+(\lambda, \lambda))$ GA',
    'lea': '$(1+\lambda)$ EA',
    'tlea': '$(1+2\lambda)$ EA',
}


def option_parse(n, option):
    if option == 'logn':
        return math.log(n)
    if option == '1_div_6e':
        return 1 / 6 / math.e
    if option == 'logn_div_n':
        return math.log(n) / n
    if option == 'sqrtn':
        return math.sqrt(n)
    if option == 'logn_div_2':
        return math.log(n) / 2
    if option == '0':
        return 0
    if option == '1':
        return 1


def option_tex_parse(option):
    if option == 'logn':
        return '$\log(n)$'
    if option == '1_div_6e':
        return '$\\frac{1}{6e}$'
    if option == 'logn_div_n':
        return '$\\frac{\log(n)}{n}$'
    if option == 'sqrtn':
        return '$\sqrt{n}$'
    if option == 'logn_div_2':
        return '$\\frac{\log(n)}{2}$'
    if option == '0':
        return '0'
    if option == '1':
        return '1'


def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--algo', type=str)
    parser.add_argument('--n_deg', type=int)
    parser.add_argument('--lam', type=str)
    parser.add_argument('--q', type=str)
    parser.add_argument('--threads', type=int)
    parser.add_argument('--runs', type=int)
    args = parser.parse_args()

    algo_name = args.algo
    n_threads = args.threads
    n_runs = args.runs
    lam_name = args.lam
    q_name = args.q

    n = 1 << args.n_deg
    lam = int(option_parse(n, args.lam))
    q = option_parse(n, args.q)

    algo = algo_dict[algo_name]

    return algo_name, algo, args.n_deg, n, lam_name, lam, q_name, q, n_threads, n_runs


def plots_args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--algo_1', type=str, default='ollga')
    parser.add_argument('--algo_2', type=str, default='lea')
    parser.add_argument('--algo_3', type=str, default='tlea')
    parser.add_argument('--n_deg_from', type=int, default=5)
    parser.add_argument('--n_deg_to', type=int, default=15)
    parser.add_argument('--lam', type=str)
    parser.add_argument('--q', type=str)
    parser.add_argument('--y_scale', type=str, default='log')
    args = parser.parse_args()

    algo_name_1 = args.algo_1
    algo_name_2 = args.algo_2
    algo_name_3 = args.algo_3
    n_deg_from = args.n_deg_from
    n_deg_to = args.n_deg_to
    lam_name = args.lam
    q_name = args.q
    y_scale = args.y_scale

    lam_tex = option_tex_parse(args.lam)
    q_tex = option_tex_parse(args.q)

    algo_tex_1 = algo_tex_dict[algo_name_1]
    algo_tex_2 = algo_tex_dict[algo_name_2]
    algo_tex_3 = algo_tex_dict[algo_name_3]

    return algo_name_1, algo_tex_1, algo_name_2, algo_tex_2, algo_name_3, algo_tex_3, n_deg_from, n_deg_to, lam_name, \
           lam_tex, q_name, q_tex, y_scale
