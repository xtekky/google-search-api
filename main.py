import json
import requests, re
from bs4 import BeautifulSoup


search = ""

head = {
    'Cookie': 'CONSENT=YES+cb.20210418-17-p0.it+FX+917; ',
    'Accept-Language': 'en-EN'
}

soup = BeautifulSoup(requests.get(f"https://www.google.com/search?q={search}", headers=head).content, "html.parser")
list2 = soup.select("a:has(h3)")
links = []
for a in list2:
    links.append(a["href"].split("=")[1])

list = soup.findAll('div',{'class':'BNeawe s3v9rd AP7Wnd'})
data = {"results": []}
z = 0
y = 0

for x in range(len(list)):
    try:
        data["results"].append({list[z].text: "link_not_found"})
        y += 1
        z += 2
    except IndexError:
        break

for index, obj in enumerate(data['results']):
    for key,val in obj.items():
        if len(links) > index:
            data['results'][index][key] = links[index]


print(json.dumps(data, indent=4))
