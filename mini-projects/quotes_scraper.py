import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

#base, print quotes
"""
url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

for quote in quotes:
    text = quote.find("span", class_="text").get_text()
    author = quote.find("small", class_="author").get_text()
    tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]

    print(f"Quote: {text}")
    print(f"Author: {author} ")
    print(f"Tags: {', '.join(tags)}")
    print("-" * 40)
"""

#Multipage
base_url = "http://quotes.toscrape.com"
next_page = "/page/1/"
all_quotes = []

while next_page:
    response = requests.get(base_url + next_page)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")
    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]
        all_quotes.append({
            "text": text,
            "author": author,
            "tags": tags
        })

    next_btn = soup.find("li", class_="next")
    next_page = next_btn.find("a")["href"] if next_btn else None

# Print the first 3 quotes from all scraped data
for i in range(min(3, len(all_quotes))):
    quote = all_quotes[i]
    print(f"Quote: {quote['text']}")
    print(f"Author: {quote['author']}")
    print(f"Tags: {', '.join(quote['tags'])}")
    print("-" * 40)

print(f"Total quotes scraped: {len(all_quotes)}")


csv_filename = "quotes.csv"
with open(csv_filename, mode="w", newline = '', encoding = "utf-8") as file:
    writer = csv.DictWriter(file,fieldnames=["text", "author","tags"])
    writer.writeheader()
    writer.writerows(all_quotes)
print(f"CSV Successfully created!")

excel_filename = "quotes.xlsx"
df = pd.read_csv(csv_filename)
df.to_excel(excel_filename, index=False)
