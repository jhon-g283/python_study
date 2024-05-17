print("AA")
from bs4 import BeautifulSoup

with open("sample.html","r",encoding="utf-8") as file:
    html_content = file.read()
    dict = {}
    dict["html"] = html_content

    soup = BeautifulSoup(html_content,"html.parser")

    test = soup.prettify()

    print("----")
    print(test)
    print("88888")


    # print(dict["html"])

