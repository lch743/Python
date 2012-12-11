path="./page.txt"
file=open(path)
page=file.read()
t='<a href='
end=0;
while end<len(page)-1:
	link=page.find(t,end)
	if link>=0:
		begin=page.find('"',link)
		end=page.find('"',begin+1)
		url=page[begin+1:end]
		print url
	end=end+1
