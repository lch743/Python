list1=[1,2,3,4]
list2=[1,2,3,4]


def proc3(x):
	x+=[5]

list1+=[5]
proc3(list2)
print list1,list2
