import json

class jsonTools:
    def __init__(self):
        pass
    def getCity():
        f = open('config.json')
        data = json.load(f)
        city = data['city']
        f.close()
        return city
            



