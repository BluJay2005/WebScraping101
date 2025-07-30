# 📝 Learning Log: Web Scraping Project

Use this log to track your progress, reflect on what you've learned, and plan your next steps.

---

## 📅 Date:
7/30/2025

## 📚 Topic:
What concept, tool, or task did you work on today?
I I worked with setting up and learning the basics of Scraping, and understanding what to look for in HTML to pull key data.

## 🧠 What I Learned:
Summarize the key takeaways, new concepts, or skills you gained.
I learned how to setup a scraper, how to pull date with the BS library and how to analyze html for the things im looking for
How to send GET requests to the website

    What to look for in HTML:
        The Container: the outer element that wraps each item you want to scrape.
        The Data Elements: inside ach container, they are the tags that holds the data youre looking for. EX: <div class "quote">
            EX: Quote text → <span class="text">
                Author name → <small class="author">
                Tags → <div class="tags"> with nested <a class="tag">
        Classes and IDs: Help you target elements precisely using BS or other tools: (class = "...") or (id="...")
        Text vs. Attributes:
            If the data is visible on the page, its usually a .text
            If the data is in a link or an image, you might need to extract an attribute like href or src
Learned Pagination!! Moving onto the next page until we cant anymore!

Learned span, small and .strip
## 🧩 Challenges:
What was difficult or confusing? Any bugs or roadblocks?
HTML looks like giberish, but when you start to see how it works it helps
## 🔜 Next Steps:
What will you work on next? Any questions or goals for the next session?
I want to scrape more sites, and look at more ways HTML can differ.
I also want to learn what happens when you need api keys
Or deal with Anti Scraper tools

---

Repeat this template for each learning session.
