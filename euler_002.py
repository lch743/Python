store={}
store[1]=1
store[2]=1
i=3
mark=1;
while mark:
	store[i]=store[i-1]+store[i-2]
	if store[i]>4000000:
		mark=0
	i=i+1
s=0
for j in xrange(1,i-1):
	if store[j]%2==0:
		s=s+store[j]
print s
