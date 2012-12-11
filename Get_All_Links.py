
def get_next_target(page):
	first_index=page.find('<a href=')
	begin=page.find('"',first_index)
	end=page.find('"',begin+1)
	url=page[begin+1:end]
	return url,end
def get_all_links(page):
	links=[]
	while True:
		url,endpos=get_next_target(page)
		if url:
			links.append(url)
			page=page[endpos:]
		else:
			break
	return links
def union(p,q):
	for e in q:
		if e not in p:
			p.append(e)
def crawl_web(seed):
	tocrawl=[seed]
	crawled=[]
	while tocrawl:
		s=tocrawl.pop()
		if s not in crawled:
			union(crawled,get_all_links(get_page(s)))
			crawled.append(s)
	return crawled
	
file=open("./page.txt")
page=file.read()
links=get_all_links(page)
l=crawl_web(links)
print l
