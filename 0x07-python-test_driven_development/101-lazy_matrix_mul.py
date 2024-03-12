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
    result = np.matmul(m_a, m_b)
    return result
