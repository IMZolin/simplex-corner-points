import pandas as pd
import numpy as np


def Adapter():
    """
    Важное правило:
    Первые неравенства: <=
    Вторые неравенства: >=
    Первые переменные >= 0 (0, 1...)
    """
    table = pd.read_excel('data.xlsx')
    Matrix = np.array(table.iloc[:-6, :6])
    b = np.array(table.b.iloc[:-6])
    c = np.array(table.iloc[-5, :-2])
    c0 = table.iloc[-5, -1]
    try:
        Less = table.sign.value_counts().loc['<=']
    except:
        Less = 0

    try:
        More = table.sign.value_counts().loc['>=']
    except:
        More = 0

    x_positive = [int(x) for x in table.iloc[-1, 0].split(',')]
    print('Matrix:\n', pd.DataFrame(Matrix))
    print('b:\n', b)
    print('c:\n', c)
    print('c0:\n', c0)
    print('Less:\n', Less)
    print('More:\n', More)
    print('x_positive:\n', x_positive)
    return Matrix, b, c, c0, More, Less, x_positive


if __name__ == "__main__":
    Adapter()
