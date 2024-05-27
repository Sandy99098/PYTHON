#  news app solution 
import requests 
import json
querry=input("What type of news are yoou intresred in ? ")
url=f"https://newsapi.org/v2/everything?q=tesla&from=2024-04-27&sortBy=publishedAt&apiKey=YOUR APIKEY"
r=requests.get(url)
news=json.loads(r.text)
for article in news['articles']:
    print("Title : \n \t",article['title'])
    print("Description : \n \t",article['description'])
    print()