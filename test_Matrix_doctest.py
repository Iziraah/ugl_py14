from matrix2 import Matrix



def test_Martix():
    """
    >>> print(repr(Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) + Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])))
    Matrix([[2, 4, 6], [8, 10, 12], [14, 16, 18], [20, 22, 24]])
    >>> print(repr(Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) * Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))
    Matrix([[1, 8, 21], [8, 25, 48], [21, 48, 81]])
    """
    

if __name__ == '__main__':
    import doctest 
    doctest.testmod(verbose=True)