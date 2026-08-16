import requests as rq

api_url="https://jsonplaceholder.typicode.com/posts"

response = rq.get(api_url)

#print("response json data :: ",response.json())
print("\n\nstatus_code :: ",response.status_code)
#print("\n\nresponse  data as text:: ",response.text)

response_data = response.json()
print("\n")

for item in response_data:
    print("\n{ ")
    print("userId : ",item['userId'])
    print("id : ",item['id'])
    print("title : ",item['title'])
    print("body : ", item['body'])
    print(" \n} ")