import requests
import json 

def getquote(maxlen, minlen):
    json = requests.get(f'api.quotable.io/random?maxLength={maxlen}&minLength={minlen}')
    print(json)


if __name__ == '__main__':
    getquote('25', '30')
    