# request modules

# import requests

# # get request
# response=requests.get("https://jsonplaceholder.typicode.com/posts")
# print(response.status_code)
# print(response.text)

# #  for making a post request 

# data= {
#     "title":"Atomic Habits ",
#     "Author":"Sandy",
#     "User_Id": 123
# } 
# # headers={
# #     'Content-type':'application/json;
# #     charset=UTF-8,
# # }
# response=requests.post("https://jsonplaceholder.typicode.com/posts",headers=headers,json=data)
# print(" response.status_code") # Print the status code of the response
# print(response.json())          # Print the JSON response from the server
# print(type(data))




# input requests


#  bs4(beautiful soup)
# import requests
# url=" https://jsonplaceholder.typicode.com/posts"
# r=requests.get(url)
# print(r.text)
# from bs4 import BeautifulSoup
# soup =BeautifulSoup(r.text,'html.parser')
# print(soup.prettify())

import requests
from bs4 import BeautifulSoup

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print the raw JSON response text
    print(response.text)
    
    # Parse the JSON response
    json_data = response.json()
    
    # Print the parsed JSON data in a pretty format
    from pprint import pprint
    pprint(json_data)
else:
    print(f"Failed to retrieve data: {response.status_code}")

