import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://example.com'  # Replace this with the URL of the website you want to scrape
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string.strip()  # Extract the page title
        print(f"Page Title: {title}")
    else:
        print("Failed to fetch the page.")

if __name__ == "__main__":
    main()
