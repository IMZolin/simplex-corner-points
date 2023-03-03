from adapter import Adapter
from preprocessing import Make_Canon_Form, Update_C
from simplex import Simplex_With_Init
from corner_dots import Corner_Dots_Method


if __name__ == "__main__":
    """read matrix from file"""
    Matrix, b, c, c0, More, Less, x_positive = Adapter()
    """making canon form from input data"""
    A2, b2, Ind2 = Make_Canon_Form(Matrix.copy(), b.copy(), False, len(x_positive), Less, More)
    c2, c_free2 = Update_C(A2.copy(), b2.copy(), c.copy(), c0, Ind2, Less, More, Matrix.shape[1] - len(x_positive))

    """solve the problem using Simplex - Method"""
    Simplex_With_Init(A2.copy(), b2.copy(), Ind2.copy(), c2.copy(), c_free2.copy())
    """solve the problem using corner dots method"""
    Corner_Dots_Method(c2, b2.copy(), A2, c_free2)














