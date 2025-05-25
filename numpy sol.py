1.
import numpy as np

even_numbers = np.arange(2, 101, 2)

reversed_array = even_numbers[::-1]

print(reversed_array)



2.
import numpy as np

checkerboard = np.zeros((8, 8), dtype=int)

checkerboard[1::2, ::2] = 1
checkerboard[::2, 1::2] = 1

print(checkerboard)



3.
import numpy as np

identity_matrix = np.eye(6, dtype=int)

identity_matrix[np.diag_indices(6)] = np.arange(1, 7)

print(identity_matrix)



4.
import numpy as np

random_array = np.random.randint(1, 100, (5, 5))

border_elements = np.concatenate([
    random_array[0],        
    random_array[-1],      
    random_array[1:-1, 0],  
    random_array[1:-1, -1] 
])

print("Original Array:\n", random_array)
print("\nBorder Elements:\n", border_elements) 
