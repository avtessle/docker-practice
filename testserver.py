import requests

url = "http://flask_app:5000/add"   # replace with your actual server URL
data = {
    "title": "Buy groceries"
}

response = requests.post(url, data=data)
