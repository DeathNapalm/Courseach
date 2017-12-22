import numpy as np
A = np.array([[5,7,1],[10,14,2],[2,0,1]])
b = np.array([13,26,13])
print(np.linalg.solve(A,b))