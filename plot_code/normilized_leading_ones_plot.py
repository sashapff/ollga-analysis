import os

import matplotlib.pyplot as plt
import numpy as np

from tools import option_parse, option_tex_parse, algo_tex_dict


def plot(algo_name, n_deg_from, n_deg_to, q_name, data_path, linestyle):
    algo_tex_name = algo_tex_dict[algo_name]
    latex_output = ''
    algo_latex_code = '\ollga' if algo_name == 'ollga' else '\oplea'
    for lam_name, color in zip(['logn_div_2', 'logn', 'sqrtn', 'n_div_2'], ['black', 'red', 'blue', 'green']):
        lam_tex = option_tex_parse(lam_name)
        keys = []
        values = []
        latex_output += '\t\t\\addplot plot [error bars/.cd, y dir=both, y explicit] coordinates\n'
        latex_output += '\t\t{'
        for n_deg in range(n_deg_from, n_deg_to + 1):
            file_name = data_path + f'{algo_name}: n_deg={n_deg}, lam={lam_name}, q={q_name}.txt'
            if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
                data = np.loadtxt(file_name)
                n = 1 << n_deg
                lam = option_parse(n, lam_name)
                data = data[data >= 0] / n ** 2
                if len(data) > 0:
                    n_iters = data.mean()
                    keys.append(n)
                    values.append(n_iters)
                    std = data.std()

                    latex_output += f'({n},{n_iters})+-(0,{std})'

                    plt.errorbar(n, n_iters, yerr=std, capsize=3, color=color)

        plt.plot(keys, values, label=algo_tex_name + ', $\lambda$=' + lam_tex, color=color, linestyle=linestyle)

        latex_output += '};\n'
        latex_output += '\t\t' + ('% ' if q_name != '0' else '') + '\\addlegendentry{' + algo_latex_code + ', $\\lambda=' + lam_tex[1:-1] + '$' + '};\n'

    return latex_output


if __name__ == '__main__':
    algo_name_1 = 'ollga'
    algo_name_2 = 'lea'
    plots_path = '../plots/leadingones/normalized/'
    latex_plots_path = '../latex_plots/leadingones/normalized/'
    data_path = '../data/leadingones/'

    algo_tex_1 = option_tex_parse(algo_name_1)
    algo_tex_2 = option_tex_parse(algo_name_2)
    n_deg_from, n_deg_to = 3, 9


    if not os.path.exists(plots_path):
        os.makedirs(plots_path)

    if not os.path.exists(latex_plots_path):
        os.makedirs(latex_plots_path)

    for q_name in ['0', 'logn_div_n', '1_div_6e', '1']:
        plt.clf()
        q_tex = option_tex_parse(q_name)
        name = f'q={q_name}'
        plt.title(f'LeadingOnes function, q={q_tex}')

        latex_output_1 = plot(algo_name_1, n_deg_from, n_deg_to, q_name, data_path, '-')
        latex_output_2 = plot(algo_name_2, n_deg_from, n_deg_to, q_name, data_path, '--')

        with open(latex_plots_path + name + '.tex', 'w') as file:
            file.write(latex_output_1)
            file.write(latex_output_2)

        plt.legend()
        plt.xlabel('n, size of individuals')
        plt.ylabel('number of noisy fitness evaluations')
        plt.xlim((2 ** n_deg_from - (2 ** n_deg_from) / 4, 2 ** n_deg_to + (2 ** n_deg_to) / 4))
        plt.xscale('log', base=2)
        plt.yscale('log')
        plt.savefig(plots_path + name + '.png')