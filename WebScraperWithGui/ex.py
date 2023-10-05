from requests_html import HTMLSession
import time
import csv
#initialize session with headers
session = HTMLSession()
session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv: 87.0) Gecko/20100101 Firefox/'
session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
session.headers['Accept-Language'] = 'en-US,en;q=0.5'
session.headers['Connection'] = 'keep-alive'
session.headers['Upgrade-Insecure-Requests'] = '1'
source_sites = ['https://stockx.com/sneakers?page=1']
stockxproduct_info = []

#200 status code means success
def parse_stockx():

    user_in = int(input('Enter mode (1) to quit or mode (2) to execute'))
    if user_in == 1:
        exit()
    elif user_in == 2:

        session = HTMLSession()
        page_num = [1,2,3,4,5,6,7,8,9,10,11,12
                    ,13,14,15,16,17,18,19,20,21,22,23,24,25]
        
        
        for page in page_num:
            response  = session.get(f'https://stockx.com/sneakers?page={page}')
            time.sleep(0.1)
            products_names = response.html.xpath('//p[@class = "chakra-text css-3lpefb"]')
            product_prices = response.html.xpath('//p[@class = "chakra-text css-nsvdd9"]')
            product_links = response.html.absolute_links

            for name, price, product_links in zip(products_names, product_prices, product_links):
                print(name.text)
                print(price.text)
                print(product_links)
                prod_info = [name.text, price.text]
                stockxproduct_info.append(prod_info)

    stockx_csv = open('stockxdata.csv', 'w')
    csv_writer = csv.writer(stockx_csv)
    header = csv_writer.writerow(['Name', 'Price', 'Link'])
    csv_contents = csv_writer.writerows(stockxproduct_info)
    stockx_csv.close()

def parse_tcgplayer():
    session = HTMLSession()
    # Populate page num list with page nums
    page_nums = []
    for i in range(200):
        page_nums.append(i)

    user_input = int(input('Select a subcategory'))
    if user_input == 1:
        for page in page_nums:
            response = session.get(f'https://www.tcgplayer.com/search/magic/product?productLineName=magic&page={page}&view=grid')
            time.sleep(0.5)
            response.html.render(sleep=2.5, keep_page=True, scrolldown=1)
            card_titles = response.html.find('span.search-result__title')
            card_prices = response.html.find('span.inventory__price-with-shipping')
            card_containers = response.html.find('div.search-result__content')

            for card_title, card_price, card_container in zip(card_titles, card_prices, card_containers):
                card_link = card_container.find('a')[0]  # Assuming the card link is the first 'a' element in the container
                card_link_href = card_link.attrs.get('href')
                if card_link_href:
                    card_link = f'https://www.tcgplayer.com{card_link_href}'
                    print(card_title.text)
                    print(card_price.text)
                    print(card_link)

parse_tcgplayer()