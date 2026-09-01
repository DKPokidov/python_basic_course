import requests
url = 'https://www.cbr.ru/scripts/XML_daily.asp'
response = requests.get(url)
print(type(response.content)) 
