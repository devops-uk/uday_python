# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# response = requests.get("https://www.flipkart.com/tyy/4io/~cs-xj7gdemumj/pr?sid=tyy,4io&collection-tab-name=Redmi+Note+12+Pro+5G&param=6765363&otracker=clp_banner_1_14.bannerX3.BANNER_mobile-phones-big-saving-days-jan23-56hj-store_FMM4NVEBNJK7&fm=neo%2Fmerchandising&iid=M_1759d3b9-b177-460f-8912-e2ef29043ab2_14.FMM4NVEBNJK7&ppt=hp&ppn=homepage&ssid=ifyq0spp5d715dds1678817793060")
# print(response)
# soup = BeautifulSoup(response.content, "html.parser")
# print(soup)
# names = soup.find_all("div", class_ = "KzDlHZ")
# print(names)
# name = []
# for i in names[0:10]:
#     d = i.get_text()
#     name.append(d)
# print(name)

# ratings = soup.find_all("div", class_ = "XQDdHH")
# print(ratings)
# star = []
# for i in ratings[0:10]:
#     d = i.get_text()
#     star.append(float(d))
# print(star)

# prices = soup.find_all("div", class_ = "Nx9bqj _4b5DiR")
# print(prices)
# price = []
# for i in prices[0:10]:
#     d= i.get_text()
#     price.append(d)
# print(price)


# DByuf4
# images = soup.find_all("img", class_="DByuf4")
# print(images)
# image = []
# for i in images[0:10]:
#     d= i['src']
#     image.append(d)
# print(image)

# df = pd.DataFrame()
# print(df)
# df['Names'] = name
# df['Prices'] = price
# df['Ratings'] = star
# df['Images'] = image
# print(df)

# df.to_csv("mobiles.csv")