import os

import matplotlib.pyplot as plt
import numpy as np

from tools import optimal_lambda_plots_args_parse


def plot(algo_name, lam_from, lam_to, q_name, data_path, n_deg, color):
    keys = []
    values = []

    for lam in range(lam_from, lam_to + 1):
        file_name = data_path + f'{algo_name}: n_deg={n_deg}, lam={lam}, q={q_name}.txt'
        if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
            data = np.loadtxt(file_name)
            n_iters = data.mean()
            keys.append(lam)
            values.append(n_iters)

            plt.errorbar(lam, n_iters, yerr=data.std(), color=color, capsize=3)

    plt.plot(keys, values, color=color)
    plt.xticks(range(lam_from, lam_to + 1))


if __name__ == '__main__':
    algo_name, algo_tex, lam_from, lam_to, q_name, q_tex, n_deg, data_path, plots_path = optimal_lambda_plots_args_parse()

    if not os.path.exists(plots_path):
        os.mkdir(plots_path)

    plt.title(f'{algo_tex}, q={q_tex}')

    plot(algo_name, lam_from, lam_to, q_name, data_path, n_deg, 'black')

    # plt.legend()
    plt.xlabel('lambda')
    plt.ylabel('number of noisy fitness evaluations')
    plt.yscale('log')
    plt.xlim((lam_from - 1, lam_to + 1))

    plt.savefig(plots_path + f'{algo_name}: n_deg={n_deg}, q={q_name}.png')
