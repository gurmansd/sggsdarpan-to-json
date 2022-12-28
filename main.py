    
# importing the HTMLSession class
from requests_html import HTMLSession
import json

# create the object of the session
session = HTMLSession()

# url of the page
web_page = 'https://www.gurugranthdarpan.net/0538.html'

# making get request to the webpage
respone = session.get(web_page)

# getting the html of the page
page_html = respone.html

# finding all the paragraphs
all_paragraphs= page_html.find('p')

res = []
i = 2
j = 0

for para in all_paragraphs[2:-2]:
    text = para.text

    if(str(all_paragraphs[i].attrs)[12] == 'B'):
        type = 'Bani'
    if(str(all_paragraphs[i].attrs)[12] == 'A'):
        type = 'Arath'


    data = {'class': type, 'data': text}

    res.append(data)

    i = i + 1


with open('htmlsession.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, ensure_ascii=False)
    
