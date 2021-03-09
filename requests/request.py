import requests

url="https://ya.ru"
response = requests.get(url)
print(f'the request to {url} return the status : {response.status_code}')