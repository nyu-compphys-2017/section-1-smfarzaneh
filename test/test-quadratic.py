import sys
sys.path.append('../')

import riemann as rn 

def func(x):
	return x**2

result = rn.int_riemann(0, 3, 100, func)
print str(result)


