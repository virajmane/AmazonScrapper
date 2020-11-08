from selectorlib import Extractor
import requests

headers = {
    'authority': 'www.amazon.in',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}
def scrape(url):
    e = Extractor.from_yaml_file('review.yml')
    if "/dp/" in url:
        url = url.replace("/dp/", "/product-review/")
    r = requests.get(url, headers=headers)
    data = e.extract(r.text)
    return data
def product(name):
    url = "https://www.amazon.in/s?k="+name
    e = Extractor.from_yaml_file('search.yml')
    r = requests.get(url, headers=headers)
    data = e.extract(r.text)
    return data
