import requests

url = "http://localhost:5029/api/Values"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)
    print("Response Status Code:", response.status_code)
    print("Response JSON:", response.json())
except requests.exceptions.RequestException as e:
    print("Error:", e)
