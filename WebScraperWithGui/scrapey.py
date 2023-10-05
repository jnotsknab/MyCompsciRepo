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
source_sites = ['https://stockx.com/sneakers?page=1', 'https://www.tcgplayer.com/']
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
            products = response.html.find('.css-111hzm2-GridProductTileContainer')

            for product in products:
                name = product.find('.css-3lpefb', first = True)
                price = product.find('.css-nsvdd9', first = True)
                link_href = product.find('a', first=True).attrs['href']
                link = f'https://stockx.com{link_href}'

                if name is not None and price is not None:
                    print(name.text)
                    print(price.text)
                    print(link)
                    product_info = [name.text, price.text, link]
                    stockxproduct_info.append(product_info)

    stockx_csv = open('stockxdata.csv', 'w')
    csv_writer = csv.writer(stockx_csv)
    header = csv_writer.writerow(['Name', 'Price', 'Link'])
    csv_contents = csv_writer.writerows(stockxproduct_info)
    stockx_csv.close()

# parse_stockx()

#website #2

def parse_tcgplayer():
    session = HTMLSession()
    #populate page num list with page nums
    page_nums = []
    for i in range(200):
        page_nums.append(i)

    user_input = int(input('Select 1 for MTG, 2 for Pokemon'))
    if user_input == 1:

        for page in page_nums:
            response = session.get(f'https://www.tcgplayer.com/search/magic/product?productLineName=magic&page={page}&view=grid')
            time.sleep(0.5)
            response.html.render(sleep = 2.5, keep_page = True, scrolldown=1)
            card_titles = response.html.find('span.search-result__title')
            card_prices = response.html.find('span.inventory__price-with-shipping')
            card_containters = response.html.find('div.search-result__content')

            for card_title, card_price, card_container in zip(card_titles, card_prices, card_containters):
                card_links = card_container.find('a')

                if card_links:
                    card_href = card_links[0].attrs.get('href')

                    if card_href:
                        card_link = f'https://www.tcgplayer.com{card_href}'
                        print(card_title.text)
                        print(card_price.text)
                        print(card_link)
    
    if user_input == 2:
        pass


parse_tcgplayer()


