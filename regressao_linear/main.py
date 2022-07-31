from read_file import read_csv
from linear_regression import calc
from plot_graphic import show_graphic

file = "dados.csv"
print('Bem-vindo(a) ao Regressão Linear')

if __name__ == '__main__':
    data = read_csv(file)
    slope, origin, correlation_coefficient = calc(data)

    if correlation_coefficient:
        print(f'Coeficiente de correlação: {correlation_coefficient:.2f}')
        show_graphic(data, slope, origin)
    else:
        print('Não há relação entre os dados. Coeficiente de correlação igual a 0')

