import numpy as np
from Constants import TRACK_DIR
import csv


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

def read_csv():
    outer, inner = [], []
    with open(TRACK_DIR, 'r') as f:
        file = csv.reader(f)
        for row in file:
            try:
                inner.append((int(row[0]), int(row[1])))
                outer.append((int(row[2]), int(row[3])))
            except IndexError:
                if len(row) == 4:
                    outer.append((int(row[2]), int(row[3])))
                else:
                    inner.append((int(row[0]), int(row[1])))


        f.close()
    return outer, inner
