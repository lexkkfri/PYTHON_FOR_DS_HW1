import numpy as np

np.random.seed(42)
# array with rand integers
array = np.random.randint(1, 101, size=(3, 3))
print(f'\nArray: {array}')

# summa
sum = np.sum(array)
print(f'\nSumma: {sum}')

# max/min value and positions
max = np.max(array)
max_i = np.unravel_index(np.argmax(array), array.shape)
print(f'\nMax value: {max} (row: {max_i[0]}, column: {max_i[1]})')

min = np.min(array)
min_i = np.unravel_index(np.argmin(array), array.shape)
print(f'\nMin value: {min} (row: {min_i[0]}, column: {min_i[1]})')

# each row sorted
sorted = np.sort(array, axis=1)
print(f'\nSorted Array: \n{sorted}')
