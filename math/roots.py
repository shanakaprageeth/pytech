import numpy as np
from scipy import optimize

# polynomial with coefficients p[0] * x**n + p[1] * x**(n-1) + ... + p[n-1]*x + p[n]
# p = [an,an-1...,a0]
coeff = [ 2, 1]
print(np.roots(coeff))
