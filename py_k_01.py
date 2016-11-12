from bs4 import BeautifulSoup

data_list = [];
with open(
        "web\\new_index.html",
        "r") as file:
    soup = BeautifulSoup(file, "lxml")
    title_list = soup.select("body > div.main-content > ul > li > div.article-info > h3 > a")
    des_list = soup.select("body > div.main-content > ul > li > div.article-info > p.description")
    rate_list = soup.select("body > div.main-content > ul > li > div.rate > span")
    img_list = soup.select("body > div.main-content > ul > li > img")
    type_list = soup.select("body > div.main-content > ul > li > div.article-info > p.meta-info")
    # print(title_list, img_list, des_list, rate_list,type_list, sep="\n------------------\n")

for title,des,rate,img,type in zip(title_list,des_list,rate_list,img_list,type_list):
    data = {
        "title" : title.get_text(),
        "des" : des.get_text(),
        "rate" : rate.get_text(),
        "img" : img.get("src"),
        "type" : list(type.stripped_strings)
    }
    data_list.append(data)

# print(data_list)
for each in data_list:
    if(float(each["rate"]) > 3.7):
        print(each)


"""
title:
body > div.main-content > ul > li:nth-child(1) > div.article-info > h3 > a
des:
body > div.main-content > ul > li:nth-child(1) > div.article-info > p.description
rate:
body > div.main-content > ul > li:nth-child(1) > div.rate > span
image:
body > div.main-content > ul > li:nth-child(1) > img
type:
body > div.main-content > ul > li:nth-child(1) > div.article-info > p.meta-info
"""
