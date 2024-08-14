import numpy as np
out=[50, 32, 83, 12, 49, 34, 81, 101, 46, 108, 106, 57, 105, 115, 102, 51, 67, 34, 124, 15, 125, 117, 51, 124, 38, 10, 30, 76, 125, 27, 89, 14, 50, 93, 88, 56]
out_shift=[x<<57 for x in out]
print(out_shift)

    

# Coefficient matrix A
A = np.array([[out_shift[len(out)-2], 1],[out_shift[len(out)-4], 1]])



# Right-hand side vector b
b = np.array([out_shift[len(out)-1], out_shift[len(out)-3]])

# Solve the system of equations
solution = np.linalg.solve(A, b)
x,y=solution
print(f"Solution: x = {x}, y = {y}")




