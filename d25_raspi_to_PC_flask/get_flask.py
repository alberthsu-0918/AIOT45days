import requests
r = requests.get('http://10.17.4.132:8080')
if r.status_code == requests.codes.ok:
    print("OK")
print(r.text)
