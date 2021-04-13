import numpy as np
import matplotlib.pyplot as plt


def replace_comma_to_dot(string):
    return string.replace(',', '.').encode()


dados = np.genfromtxt((replace_comma_to_dot(text) for text in open('exercicio_aula_1.csv')),
                      delimiter=';', dtype=(float, float), names=['P_bar', 'd_gL'], skip_header=1)

pressao_sobre_densidade = dados['P_bar'] / dados['d_gL']

fig, ax = plt.subplots(figsize=(8, 6), nrows=1, ncols=1)

ax.scatter(dados['d_gL'], pressao_sobre_densidade)

print(dados.dtype.names)

plt.show()
