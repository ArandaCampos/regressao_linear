from read_file import read_csv
from linear_regression import calc
from plot_graphic import show_graphic

file = "dados.csv"

if __name__ == '__main__':
    data = read_csv(file)
    slope, origin, correlation_coefficient = calc(data)
    print(slope, origin, correlation_coefficient)
    if correlation_coefficient:
        show_graphic(data, slope, origin)
    else:
        print('coeficiente de correlação igual a 0 ')

