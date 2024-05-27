# # excercise 10
# use the request module 
# use the news api  to fetch the daily news related to different topicd 
# got to https://newsapi.org/
# and explore the variouse options to build the various options to buold your application


# import requests 
# import json

# API_KEY = "#"
# url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'

# r = requests.get(url)
# data = json.loads(r.content)
# print(data)
# for i in range(len(data)):
#     i=1
#     print(i,data['articles'][i]['title'])
#     print(i,data['articles'][i]['description'])
#     i=i+1


import requests 

# API_KEY = "#"
# url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'

# response = requests.get(url)
# data = response.json()

# articles = data['articles']
# for article in articles:
#     print("Title:", article['title'])
#     print("Description:", article['description'])
#     print()

# import requests
# import json
# API_KEY = "#"

# url=f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'

# r=requests.get(url)
# data=r.json()
# articles=data['articles']
# i=1
# for (article) in   articles:
    
#     print(i,"title : \n",article['title'])
#     print("Description : \n",article['description'])
#     i+=1   


import requests
import json
API_KEY='#'
url=f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
r=requests.get(url)
data=json.loads(r.content) # or data= r.json()
articles=data['articles']

for i,article in enumerate(articles,start=1):
    print(f"{i} Tile : \n \t{article["title"]}" )
    print(f"Description : \n \t{ article["description"]}")
    


