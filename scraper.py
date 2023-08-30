import os
import requests
from bs4 import BeautifulSoup

def main():
    url = input("Enter the URL to scrape: ")
    
    if not url:
        print("URL is required.")
        return

    try:
        response = requests.get(url, timeout=10, headers={"User-Agent": "MyScraper"})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Failed to fetch the page:", e)
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.get_text(strip=True)
    print(f"Page Title: {title}")

if __name__ == "__main__":
    main()
