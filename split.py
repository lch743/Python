def split_string(s):
	begin=0
	i=0
	result=[]
	while i<len(s): 
		if s[i]==' ':
			if s[begin:i]!=[]:
				result.append(s[begin:i])
			begin=i+1
		if i==len(s)-1:
			result.append(s[begin:i])
		i+=1
	return result
print split_string("This is a test string!")
