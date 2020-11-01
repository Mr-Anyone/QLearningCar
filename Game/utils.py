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
            if row[0] and row[-1]:
                inner.append((row[0], row[1]))
                outer.append((row[2], row[3]))

            elif row[0] and not row[-1]:
                inner.append((row[0], row[1]))

            else:
                outer.append((row[2], row[3]))

        f.close()
    return outer, inner
outer, innter = read_csv()
print("hi")
