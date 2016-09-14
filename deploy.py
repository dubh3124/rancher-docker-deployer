import requests
from requests.auth import HTTPBasicAuth
from aik import ukey, pkey


sitename = input("What is your site name? ")



url = 'http://IP:PORT/v1/containers'


data = { "hostname": "dubdocker","name": sitename ,"imageUuid": "docker:ahumaro/grav-php-nginx", "count":1}

create = requests.post(url=url, data=data, auth=HTTPBasicAuth(ukey, pkey))

print(create)

