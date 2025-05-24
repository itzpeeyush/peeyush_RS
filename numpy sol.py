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



5.
import numpy as np

array = np.array([[1, 2], 
                  [3, 4], 
                  [1, 2],
                  [3,5]])

unique_rows = np.unique(array, axis=0)

print(unique_rows)



6.
import numpy as np

image = np.random.randint(0, 256, (5, 5, 3), dtype=np.uint8)

image_swapped = image[:, :, [2, 1, 0]]

print("Original Image:\n", image)
print("\nSwapped Image:\n", image_swapped)



7.
import numpy as np

matrix = np.array([[1,2,3], 
                   [4,5,6], 
                   [7,8,9]])

determinant = (matrix[0, 0] * (matrix[1, 1] * matrix[2, 2] - matrix[1, 2] * matrix[2, 1])
             - matrix[0, 1] * (matrix[1, 0] * matrix[2, 2] - matrix[1, 2] * matrix[2, 0])
             + matrix[0, 2] * (matrix[1, 0] * matrix[2, 1] - matrix[1, 1] * matrix[2, 0]))

print("Determinant:", determinant)




8.
import numpy as np

arr = np.array([])

arr = np.append(arr, [1, 2, 3, 4, 5])

print(arr)



9.
import numpy as np
import time

arr = np.array([])


start_time = time.time()
for i in range(10000):
    arr = np.append(arr, i)
append_time = time.time() - start_time


arr = np.array([])
data_to_append = np.arange(10000)

start_time = time.time()
arr = np.concatenate([arr, data_to_append])
concat_time = time.time() - start_time

print(f"np.append() time: {append_time:.6f} seconds")
print(f"np.concatenate() time: {concat_time:.6f} seconds")





10.
import numpy as np

arr = np.array([1, 2, 3])
new_values = np.array([4, 5, 6])

even_values = new_values[new_values % 2 == 0]

arr = np.append(arr, even_values)

print(arr) 