import numpy as np
from matplotlib.ticker import MaxNLocator
from preprocessing import Make_Canon_Form, Update_C
import time
from simplex import Simplex_With_Init
from corner_dots import Corner_Dots_Method
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use('TkAgg')  # !IMPORTANT


def generate_matrix(rank):
    array = np.random.randint(rank, size=(rank, rank))
    array = array.astype(float)
    return array


def write_in_array(massiv):
    Array_of_matrix = []
    array_of_c = []
    array_of_c0 = []
    array_of_basis = []
    for i in massiv:
        try:
            tmp_matrix = generate_matrix(i)
            A, b, Basis_Ind = Make_Canon_Form(tmp_matrix, [float(x) for x in np.arange(i)], False, i, i // 4, i // 4)
            c, c0 = Update_C(A, b, [float(x) for x in np.arange(i)], 0, Basis_Ind, i // 4, i // 4, 0)
            Array_of_matrix.append(A)
            array_of_c.append(c)
            array_of_c0.append(c0)
            array_of_basis.append(Basis_Ind)
        except:
            pass
    return Array_of_matrix, array_of_c, array_of_c0, array_of_basis


def Simplex_Record_Time(Array_of_matrix, array_of_c, array_of_c0, array_of_basis):
    t_array = []
    solution_simplex_array = []
    for i in range(len(array_of_c0)):
        t0 = time.time()
        try:
            Array_of_matrix[i], b_fr_ch, array_of_c[i], sol = Simplex_With_Init(Array_of_matrix[i],
                                                                                [float(x) for x in np.arange(Array_of_matrix[i].shape[0])],
                                                                                array_of_basis[i],
                                                                                array_of_c[i],
                                                                                array_of_c0[i])
            t1 = time.time()
            t_array.append(t1 - t0)
            solution_simplex_array.append(-sol)
        except:
            t_array.append(None)
            solution_simplex_array.append(None)

    return t_array, solution_simplex_array


def Corner_Dots_Record_Time(Array_of_matrix, array_of_c, array_of_c0):
    t_array = []
    solution_array_kr_tchk = []
    for i in range(len(array_of_c0)):
        t0 = time.time()
        solution = Corner_Dots_Method(array_of_c[i],
                                [float(x) for x in np.arange(Array_of_matrix[i].shape[0])],
                                Array_of_matrix[i],
                                array_of_c0[i])
        t1 = time.time()
        t_array.append(t1 - t0)
        solution_array_kr_tchk.append(solution)
    return t_array, solution_array_kr_tchk


def create_time_dependence_graph_data(min_matrix_rang, max_matrix_rang):
    massive = []
    for i in range(min_matrix_rang, max_matrix_rang):
        massive.append(i)
    A_s, c_s, c0_s, base_s = write_in_array(massive)
    A_kt = []
    c_kt = []
    c0_kt = []
    for i in range(len(A_s)):
        A_kt.append(A_s[i].copy())
        c_kt.append(c_s[i].copy())
        c0_kt.append(c0_s[i].copy())

    time_simplex_array, sol_val_simp = Simplex_Record_Time(A_s, c_s, c0_s, base_s)
    time_corner_dots_array, sol_val_kr_t4k = Corner_Dots_Record_Time(A_kt, c_kt, c0_kt)
    plot_time_dependence_graph_data(massive, time_simplex_array, time_corner_dots_array)


def create_get_count_of_iter(min_matrix_rang, max_matrix_rang):
    massive = []
    for i in range(min_matrix_rang, max_matrix_rang):
        massive.append(i)
    A_s, c_s, c0_s, base_s = write_in_array(massive)
    A_kt = []
    c_kt = []
    c0_kt = []
    for i in range(len(A_s)):
        A_kt.append(A_s[i].copy())
        c_kt.append(c_s[i].copy())
        c0_kt.append(c0_s[i].copy())
        
    Simplex_Record_Time(A_s, c_s, c0_s, base_s)


def plot_time_dependence_graph_data(massive, time_simplex_array, time_corner_dots_array):
    plt.rc('lines', linewidth=2.5)
    fig, ax = plt.subplots()

    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    line1, = ax.plot(massive, time_simplex_array, '-o', label='simplex')
    line2 = ax.plot(massive, time_corner_dots_array, '-o', label='corner_dots')
    plt.title('График зависимости времени выполнения метода от размерности матрицы')
    ax.legend(handlelength=4)
    plt.xlabel('Размерность матрицы')
    plt.ylabel('Время, с')
    plt.show()


def main():
    create_time_dependence_graph_data(3, 7)


main()

