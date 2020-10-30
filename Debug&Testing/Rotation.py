"""
These files are only used for testing purpose only
"""
import matplotlib.pyplot as plt
import numpy as np


def rotation(degree, vet):
    radian= degree * np.pi/180
    rotation_matrix = np.array([[
        np.cos(radian) , -np.sin(radian)# Degree to radian
    ], [
        np.sin(radian) , np.cos(radian)
    ]])

    return np.matmul(rotation_matrix, vet.T)

vector = np.array([10,5])
all_vector = np.array([vector])
rotations = np.linspace(0, 180, 1000)

for angle in rotations:
    all_vector = np.append(all_vector , rotation(angle, vector))

all_vector = all_vector.reshape(len(rotations) +1, 2)
plt.scatter(all_vector[:, 0], all_vector[:, 1])
plt.show()
