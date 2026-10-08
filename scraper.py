import requests

url = input("Enter webpage URL: ")

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

except requests.exceptions.Timeout:
    print("Request timed out.")

except requests.exceptions.ConnectionError:
    print("Could not connect to the website.")

except requests.exceptions.HTTPError:
    print(f"HTTP error: {response.status_code}")

except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")
