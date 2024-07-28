import requests

url = "http://31.129.97.50:8000/utochnenie_diagnoza"
data = {
    "data": "dataTest"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Failed:", response.status_code, response.text)
