import requests
from bs4 import BeautifulSoup
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    url = 'https://xicons.org/#/'

    respone = requests.get(url=url, headers=headers)
    respone.encoding = 'utf-8'
    
    text_html = respone.text

    soup = BeautifulSoup(text_html, "html.parser")
    print(soup)