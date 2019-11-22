import requests
from bs4 import BeautifulSoup
import json
from bottle import route, run


 

result = requests.get("https://www.news18.com/india/")


print(result.status_code)

src=result.content
soup=BeautifulSoup(src,'lxml')

urls = []
for a_tag in soup.find_all('p'):
    title_tag = a_tag.find('a')
    urls.append(title_tag)

#print(urls)


L = ['L','O','L']
makeitastring = ''.join(map(str,urls))
#print(makeitastring)

x = {
  "name": "anormous",
  "news": makeitastring,
  "city": "un"
}
y = json.dumps(x)

print(y)

@route('/')
def home():
    return "<h1> Home page<h1>"

@route('/api')
def hello():
    return {"news":y}

run(host='localhost', port=8080, debug=True)
  