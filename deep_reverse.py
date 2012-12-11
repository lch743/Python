# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list, 
# and returns a new list that is the deep reverse of the input list.  
# This means it reverses all the elements in the list, and if any 
# of those elements are lists themselves, reverses all the elements 
# in the inner list, all the way down. 

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if 
# p is a list and False if it is not.
import copy

def is_list(p):
    return isinstance(p, list)

def reverse(x):
	i=0
	j=len(x)-1
	while i<=j:
		x[i],x[j]=x[j],x[i]
		i+=1
		j-=1
record=[]	

def func(x):
	reverse(x)
	for e in x:
		if is_list(e):
			func(e)
def deep_reverse(x):
	y=copy.deepcopy(x)
	func(y)
	return y  


#For example,

p = [1, [2, 3, [4, [5, 6]]]]
print deep_reverse(p)
#>>> [[[[6, 5], 4], 3, 2], 1]
print p
#>>> [1, [2, 3, [4, [5, 6]]]]

q =  [1, [2,3], 4, [5,6]]
print deep_reverse(q)
#>>> [ [6,5], 4, [3, 2], 1]
print q
#>>> [1, [2,3], 4, [5,6]]

