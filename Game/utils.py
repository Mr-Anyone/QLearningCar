import numpy as np


def rotation(degree, vet):
    """
    Calculate the point when given degree and initial position
    :param degree: rotated degree
    :param vet: initial position
    :return: the rotated position
    """
    radian = degree * np.pi / 180
    rotation_matrix = np.array([[np.cos(radian), -np.sin(radian)],  # Degree to radian
                                [np.sin(radian), np.cos(radian)]])

    return np.matmul(rotation_matrix, vet.T)