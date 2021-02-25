import requests
r = requests.get('http://169.254.27.173:8080')
if r.status_code == requests.codes.ok:
    print("OK")
print(r.text)
