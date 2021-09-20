import requests
from bs4 import BeautifulSoup
# import lxml   # if html.parser fails

def get_number(s: str):
    subs = s.split()
    return int(subs[0])

response = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(response.text, "html.parser")

stories = soup.select(".storylink")
scores = soup.select(".score")

data = []
for story, score in zip(stories, scores):
    data.append(
            {
                "title": story.getText(),
                "link": story.get("href"),
                "score": get_number(score.getText())
            }
    )

data_sorted = sorted(data, key=lambda x: x["score"], reverse=True)
print(data_sorted)

# EXAMPLES:

# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# all_a = soup.find_all(name="a")
#
# all_p = soup.find_all(name="p")
#
# for tag in all_p:
#     print(tag.getText())
#
# for tag in all_a:
#     print(tag.get("href"))
#
# print(soup.find(name="h3", class_="heading").getText())
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name_tag = soup.select_one(selector="#name")
# print(name_tag)
#
# headings = soup.select(selector=".heading")
# print(headings)
