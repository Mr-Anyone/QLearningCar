"""
These files are only used for testing purpose only
"""
import matplotlib.pyplot as plt
import numpy as np
from Constants import *


def rotation(degree, vet):
    radian= degree * np.pi/180
    rotation_matrix = np.array([[
        np.cos(radian) , -np.sin(radian)# Degree to radian
    ], [
        np.sin(radian) , np.cos(radian)
    ]])

    return np.matmul(rotation_matrix, vet.T)

vector = np.array([10,5])
B = vector + np.array([BOX_WIDTH/2, -BOX_HEIGHT/2]) # B Point the vector space in terms of orgin reference
C = vector + np.array([-BOX_WIDTH/2, -BOX_HEIGHT/2])

all_vector = np.array([vector])
b_rotation_matrix = np.array([B])
c_rotation_matrix = np.array([C])

rotations = np.linspace(0, 90, 2)

for angle in rotations:
    # all_vector = np.append(all_vector , rotation(angle, vector))
    b_rotation_matrix = np.append(b_rotation_matrix, rotation(angle, B)) # Rotation definition in terms of B
    c_rotation_matrix = np.append(c_rotation_matrix, rotation(angle, C))

# all_vector = all_vector.reshape(len(rotations) +1, 2)
b_rotation_matrix = b_rotation_matrix.reshape(len(rotations) + 1, 2)
c_rotation_matrix = c_rotation_matrix.reshape(len(rotations) + 1, 2)

# plt.scatter(all_vector[:, 0], all_vector[:, 1], c='b')
plt.scatter(b_rotation_matrix[:, 0], b_rotation_matrix[:, 1], c='g')
plt.scatter(c_rotation_matrix[:, 0], c_rotation_matrix[:, 1], c='r')
plt.show()
