import time
import requests

url = "http://app:5000/add"
data = {"title": "Buy groceries"}

for i in range(10):
    try:
        print(f"Attempt {i+1}: sending request to app...")
        response = requests.post(url, data=data)
        print("Status Code:", response.status_code)
        print("Response text:", response.text)
        break
    except requests.exceptions.ConnectionError:
        print("App not ready yet, retrying in 3 seconds...")
        time.sleep(3)
else:
    raise SystemExit("App did not become ready in time")

