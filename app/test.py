import json
import requests

# url = 'http://localhost:5000/stories'
url = 'http://54.236.22.180/stories'

data = {"yo": 6}

jdata = json.dumps(data)

headers = {'Content-Type': "application/json; charset=xxxe", 'Accept': "application/json"}

params = {"url": "https://www.imdb.com/title/tt0117500/reviews"}

response = requests.post(url=url, params=params,json=jdata, headers=headers)

# print(response.status_code)
# print(response.raise_for_status())
# print(response.status_code)
# print(response.content)
# print(response.cookies)
# print(response.headers)


data = response.content
print(data)

j = json.loads(data)

print()
print()
# print(j)

id = j['id']

print(f"id: {id}")



response = requests.get(url=f'http://localhost:5000/stories/{id}', json=jdata)

print(response.content)


# response = requests.get(url=url, json=jdata)
# #
# #
# # print(response.status_code)
# # print(response.content)
# # print(response.cookies)
# # print(response.headers)
# #
# #
# # print()
# # print()
