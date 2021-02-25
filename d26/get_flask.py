import requests
r = requests.get('http://192.168.199.75:8080')
if r.status_code == requests.codes.ok:
    print("OK")
print(r.text)
