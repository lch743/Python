def make_hashtable(nbuckets):
	s=[]
	i=0
	while i<nbuckets:
		s.append([])
		i+=1
	return s
print make_hashtable(3)
