# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def find_max(x):
	result=0
	mark=0
	i=0
	for e in x:
		if e>result:
			result=e
			mark=i
		i+=1	
	return mark 
def longest_repetition(x):
	if x==[]:
		return None
	length=len(x)
	record=[]
	for e in x:
		record.append(1)
	for i in range(0,length):
		if x[i]==x[i-1]:
			record[i]+=record[i-1]	
	return x[find_max(record)]


#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1
print longest_repetition([1,2,2,3])
print longest_repetition([])
# None


