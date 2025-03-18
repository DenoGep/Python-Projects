from bs4 import BeautifulSoup
# import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find(name='a').get("href")
    article_links.append(link)

subtexts = soup.findAll(class_="subtext")
article_upvotes = [int(line.span.span.getText().strip(" points")) if line.span.span else 0 for line in subtexts]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(
    f"Most upvoted article: {article_texts[largest_index]}\n"
    f"Number of upvotes: {article_upvotes[largest_index]} points\n"
    f"Available at: {article_links[largest_index]}."
)






''' Beautiful Soup Notes and Study
with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")  # instead of html.parser "lxml" can be used for other websites

# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.p)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())

company_url = soup.select_one(selector="p a")
print(company_url)
'''