from bs4 import BeautifulSoup
import requests


url="http://konachan.net/post?page="
# response=requests.get(url+str(0))
# print(response.pretiffy)

result=[]

def get_url_list():
	with open(u"url.txt","w") as fp:
		for i in range(10):
			response=requests.get(url+str(i))
			response.encoding="utf-8"
			# print(response.text)
			html=BeautifulSoup(response.text,"html.parser")
			# print(html)
			data=html.find("div",{"class":"content"}).find_all('li')		
			# print(data)
			for pic in data:
				pics=pic.find("img")
				link=pics.get("src")
				result.append(link)				
				fp.write("http:"+link+"\n")

			



get_url_list()
# index=1
# for urlImg in result:
# 	res=requests.get("http:"+urlImg)
# 	with open(u"pics/"+"pic_%d.jpg" % index,"wb") as f:
# 		f.write(res.content)
# 		index+=1



