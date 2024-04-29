import requests

# Login check
url = 'http://127.0.0.1:5000/login'
data = {'username': 'user1', 'password': 'password1'}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())

# Careers check
url = 'http://127.0.0.1:5000/careers'

response = requests.get(url)

print(response.status_code)
print(response.json())
