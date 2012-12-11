import time
record={}
def fibonacci(n):
	if n==0:
		if n not in record:
			record[n]=0
		return record[n]
	if n==1:
		if n not in record:
			record[n]=1
		return record[n]
	if n not in record:
		record[n]=fibonacci(n-1)+fibonacci(n-2)
	return record[n]
def exec_func(record,proc,proc_arg):
	start=time.clock()
	if proc_arg not in record:
		result=proc(proc_arg)
		record[proc_arg]=result
	runtime=time.clock()-start
	return record[proc_arg],runtime
	
v,t=exec_func(record,fibonacci,100)
v1,t1=exec_func(record,fibonacci,100)
print "%d,%.10f" %(v,t)
print "%d,%.10f" %(v1,t1)
