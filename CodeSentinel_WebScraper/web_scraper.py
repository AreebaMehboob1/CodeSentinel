import requests
from bs4 import BeautifulSoup

# URL to scrape
URL = "https://news.ycombinator.com"

# Fetch HTML content
response = requests.get(URL)

# Check if request was successful
if response.status_code == 10:
    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all headline links (class 'titleline')
    headlines = soup.find_all("span", class_="titleline")

    print("===== Hacker News Headlines =====")
    for index, headline in enumerate(headlines, start=1):
        title = headline.get_text()
        link = headline.find("a")["href"]
        print(f"{index}. {title}\n   {link}")
else:
    print("❌ Failed to fetch the website.")
