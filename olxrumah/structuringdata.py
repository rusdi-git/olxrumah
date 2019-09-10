import json

data = []
data2 = []

with open('../result2.json','r') as file:
    data = json.load(file)

for i in range(len(data)):
    item = data[i]
    try:
        fasilitas = item['fasilitas']
    except KeyError:
        fasilitas = ''
    try:
        price = item['price']
    except KeyError:
        price = 0
    try:
        address = item['address']
    except KeyError:
        address = ''
    try:
        supplyImageUrls = 'images/'+item['imagename']
    except KeyError:
        supplyImageUrls = ''
    try:
        size_value = item['luasbangunan']
    except KeyError:
        size_value = 0
    try:
        additionalInformation = item['deskripsi']
    except KeyError:
        additionalInformation = ''
    try:
        title = item['title']
    except KeyError:
        title = ''
    
    structured_data = {
        "facilities": [fasilitas,],
        "isNegotiablePrice": False,
        "location": {
            "address": address,
            "coordinates": [0,]
            },
        "operationalHours": [
            {
                "timeEnd": "",
                "timeStart": ""
            },
        ],
        "payment_methods": ["cash",],
        "prices": [{
            "period": "one_month",
            "price": price
            },],
        "size": {
            "additionalInformation": additionalInformation,
            "value": size_value
            },
        "supplyImageURLs": [supplyImageUrls,],
        "supplyType": "room",
        "title": title,
        "user_id": ""
        }
    data2.append(structured_data)

with open('../result3.json','w') as file:
    json.dump(data2,file)