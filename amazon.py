import requests
from bs4 import BeautifulSoup
class Amazon:
    def __init__(self,website,expecting):
        self.url = website
        self.target = expecting
        self.product_name = ""
        self.current_price = 0
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "Accept-Language" : "en-GB,en-US;q=0.9,en;q=0.8"
        }
    def scrape_product(self):
        response = requests.get(url=self.url, headers=self.headers)
        content = response.text
        soup = BeautifulSoup(content, "html.parser")
        self.product_name =" ".join(soup.select_one("div#titleSection span#productTitle").getText().split())
        print(self.product_name)
        try :
            self.current_price = int(soup.select_one("span.a-price-whole").getText().replace(",",""))
        except ValueError:
            print("Amount is not viable")
    def check_product(self):
        self.scrape_product()
        if self.current_price < self.target:
            return True
        return False

