import os

import matplotlib.pyplot as plt
import numpy as np

from tools import plots_args_parse, option_parse
from main import stop_criterion


def plot(algo_name, n_deg_from, n_deg_to, lam_name, q_name, label, data_path, lam_tex, is_same, k, color):
    if not is_same:
        label += ', $\lambda$=' + lam_tex
    keys = []
    values = []

    for n_deg in range(n_deg_from, n_deg_to + 1):
        file_name = data_path + f'{algo_name}: n_deg={n_deg}, lam={lam_name}, q={q_name}.txt'
        if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
            data = np.loadtxt(file_name)
            n = 1 << n_deg
            lam = option_parse(n, lam_name, k=k)
            if algo_name == 'lea':
                assert len(data[data >= stop_criterion(n) * (lam + 1)]) == 0
            else:
                assert len(data[data >= stop_criterion(n) * (2 * lam + 1)]) == 0
            n_iters = data[data >= 0].mean()
            # print(f'k={k}, algo={algo_name}, lam={lam_name}, n={n}, {len(data[data < 0])}%' )
            keys.append(n)
            values.append(n_iters)

            plt.errorbar(n, n_iters, yerr=data.std(), color=color, capsize=3)

    plt.plot(keys, values, label=label, color=color)


if __name__ == '__main__':
    algo_name_1, algo_tex_1, algo_name_2, algo_tex_2, algo_name_3, algo_tex_3, n_deg_from, n_deg_to, lam_name_1, \
    lam_tex_1, lam_name_2, lam_tex_2, lam_name_3, lam_tex_3, q_name, q_tex, fitness_name, data_path, plots_path, k \
        = plots_args_parse()

    if not os.path.exists(plots_path):
        os.makedirs(plots_path)

    is_same = lam_name_1 == lam_name_2 == lam_name_3

    if is_same:
        plt.title(f'{fitness_name} function, $\lambda$={lam_name_1}, q={q_tex}')
    else:
        plt.title(f'{fitness_name} function, k={k}, q={q_tex}')

    plot(algo_name_1, n_deg_from, n_deg_to, lam_name_1, q_name, algo_tex_1, data_path, lam_tex_1, is_same, k, 'black')
    plot(algo_name_2, n_deg_from, n_deg_to, lam_name_2, q_name, algo_tex_2, data_path, lam_tex_2, is_same, k, 'tab:red')
    plot(algo_name_3, n_deg_from, n_deg_to, lam_name_3, q_name, algo_tex_3, data_path, lam_tex_3, is_same, k, 'darkblue')

    plt.legend()
    plt.xlabel('n, size of individuals')
    plt.ylabel('number of noisy fitness evaluations')
    plt.yscale('log')
    plt.xlim((2 ** n_deg_from - (2 ** n_deg_from) / 4, 2 ** n_deg_to + (2 ** n_deg_to) / 4))
    plt.xscale('log', base=2)

    if is_same:
        plt.savefig(
            plots_path + f'{algo_name_1}_{algo_name_2}_{algo_name_3}: lam={lam_name_1}, q={q_name}.png')
    else:
        plt.savefig(
            plots_path + f'{algo_name_1}_{algo_name_2}_{algo_name_3}: lam1={lam_name_1}, lam2={lam_name_2}, lam3={lam_name_3}, q={q_name}.png')
