def traverse(x,w,h):
	y=[]
	i=0
	while i<w:
		j=0
		tmp=[]
		while j<h:
			tmp.append(x[j][i])
			j=j+1
		y.append(tmp)
		i=i+1
	return y	
def check_sudoku(x):
	i=0
	j=0
	for e in x:
		i=i+1
	for q in x[0]:
		j=j+1
	if i!=j:
		return False
	k=1
	while k<=i:
		for e in x:
			if k not in e:
				return False
		k=k+1
	k=1
	y=traverse(x,i,j)
	while k<=i:
		for e in y:
			if k not in e:
				return False
		k=k+1
	return True
a=[[1,2,3],[2,3,1],[3,1,2]]
print check_sudoku(a)
