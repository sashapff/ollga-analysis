import argparse
import math

from algorithms import ollga, lea, tlea, onemax, jump, leading_ones

algo_dict = {
    'ollga': ollga,
    'lea': lea,
    'tlea': tlea
}

fitness_dict = {
    'onemax': onemax,
    'jump': jump,
    'leading_ones': leading_ones
}

fitness_name_dict = {
    'onemax': 'OneMax',
    'jump': 'Jump',
    'leading_ones': 'LeadingOnes'
}

algo_tex_dict = {
    'ollga': '$(1+(\lambda, \lambda))$ GA',
    'lea': '$(1+\lambda)$ EA',
    'tlea': '$(1+2\lambda)$ EA',
}


def option_parse(n, option, lam=None, k=None):
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
    if option == '1_div_n':
        return 1 / n
    if option == 'lambda_div_n':
        return lam / n
    if option == '1_div_lambda':
        return 1 / lam
    if option == 'sqrtn_div_2':
        return math.sqrt(n) / 2
    if option == 'sqrt_k_div_n':
        return math.sqrt(k / n)
    if option == 'sqrtn_pow_k_minus_1_div_sqrt_k_pow_k':
        assert k
        if k == 2:
            assert abs(math.sqrt(n) / 2 - math.sqrt(n) ** (k - 1) / math.sqrt(k) ** k) < 1e-8
        return math.sqrt(n) ** (k - 1) / math.sqrt(k) ** k
    if not option:
        return None
    try:
        return int(option)
    except:
        print('no!')


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
    if option == '1_div_n':
        return '$\\frac{1}{n}$'
    if option == 'lambda_div_n':
        return '$\\frac{\lambda}{n}$'
    if option == '1_div_lambda':
        return '$\\frac{1}{\lambda}$'
    if option == 'sqrt_2_div_n':
        return '$\sqrt{\\frac{2}{n}}$'
    if option == 'sqrtn_div_2':
        return '$\\frac{\sqrt{n}}{2}$'
    if option == 'sqrtn_pow_k_minus_1_div_sqrt_k_pow_k':
        return '$\\frac{\sqrt{n}^{k-1}}{\sqrt{k}^k}$'
    return option


def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--algo', type=str)
    parser.add_argument('--n_deg', type=int)
    parser.add_argument('--lam', type=str)
    parser.add_argument('--q', type=str)
    parser.add_argument('--fitness', type=str, default='onemax')
    parser.add_argument('--k', type=int, default=None)
    parser.add_argument('--p', type=str, default=None)
    parser.add_argument('--c', type=str, default=None)
    parser.add_argument('--threads', type=int, default=10)
    parser.add_argument('--runs', type=int, default=10)
    parser.add_argument('--data_path', type=str, default='data')
    parser.add_argument('--plots_path', type=str, default='plots')
    args = parser.parse_args()

    algo_name = args.algo
    n_threads = args.threads
    n_runs = args.runs
    lam_name = args.lam
    q_name = args.q
    fitness = args.fitness
    k = args.k
    fitness_name = fitness_name_dict[fitness]
    data_path = args.data_path + '/' + fitness_name.lower() + '/' + ('k=' + str(k) + '/' if k else '')
    plots_path = args.plots_path + '/'

    n = 1 << args.n_deg
    lam = int(option_parse(n, args.lam, k=k))
    q = option_parse(n, args.q, lam=lam)
    p = option_parse(n, args.p, lam=lam, k=k)
    c = option_parse(n, args.c, lam=lam, k=k)

    algo = algo_dict[algo_name]
    f = fitness_dict[fitness]

    return algo_name, algo, args.n_deg, n, lam_name, lam, q_name, q, f, fitness_name, k, p, c, n_threads, n_runs, \
           data_path, plots_path


def plots_args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--algo_1', type=str, default='ollga')
    parser.add_argument('--algo_2', type=str, default='lea')
    parser.add_argument('--algo_3', type=str, default='tlea')
    parser.add_argument('--n_deg_from', type=int, default=3)
    parser.add_argument('--n_deg_to', type=int, default=7)
    parser.add_argument('--lam', type=str, default=None)
    parser.add_argument('--lam1', type=str, default=None)
    parser.add_argument('--lam2', type=str, default=None)
    parser.add_argument('--lam3', type=str, default=None)
    parser.add_argument('--q', type=str)
    parser.add_argument('--k', type=int, default=None)
    parser.add_argument('--fitness', type=str, default='onemax')
    parser.add_argument('--data_path', type=str, default='data')
    parser.add_argument('--plots_path', type=str, default='plots')
    args = parser.parse_args()

    algo_name_1 = args.algo_1
    algo_name_2 = args.algo_2
    algo_name_3 = args.algo_3
    n_deg_from = args.n_deg_from
    n_deg_to = args.n_deg_to
    if args.lam:
        lam_name_1 = lam_name_2 = lam_name_3 = args.lam
        lam_tex_1 = lam_tex_2 = lam_tex_3 = option_tex_parse(args.lam)
    elif args.lam1 and args.lam2 and args.lam3:
        lam_name_1 = args.lam1
        lam_name_2 = args.lam2
        lam_name_3 = args.lam3
        lam_tex_1 = option_tex_parse(args.lam1)
        lam_tex_2 = option_tex_parse(args.lam2)
        lam_tex_3 = option_tex_parse(args.lam3)
    else:
        raise RuntimeError('Specify lambdas!')
    q_name = args.q
    k = args.k
    fitness_name = fitness_name_dict[args.fitness]
    data_path = args.data_path + '/' + fitness_name.lower() + '/' + ('k=' + str(k) + '/' if k else '')
    plots_path = args.plots_path + '/' + fitness_name.lower() + '/' + ('k=' + str(k) + '/' if k else '')

    q_tex = option_tex_parse(args.q)

    algo_tex_1 = algo_tex_dict[algo_name_1]
    algo_tex_2 = algo_tex_dict[algo_name_2]
    algo_tex_3 = algo_tex_dict[algo_name_3]

    return algo_name_1, algo_tex_1, algo_name_2, algo_tex_2, algo_name_3, algo_tex_3, n_deg_from, n_deg_to, \
           lam_name_1, lam_tex_1, lam_name_2, lam_tex_2, lam_name_3, lam_tex_3, q_name, q_tex, fitness_name, data_path, \
           plots_path, k
