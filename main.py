import requests

URL = "https://www.knauf.de"
page = requests.get(URL)

print(page.text)

