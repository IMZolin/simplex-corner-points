from itertools import combinations
import numpy as np
from preprocessing import Mini_Gauss
np.seterr(invalid='ignore')


def get_Aux(Matrix):
    """
    На основе входной матрицы Matrix генеририруются подматрицы размером m * m и возвращаются через yield
    вместе с индексами соответствующих столбцов матрицы Matrix
    """
    columns_configuration = combinations(range(Matrix.shape[1]), Matrix.shape[0])
    for item in columns_configuration:
        A_aux = np.zeros(Matrix.shape[0]*Matrix.shape[0]).reshape(Matrix.shape[0],Matrix.shape[0])
        for j in range(len(item)):
            assrt = Matrix[:, item[j]]
            A_aux[:, j] = assrt
        yield A_aux, item


def Corner_Dots_Method(c_vector, b_vector, Matrix, c0):
    """
    Метод крайних точек
    Каждая из подматриц решается методом Жордано-Гаусса
    Если решение существует, проверяется его допустимость
    Если решение допустимо, оно добавляется в массив
    Из сформированного массива выбирается решение - наименьший элемент
    Если массив пуст, то допустимого решения не существует
    """
    generator = get_Aux(Matrix)
    solution_list = list()
    for A_aux, item in generator:
        try:
            tmp_basis = np.arange(A_aux.shape[1])
            A_aux, b_vector_1 = Mini_Gauss(A_aux, A_aux.shape[1], A_aux.shape[0], b_vector.copy(), 0, tmp_basis)
            if len(b_vector_1) == len([val for val in b_vector_1 if val >= 0]):
                result = 0
                for j in range(len(item)):
                    result += c_vector[item[tmp_basis[j]]]*b_vector_1[j]
                result -= c0
                solution_list.append(result)
        except Exception:
           pass
    if len(solution_list) != 0:
        print('\nРЕШЕНИЕ КРАЙНИМИ ТОЧКАМИ: ', min(solution_list))
        return min(solution_list)
    else:
        print("\nКРАЙНИЕ ТОЧКИ. У ЗАДАЧИ НЕ СУЩЕСТВУЕТ ДОПУСТИМОГО РЕШЕНИЯ\n")



