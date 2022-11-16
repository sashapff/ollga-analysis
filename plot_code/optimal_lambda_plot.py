import os

import numpy as np

from tools import option_tex_parse


def plot(algo_name, algo_tex, algo_den_name, q_name, q_tex, q_den_name, data_path, n, n_deg):
    latex_output = ''
    latex_output += '\t\t\\addplot plot [error bars/.cd, y dir=both, y explicit] coordinates\n'
    latex_output += '\t\t{'

    file_name = f'opt_lambda_{algo_den_name}-n_{n}-q_{q_den_name}.out'
    with open(data_path + file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            tokens = line.split()
            lam = int(tokens[0].split('=')[1])
            if lam > 1 and not (algo_name == 'olga' and lam < 4 and q_name == '1_div_6e'):
                data = np.array([int(x) for x in tokens[1:]])
                data *= (2 * int(lam) + 1) if algo_name == 'ollga' else (int(lam) + 1)
                n_iters = data[data >= 0].mean()
                std = data[data >= 0].std()

                latex_output += f'({lam},{n_iters})+-(0,{std})'

    latex_output += '};\n'
    latex_output += '\t\t' + ('% ' if q_name != '0' else '') + '\\addlegendentry{' + algo_tex + '};\n'


    return latex_output

if __name__ == '__main__':
    for n_deg in [7, 10]:
        n = 2 ** n_deg

        latex_plots_path = f'../latex_plots/optimal_lambda/n={n}/'
        data_path = '../data/optimal_lambda/'

        if not os.path.exists(latex_plots_path):
            os.makedirs(latex_plots_path)

        for q_name in ['0', 'logn_div_n', '1_div_6e']:
            file_name = f'q={q_name}'
            q_tex = option_tex_parse(q_name)
            if q_name == '0':
                q_den_name = 0
            elif q_name == '1_div_6e':
                q_den_name = '16e'
            else:
                q_den_name = 'lognn'

            latex_output_1 = plot('ollga', '\ollga', 'ollga', q_name, q_tex, q_den_name, data_path, n, n_deg)
            latex_output_2 = plot('lea', '\oplea', 'olea', q_name, q_tex, q_den_name, data_path, n, n_deg)

            with open(latex_plots_path + file_name + '.tex', 'w') as file:
                file.write(latex_output_1)
                file.write(latex_output_2)
