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
            except IndexError as e:
                if len(row) == 4:
                    outer.append((int(row[2]), int(row[3])))
                else:
                    inner.append((int(row[0]), int(row[1])))
            except ValueError as e: # More outer than inner
                outer.append((int(row[2]), int(row[3])))

        f.close()
    return outer, inner

def interesction_point(p1, p2, p3, p4):
    """
    :return: the interesction point with the given points
    """
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]
    x4, y4 = p4[0], p4[1]

    uA = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))
    uB = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))
    return np.array([x1 + (uA * (x2-x1)), y1 + (uA * (y2-y1))])

def distance(p1, p2):
    """
    The distance for 2 points
    :return: the shortest distance between two points using a^2 + b^2 = c^2
    """
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2)