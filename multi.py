from bs4 import BeautifulSoup
import requests
import threadpool
import threading


result=[]

def get_url_list(url):
	print("page:"+url[url.find("=")+1:])
	try:
		response=requests.get(url)
		response.encoding="utf-8"
		# print(response.text)
		html=BeautifulSoup(response.text,"html.parser")
		# print(html)
		data=html.find("div",{"class":"content"}).find_all('li')		
		# print(data)
		urls=[]
		for pic in data:
			pics=pic.find("img")
			link=pics.get("src")
			urls.append("http:"+link)	

		if lock.acquire():
			if url in result:
				result.remove(url)
			with open(u"mulUrl.txt","a") as fp:					
				fp.write("\n".join(urls)+"\n")				
			lock.release()
	except Exception:
		if errLock.acquire():			
			result.append(url)			
			errLock.release()

lock = threading.Lock()
errLock = threading.Lock()
pool=threadpool.ThreadPool(50)

argsUrl="http://konachan.net/post?page="
urls=[]
for i in range(1000):
	urls.append(argsUrl+str(i))

reqs=threadpool.makeRequests(get_url_list,urls)
[pool.putRequest(req) for req in reqs]  
pool.wait()  

while len(result)>0:
	reqs=threadpool.makeRequests(get_url_list,result)
	[pool.putRequest(req) for req in reqs]  
	pool.wait()  