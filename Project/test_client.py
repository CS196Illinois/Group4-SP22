import requests
URL = "http://127.0.0.1:3000/movies"
PARAMS = {'index': 184}
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
print(r.json())
PARAMS = {'index': 653}
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
print(r.json())
PARAMS = {'index': 927}
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
print(r.json())