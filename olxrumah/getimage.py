import requests
import json
from io import open

data = []
data2 = []

with open('../result.json','r') as file:
    data = json.load(file)

for i in range(len(data)):
    try:
        url = data[i]['supplyImageUrls']
        result = requests.get(url)
        with open('images/{}.jpg'.format(i),'wb') as file:
            file.write(result.content)
        data[i]['imagename']='{}.jpg'.format(i)
        data2.append(data[i])
    except KeyError:
        continue

with open('../result2.json','w') as file:
    json.dump(data2,file)

