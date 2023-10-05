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

parse_stockx()
