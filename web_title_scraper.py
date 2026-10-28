import requests
from bs4 import BeautifulSoup
url = "https://example.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(response.status_code)
# print(response.text)
title_tag = soup.find("title")
print(title_tag.text)
if title_tag:
    title = title_tag.text.strip()

    with open("title.txt", "w", encoding="utf-8") as file:
        file.write(title)

    print("Title saved successfully!")

else:
    print("No title found on the webpage.")