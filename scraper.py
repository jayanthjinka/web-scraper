import requests
from bs4 import BeautifulSoup

url = input("Enter webpage URL: ")

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = []

    for tag in soup.find_all(["h1", "h2", "h3"]):
        headline = tag.get_text(strip=True)

        if headline:
            headlines.append(headline)

    if headlines:
        print("\nExtracted Headlines:")

        for number, headline in enumerate(headlines, start=1):
            print(f"{number}. {headline}")

    else:
        print("No headlines found.")


except requests.exceptions.Timeout:
    print("Request timed out.")

except requests.exceptions.ConnectionError:
    print("Could not connect to the website.")

except requests.exceptions.HTTPError:
    print(f"HTTP error: {response.status_code}")

except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")
