import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

x = list(range(1, 101))

n_factorial = list(map(math.factorial, x))
f1 = interp1d(x, n_factorial)
nth_power2 = list(map(lambda i: 2**i, x))
f2 = interp1d(x, nth_power2, kind='cubic')
n_squared = list(map(lambda i: i**2, x))
f3 = interp1d(x, n_squared, kind='cubic')
n_log2_2 = list(map(lambda i: i*math.log2(i), x))
f4 = interp1d(x, n_log2_2, kind='cubic')
n = x
f5 = interp1d(x, n, kind='cubic')
n_sqrt = list(map(math.sqrt, x))
f6 = interp1d(x, n_sqrt, kind='cubic')
log2_n = list(map(math.log2, x))
f7 = interp1d(x, log2_n, kind='cubic')
O1 = [1 for i in x]
f8 = interp1d(x, log2_n, kind='cubic')

x = np.arange(1, 100, 0.1)
plt.plot(x, f1(x), label='O(n!)', linestyle='--')
plt.plot(x, f2(x), label='O(2^n)', linestyle='--')
plt.plot(x, f3(x), label='O(n^2)', linestyle='--')
plt.plot(x, f4(x), label='O(n*log2(n))', linestyle='--')
plt.plot(x, f5(x), label='O(n)', linestyle='--')
plt.plot(x, f6(x), label='O(n^0.5)', linestyle='--')
plt.plot(x, f7(x), label='O(log2(n))', linestyle='--')
plt.plot(x, [1 for _ in x], label='O(1)', linestyle='--')
plt.title('Time complexity visualization')
plt.xlabel('n')
plt.ylabel('time complexity O()')
plt.grid()
plt.ylim(0, 100)
plt.xlim(0, 100)
plt.legend()
plt.show()


