import requests 

def getsum(text=None):
    if text == None:
        request='https://en.wikipedia.org/api/rest_v1/page/random/summary'
    else:
        request=f'https://en.wikipedia.org/api/rest_v1/page/summary/{text}'
    result = requests.get(request)
    json = result.json()
    return json['extract']

if __name__ == '__main__':
    req = getsum('Fortnite: Battle Royale')
    print(req)
    nullreq = getsum()
    print(nullreq)