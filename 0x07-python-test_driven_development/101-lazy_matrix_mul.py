#!/usr/bin/python3
"""Using numpy to multiply 2 matrices"""


import numpy as np

def matrix_mul_numpy(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (numpy.ndarray): The first matrix.
        m_b (numpy.ndarray): The second matrix.

    Raises:
        ValueError: If matrices m_a and m_b can't be multiplied.

    Returns:
        numpy.ndarray: The resulting matrix after multiplication.
    """
    result = np.dot(m_a, m_b)
    return result

# Example usage:
matrix_a = np.array([[1, 2, 3], [4, 5, 6]])
matrix_b = np.array([[7, 8], [9, 10], [11, 12]])

result_matrix = matrix_mul_numpy(matrix_a, matrix_b)
print(result_matrix)

