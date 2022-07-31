def calc_n(data):
    return len(data)

def summation(datas):
    sum_x = sum_y = sum_xy = sum_x_pow = sum_y_pow = 0
    for data in datas:
        x, y = data
        sum_x += x
        sum_y += y
        sum_xy += x * y
        sum_x_pow += x ** 2
        sum_y_pow += y ** 2
    return (sum_x, sum_y, sum_xy, sum_x_pow, sum_y_pow)

def calc(data):
    n = calc_n(data)
    sum_x, sum_y, sum_xy, sum_x_pow, sum_y_pow = summation(data)

    b = (n * sum_xy - sum_x * sum_y)/(n * sum_x_pow - sum_x ** 2)
    a = (sum_y - b * sum_x) / n

    # correlation_coefficient
    r = (n * sum_xy - sum_x * sum_y) / ((n * sum_x_pow - sum_x ** 2) ** (1/2) * (n * sum_y_pow - sum_y ** 2) ** (1/2))
    r = round(r, 2)
    return b, a, r

if __name__ == '__main__':
    print(summation([(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)]))
    print(summation([(1, 1), (2, 2)]))
    print(summation([(7, 1), (-2, 5)]))
