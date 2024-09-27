import requests
from bs4 import BeautifulSoup

def get_key (key_page_url, key_name = "unknown"):
    print (f"\033[3;32;m Записываю ключ \033[1;34m{key_name}\033[3;32;m...\033[0m{' ' * 20}", end='\r')
    response = requests.get(key_page_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        accesskey = soup.find('textarea', {'id': 'accessKey'}).text
        keys_file.write (accesskey + '\n')

def get_key_page_links (page_link):
    page_response = requests.get (page_link, headers=headers)
    if page_response.status_code == 200:
        soup = BeautifulSoup (page_response.text, 'html.parser')
        key_page_links = soup.find_all ('a', {'class': 'row g-0 text-decoration-none'})
        for key_page_link in key_page_links:
            key_page_url = main_page_link + key_page_link.get ('href')
            key_name = ' '.join(key_page_link.find ('h3').text.split())
            get_key (key_page_url, key_name)
        next_page_link = main_page_link + soup.find_all ('a', {'class': 'page-link'})[-1].get ('href')
        if next_page_link != page_link:
            get_key_page_links (next_page_link)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
domain = "openkeys.net" # Домен зеркала (напр. openkeys.net)
pagenum = 1

main_page_link = f'https://{domain}/'
with open ('keys.txt', 'w+') as keys_file:
    get_key_page_links (main_page_link)

