import requests
import bs4  # import beautiful soup 4


def print_detail_list():
    """Function to print list of details from Amazon product price"""
    ullist = doc.find_all(["ul"], class_="a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list")
    # det1 = doc.find(["div"], id="detailBullets_feature_div") <--> example of getting id element
    li_elements = ullist[0].find_all("li")
    for el in li_elements:
        el = el.text.split()
        li_2 = "- "
        for i in el:
            li_2 += i + " "
        print(li_2)


if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

    url = input("wklej link do przedmiotu/paste url: \n") # input url
    respond = requests.get(url, headers=headers)    # get respond with requests module
    doc = bs4.BeautifulSoup(respond.text, "html.parser")  # set doc variable with html document received from request

    page_titile = doc.title  # get page title

    title = doc.find("span", attrs={"id": 'productTitle'})  # get title of product

    prices = doc.find_all(text="zł")  # find in html doc list of code samples with text "zł" in it
    parent = prices[0].parent.parent  # use parent twice, to find code for full price
    price_whole = parent.find(["span"], class_="a-price-whole").text  # find whole price
    price_decimal = parent.find(["span"], class_="a-price-fraction").text  # find decimal price

    print("Amazon page info:", page_titile.string.strip())
    print("Title:", title.text.strip())
    print("Price:", price_whole + price_decimal, "zł")
    print("Details:")
    print_detail_list()



