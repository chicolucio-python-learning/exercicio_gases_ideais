import numpy as np


def replace_comma_to_dot(string):
    return string.replace(',', '.').encode()


dados = np.genfromtxt((replace_comma_to_dot(text) for text in open('exercicio_aula_1.csv')),
                      delimiter=';', dtype=(float, float), names=True)


print(dados)
# print(dados['P_bar'])