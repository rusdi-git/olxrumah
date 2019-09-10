import json

data0 = {'nama':'Budi','asal':'Tasikmalaya'}

data = [
    {'nama':'Rusdi','asal':'Bandung'},
    {'nama':'Adit','asal':'Madiun'},
    {'nama':'Dimas','asal':'Bandung'},
]

if __name__ == "__main__":
    # with open('data_file.json','w') as file:
    #     json.dump(data0,file)

    with open('data_file.json','r') as file:
        raw = json.load(file)
        data.append(raw)
    with open('data_file.json','r+') as file:
        try:
            raw = json.load(file)
            data.append(raw)
        except json.JSONDecodeError:
            json.dump(data0,file)
            data.append(data0)

    with open('data_file.json','w') as file:
        json.dump(data,file)