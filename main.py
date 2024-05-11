import requests
from colorama import Fore,init
from bs4 import BeautifulSoup
init()

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

def find(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []
        facebook_links = soup.find_all('a', href=lambda href: href and 'facebook.com' in href)
        instagram_links = soup.find_all('a', href=lambda href: href and 'instagram.com' in href)
        twitter_links = soup.find_all('a', href=lambda href: href and 'twitter.com' in href)
        for link in facebook_links:
            href = link.get('href')
            print(Fore.BLUE + "Facebook Link:", href)
            links.append(href)
        for link in instagram_links:
            href = link.get('href')
            print(Fore.BLUE + "Instagram Link:", href)
            links.append(href)
        for link in twitter_links:
            href = link.get('href')
            print(Fore.BLUE + "Twitter Link:", href)
            links.append(href)
        return links
    except requests.HTTPError as e:
        pass
    except Exception:
        pass

def blh(link):
    try:
        response = requests.head(link, headers=headers)
        if response.status_code != 200:
            print(response.status_code, link)
            print(Fore.RED + "Broken Link Found:", link)
    except requests.RequestException as e:
        pass

if __name__ == "__main__":
    with open("urls", "r") as f:
        urls = f.readlines()
        for url in urls:
            url = url.strip()
            links = find(url)
            if links is not None:
                for link in links:
                    blh(link)
