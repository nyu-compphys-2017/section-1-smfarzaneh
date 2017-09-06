# This is a python file! The '#' character indicates that the following line is a comment.
import numpy as np

# The following is an example for how to define a function in Python
# def tells the compiler that hello_world is the name of a function
# this implementation of hello_world takes a string as an argument,
# which has default value of the empty string. If the user calls 
# hello_world() without an argument, then the compiler uses ''
# as the default value of the argument.
def hello_world(name=''):
    print 'hello world!'
    print name
    return
    
    
#Implement the Riemann Sum approximation for integrals.
def int_riemann(a, b, N, func): 
	width = (b - a + 0.0)/N
	print str(width)
	x_vals = np.arange(a + width, b + width, width) # right biased points
	print str(x_vals)
	func_vals = func(x_vals)
	int_reimann = np.sum(func_vals)*width
	return int_reimann



