import requests, bs4


url_instance = "https://www.amazon.pl/Microsoft-512GB-Edycja-Cyfrowa-Konsola/dp/B08K3BRFT3/ref=sr_1_5?crid=1U1UGL4TV1HWJ&keywords=xbox+series+s&qid=1670063054&sprefix=xbox%2Caps%2C128&sr=8-5"


def get_product_name(soup):
    title = soup.find("span", attrs={"id":'productTitle'})
    return title.string.strip()

if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

    #url = input("wklej link do przedmiotu: \n")
    respond = requests.get(url_instance, headers=headers)
    doc = bs4.BeautifulSoup(respond.content, "html.parser")
    print(doc.prettify())
    title = get_product_name(doc)




    print("Title:", title)