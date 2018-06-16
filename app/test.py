import json
import requests

url = 'http://localhost:5000/stories'

data = {"yo": 6}

jdata = json.dumps(data)

headers = {'Content-Type': "application/json; charset=xxxe", 'Accept': "application/json"}

params = {"url": "https://www.imdb.com/title/tt0117500/"}

response = requests.post(url=url, params=params,json=jdata, headers=headers)

print(response.status_code)
print(response.raise_for_status())
print(response.status_code)
print(response.content)
print(response.cookies)
print(response.headers)



# response = requests.get('http://localhost:5000/stories', json=data)

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
