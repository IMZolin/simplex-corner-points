from adapter import Adapter
from preprocessing import Make_Canon_Form, Update_C
from corner_dots import Corner_Dots_Method
from simplex import Simplex_With_Init


def parse_to_dual(A, b_, c_, Less_, More_, var_positive_amount):
    """solve min task only"""

    """change all <= to >="""
    for i in range(Less_):
        A[i, :] = -A[i, :]
        b_[i] = -b_[i]

    c_dual_ = b_
    """max -> min"""
    c_dual_[:] = -c_dual_[:]

    b_dual_ = c_
    A_dual_ = A.T
    A_dual_ = A_dual_.astype(float)

    X_Positive_dual_ = Less_ + More_
    Less_dual = var_positive_amount
    More_dual = 0

    return A_dual_, b_dual_, c_dual_, X_Positive_dual_, Less_dual, More_dual, X_Positive_dual_


if __name__ == "__main__":

    Matrix, b, c, c0, More, Less, x_positive = Adapter()
    """make dual form"""
    A_dual, b_dual, c_dual, X_Positive_dual, Less, More, X_Positive_dual = parse_to_dual(Matrix,
                                                                                         b,
                                                                                         c,
                                                                                         Less,
                                                                                         More,
                                                                                         len(x_positive))
    """make canon form from dual"""
    A_dual, b_dual, Ind_dual = Make_Canon_Form(A_dual.copy(),
                                               b_dual.copy(),
                                               False,
                                               X_Positive_dual,
                                               Less,
                                               More)

    c_dual, c_free_dual = Update_C(A_dual.copy(),
                                   b_dual.copy(),
                                   c_dual.copy(),
                                   c0,
                                   Ind_dual.copy(),
                                   Less,
                                   More,
                                   Matrix.shape[1] - X_Positive_dual)

    """solve with Simplex Method"""
    Simplex_With_Init(A_dual.copy(),
                      b_dual.copy(),
                      Ind_dual.copy(),
                      c_dual.copy(),
                      c_free_dual.copy())

    """solve with Corner Dots Method"""
    Corner_Dots_Method(c_dual, b_dual.copy(), A_dual, c_free_dual)
