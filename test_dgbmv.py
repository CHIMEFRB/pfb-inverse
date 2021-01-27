import numpy as np
from pfb import band_mv,band_mv_py3
A = np.random.randn(91,1300000)
kl = 90
ku = 0
n = 1300000
m = 1300000
x = np.random.randn(1300000,80)
trans = False
import timeit

start = timeit.timeit()
new = band_mv_py3(A, kl, ku, n, m, x, trans=False)
end = timeit.timeit()
print('new:',end - start)

start = timeit.timeit()
old = band_mv(A, kl, ku, n, m, x, trans=False)
end = timeit.timeit()
print('old:',end - start)

assert np.isclose(old,new).all()
print('Yay, everything is close!')
