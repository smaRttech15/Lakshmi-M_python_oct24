import numpy as np
import numpy as np
def f(x, y):
	return 10 * x + y
my_array = np.fromfunction(f, (5, 4), dtype = int)
my_array[[0, 1, -1], :] = 0
print(f'After:\n {my_array}')