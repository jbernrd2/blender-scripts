import functions.vertex_functions as vf
import numpy as np


A = np.array([[0, 5, 1],
              [4, 4, 9],
              [7, 0, -1]])

rotated_A = vf.orthoRotateObject(A, 'x')

print(rotated_A)