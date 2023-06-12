import pytest
from matrix2 import Matrix

mtx_a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
mtx_b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
mtx_a_sum_b = Matrix([[2,4,6], [8, 10, 12],[14,16,18],[20,22,24]])
mtx_c = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
mtx_d = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
mtx_mul_ans = Matrix([[1,8,21,40],[10,30,56,88],[27,60,99,144]])


def test_sum():
    assert mtx_a + mtx_b == mtx_a_sum_b, "It's allive!!!!"

def test_mul():
     assert mtx_c * mtx_d == mtx_mul_ans, "It's ok!=)"   
    
if __name__ == '__main__':
    pytest.main(['-v'])