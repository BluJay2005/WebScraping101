import requests
from bs4 import BeautifulSoup

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
    if next_btn:
        next_page = next_btn.find("a")["href"]
    else:
        next_page = None


        print(f"Quote: {text}")
        print(f"Author: {author} ")
        print(f"Tags: {', '.join(tags)}")
        print("-" * 40)


print(f"Total quotes scraped: {len(all_quotes)}")