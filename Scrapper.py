import requests
import bs4


url_instance = "https://www.amazon.pl/Microsoft-Xbox-1TB-Konsola-Czarna/dp/B08K3F3VQG/ref=sr_1_5?__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2UKXQKV1XWGUC&keywords=xbox+series+x&qid=1671021734&sprefix=xbox+series+x%2Caps%2C175&sr=8-5"


if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

    # url = input("wklej link do przedmiotu: \n")
    respond = requests.get(url_instance, headers=headers)
    doc = bs4.BeautifulSoup(respond.text, "html.parser")

    page_titile = doc.title

    title = doc.find("span", attrs={"id": 'productTitle'})

    prices = doc.find_all(text="zł")
    parent = prices[0].parent.parent

    price_whole = parent.find(["span"], class_="a-price-whole").text
    price_decimal = parent.find(["span"], class_="a-price-fraction").text

    print("Amazon page info:", page_titile.string.strip())
    print("Title:", title.text.strip())
    print("Price:", price_whole + price_decimal, "zł")

    # print(doc.prettify())

