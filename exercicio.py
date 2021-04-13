import numpy as np
import matplotlib.pyplot as plt
import pint
from scipy.constants import gas_constant
from scipy.stats import linregress

ureg = pint.UnitRegistry()
ureg.setup_matplotlib()

gas_constant = gas_constant * ureg('J/(mol*K)')

temperature = 300 * ureg.kelvin


def replace_comma_to_dot(string):
    return string.replace(',', '.').encode()


def plot_params(axis):
    ax = axis
    ax.grid(b=True, axis='both', which='major', linestyle='--', linewidth=1.5)
    ax.minorticks_on()
    ax.grid(b=True, which='minor', axis='both', linestyle=':', linewidth=1.0)
    ax.tick_params(axis='both', labelsize=16, length=6, which='major', width=1.5)
    ax.tick_params(axis='both', length=3, which='minor', width=1.0)
    ax.set_axisbelow(True)


dados = np.genfromtxt((replace_comma_to_dot(text) for text in open('exercicio_aula_1.csv')),
                      delimiter=';', dtype=(float, float), names=['P_bar', 'd_gL'], skip_header=1)

valores_pressao = dados['P_bar'] * ureg.bar
valores_densidade = dados['d_gL'] * ureg('g/l')
pressao_sobre_densidade = valores_pressao / valores_densidade

regressao = linregress(valores_densidade, pressao_sobre_densidade)

massa_molar = gas_constant * temperature / (regressao.intercept * ureg('bar / (g/l)'))

fig, ax = plt.subplots(figsize=(8, 6), nrows=1, ncols=1, tight_layout=True)

plot_params(ax)
ax.scatter(valores_densidade, pressao_sobre_densidade)
ax.set_xlabel(r'$\rho$ / $g \cdot \ell^{-1}$', fontsize=18)
ax.set_ylabel(r'$\frac{P}{\rho}$ / $bar \cdot \ell \cdot g^{-1}$', fontsize=18)

plt.show()
print(massa_molar.to('g/mol'))
