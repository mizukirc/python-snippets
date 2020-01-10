import numpy as np

in_arr = input().strip().split(' ')
in_arr = np.array(in_arr, int)
out_arr = np.reshape(in_arr, (3,3))
print(out_arr)


# -- another answer
in_arr = np.array(input().split(), int)
out_arr = np.reshape(in_arr, (3,3))
print(out_arr)