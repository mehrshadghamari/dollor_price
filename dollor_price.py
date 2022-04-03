import requests


x=requests.get('https://dapi.p3p.repl.co/api/?currency=usd')

y=x.json()
k=y["Price"]

print(f'gheymat dollor be riyal {k}')