import csv

def read_csv(arq=None):
    datas = []

    if arq:
        try:
            file = open('dados.csv')
        except FileNotFoundError:
            return None

        lines = csv.reader(file)

        for line in lines:
            x, y = line
            datas.append((int(x), int(y)))
        datas = sorted(datas)
    # Pytest
    return datas

if __name__ == '__main__':
    print(read_csv('dados.csv'))
