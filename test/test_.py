from pytest import mark
from regressao_linear import read_csv, calc_n, summation, calc

@mark.parametrize(
    'file_name, expected',
    [("dados.csv", [(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)])]
)
def test_read_csv_retorn_expected(file_name, expected):
    assert read_csv(file_name) == expected


@mark.parametrize(
    'data, expected',
    [
        ([(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)], 6),
        ([(1, 1), (2, 2)], 2)
    ]
)
def test_n_retorn_expected(data, expected):
    assert calc_n(data) == expected

@mark.parametrize(
    'data, expected',
    [
        ([(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)], (21, 21, 56, 91, 91)),
        ([(1, 1), (2, 2)], (3, 3, 5, 5, 5)),
        ([(7, 1), (-2, 5)], (5, 6, -3, 53, 26))
    ]
)
def test_summation_retorn_expected(data, expected):
    assert summation(data) == expected

@mark.parametrize(
    'data, expected',
    [
        ([(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)], (-1.0, 7.0, -1.0)),
    ]
)
def test_calc_retorn_expected(data, expected):
    assert calc(data) == expected

