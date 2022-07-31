import matplotlib.pyplot as plt

def line_draw(data, slope, origin):
    # datas of line
    line = [slope * x + origin for x in range(data[-1][0])]
    # label
    if origin < 0:
        label = f'f(x) = {slope:.2f}x {origin:.2f}'
    else:
        label = f'f(x) = {slope:.2f}x + {origin:.2f}'
    #plot
    plt.plot(line, color='red', label=label)
    plt.legend([label])

def points_draw(data):
    line_values = []
    for line in data:
        x, y = line
        plt.plot(x, y, 'g.')

def show_graphic(data, slope, origin):
   # Settings graphics
    plt.title('Regressão Linear')
    plt.xlabel('Eixo x')
    plt.ylabel('Eixo y')

    line_draw(data, slope, origin)
    points_draw(data)
    plt.show()

# Debug
if __name__ == '__main__':
    show_graphic([(1,6), (2, 5), (4, 4), (4, 3), (5, 2), (6,1)], -1, 7)
