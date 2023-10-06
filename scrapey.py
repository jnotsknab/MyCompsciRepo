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


#parses sneakers off stockx and stores in csv
def parse_stockx():
    try:

        stockxproduct_info = []
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

        session.close()
        stockx_csv = open('stockxdata.csv', 'w')
        csv_writer = csv.writer(stockx_csv)
        header = csv_writer.writerow(['Name', 'Price', 'Link'])
        csv_contents = csv_writer.writerows(stockxproduct_info)
        stockx_csv.close()

    except KeyboardInterrupt:
        print('User interrupted the scraping process.')

    except Exception as e:
        print(f'An error has occurred: {e}')

#parses magic the gathering cards off tcg player and stores in csv
def parse_tcgplayermtg():
    try:

        tcg_prodinfo = []
        page_nums = []

        for i in range(5):
            page_nums.append(i)
        session = HTMLSession()

        for page in page_nums:
            response = session.get(f'https://www.tcgplayer.com/search/magic/product?productLineName=magic&page={page}&view=grid')
            time.sleep(0.1)
            response.html.render(sleep = 2.0, keep_page = True, scrolldown=1)
            card_titles = response.html.find('span.search-result__title')
            card_prices = response.html.find('span.search-result__market-price--value')
            card_containters = response.html.find('div.search-result__content')

            for card_title, card_price, card_container in zip(card_titles, card_prices, card_containters):
                card_links = card_container.find('a')

                if card_links:
                    card_href = card_links[0].attrs.get('href')

                    if card_href:
                        card_link = f'https://www.tcgplayer.com{card_href}'
                        product_info = [card_title.text, card_price.text, card_link]
                        tcg_prodinfo.append(product_info)
                        print(card_title.text)
                        print(card_price.text)
                        print(card_link)

        mtg_csv = open('mtg.csv', 'w')
        csv_writer = csv.writer(mtg_csv)
        header = csv_writer.writerow(['Card Name', 'Card Price', 'Link'])
        csv_contenets = csv_writer.writerows(tcg_prodinfo)
        mtg_csv.close()

    except KeyboardInterrupt:
        print("User interrupted the scraping process.")
        
    except Exception as e:
        print(f'An error has occurred: {e}')

    finally:
        session.close()
        


#parse one piece cards off tcgplayer
def parseone_piecetcg():
    try:

        op_prodinfo = []
        page_nums = []

        for i in range(58):
            page_nums.append(i)

        session = HTMLSession()

        for page in page_nums:
            response = session.get(f'https://www.tcgplayer.com/search/one-piece-card-game/product?productLineName=one-piece-card-game&page={page}&view=grid')
            time.sleep(0.1)
            response.html.render(sleep = 2.0, keep_page = True, scrolldown = 1)
            card_titles = response.html.find('span.search-result__title')
            card_prices = response.html.find('section.search-result__market-price')
            card_containters = response.html.find('div.search-result__content')

            for card_title, card_price, card_container in zip(card_titles, card_prices, card_containters):
                card_hrefs = card_container.find('a')

                if card_hrefs:
                    card_href = card_hrefs[0].attrs.get('href')

                    if card_href:
                        card_link = f'https://www.tcgplayer.com{card_href}'
                        card_info = [card_title.text, card_price.text, card_link]
                        op_prodinfo.append(card_info)
                        print(card_title.text)
                        print(card_price.text)
                        print(card_link)

        op_csv = open('onepiece.csv', 'w')
        csv_writer = csv.writer(op_csv)
        header = csv_writer.writerow(['Title', 'Price', 'Link'])
        opcsv_content = csv_writer.writerows(op_prodinfo)
        op_csv.close()

    except KeyboardInterrupt:
        print("User interrupted the scraping process.")
        
    except Exception as e:
        print(f'An error has occurred: {e}')

    finally:
        session.close()




def anysite_html():
    try:

        user_input = input('Enter a site to grab html from: ')
        session = HTMLSession()
        response = session.get(user_input)
        response.html.render(sleep = 5.0, scrolldown = 1)
        site_html = response.html.html

        print(site_html)

        timestamp = int(time.time())
        rand_file_name = f'rawhtml_{timestamp}.txt'
        rawhtml_txt = open(rand_file_name, 'w', encoding='utf-8')
        rawhtml_txt.write(f'Raw HTML from {user_input}:\n')
        rawhtml_txt.write(site_html)
        rawhtml_txt.close()

    except KeyboardInterrupt:
        print("User interrupted the scraping process.")
        
    except Exception as e:
        print(f'An error has occurred: {e}')

    finally:
        session.close()







if __name__ == "__main__":

    try:
        user_input = int(input('Enter a mode 1 to execute 2 to exit: '))
        if user_input == 2:
            exit()
        elif user_input == 1:
            choice = int(input("Stockx(Enter 1), MagicTG(Enter 2), OnePieceTCG(Enter 3), RAWSiteHTML(Enter 4)"))
            if choice == 1:
                parse_stockx()
            elif choice == 2:
                parse_tcgplayermtg()
            elif choice == 3:
                parseone_piecetcg()
            elif choice == 4:
                anysite_html() 
            else:
                print('Invalid Choice...')
                
    except ValueError:
        print('Invalid input please enter a number')
    except KeyboardInterrupt:
        print('user interuppted the program')



