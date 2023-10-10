from requests_html import HTMLSession
import time
import csv
import requests
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

#parses all pokemon cards off tcgplayer
def parse_poketcg():

    try:

        pokemon_prodinfo = []
        page_nums = []

        for i in range(200):
            page_nums.append(i)

        session = HTMLSession()

        for page in page_nums:
            response = session.get(f'https://www.tcgplayer.com/search/pokemon/product?productLineName=pokemon&page={page}&view=grid')
            time.sleep(0.1)
            response.html.render(sleep = 3.0, keep_page = True, scrolldown = 1)
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
                        pokemon_prodinfo.append(card_info)
                        print(card_title.text)
                        print(card_price.text)
                        print(card_link)

        poke_csv = open('pokemon.csv', 'w')
        csv_writer = csv.writer(poke_csv)
        header = csv_writer.writerow(['Title', 'Price', 'Link'])
        poke_csvcontent = csv_writer.writerows(pokemon_prodinfo)
        poke_csv.close()

    except KeyboardInterrupt:
        print("User interrupted the scraping process.")
        
    except Exception as e:
        print(f'An error has occurred: {e}')

    finally:
        session.close()

#parses all digimon cards off tcgplayer
def parse_digimon():
    try:

        digimon_prodinfo = []
        page_nums = []

        for i in range(175):
            page_nums.append(i)

        session = HTMLSession()

        for page in page_nums:
            response = session.get(f'https://www.tcgplayer.com/search/digimon-card-game/product?productLineName=digimon-card-game&page={page}&view=grid')
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
                        digimon_prodinfo.append(card_info)
                        print(card_title.text)
                        print(card_price.text)
                        print(card_link)

        digi_csv = open('digi.csv', 'w')
        csv_writer = csv.writer(digi_csv)
        header = csv_writer.writerow(['Title', 'Price', 'Link'])
        digi_csvcontent = csv_writer.writerows(digimon_prodinfo)
        digi_csv.close()

    except KeyboardInterrupt:
        print("User interrupted the scraping process.")
        
    except Exception as e:
        print(f'An error has occurred: {e}')

    finally:
        session.close()

#grabs raw html from almost any site
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

#parses yugioh cards from tcgplayer
def parse_yugi():
    try:

        yugi_prodinfo = []
        page_nums = []

        for i in range(200):
            page_nums.append(i)

        session = HTMLSession()

        for page in page_nums:
            response = session.get(f'https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={page}&view=grid')
            time.sleep(0.1)
            response.html.render(sleep = 2.5, keep_page = True, scrolldown = 1)
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
                        yugi_prodinfo.append(card_info)
                        print(card_title.text)
                        print(card_price.text)
                        print(card_link)

        yugi_csv = open('yugioh.csv', 'w')
        csv_writer = csv.writer(yugi_csv)
        header = csv_writer.writerow(['Title', 'Price', 'Link'])
        opcsv_content = csv_writer.writerows(yugi_prodinfo)
        yugi_csv.close()

    except KeyboardInterrupt:
        print("User interrupted the scraping process.")
        
    except Exception as e:
        print(f'An error has occurred: {e}')

    finally:
        session.close()


#parses flesh and blood tcg from tcgplayer
def parse_flesh_and_blood():
    try:

        flesh_and_bloodinfo = []
        page_nums = []

        for i in range(190):
            page_nums.append(i)

        session = HTMLSession()

        for page in page_nums:
            response = session.get(f'https://www.tcgplayer.com/search/flesh-and-blood-tcg/product?productLineName=flesh-and-blood-tcg&page={page}&view=grid')
            time.sleep(0.1)
            response.html.render(sleep = 2.5, keep_page = True, scrolldown = 1)
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
                        flesh_and_bloodinfo.append(card_info)
                        print(card_title.text)
                        print(card_price.text)
                        print(card_link)

        flesh_and_bloodcsv = open('flsehandblood.csv', 'w')
        csv_writer = csv.writer(flesh_and_bloodcsv)
        header = csv_writer.writerow(['Title', 'Price', 'Link'])
        opcsv_content = csv_writer.writerows(flesh_and_bloodinfo)
        flesh_and_bloodcsv.close()
    
    except KeyboardInterrupt:
        print("User interrupted the scraping process.")
        
    except Exception as e:
        print(f'An error has occurred: {e}')

    finally:
        session.close()

#parses funko pops from tcgplayer
def parse_funkopops():
    try:

        funk_prodinfo = []
        page_nums = []

        for i in range(171):
            page_nums.append(i)

        session = HTMLSession()

        for page in page_nums:
            response = session.get(f'https://www.tcgplayer.com/search/funko/product?productLineName=funko&view=grid&page={page}')
            time.sleep(0.1)
            response.html.render(sleep = 2.5, keep_page = True, scrolldown = 1)
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
                        funk_prodinfo.append(card_info)
                        print(card_title.text)
                        print(card_price.text)
                        print(card_link)

        funko_csv = open('funko_pop.csv', 'w')
        csv_writer = csv.writer(funko_csv)
        header = csv_writer.writerow(['Title', 'Price', 'Link'])
        opcsv_content = csv_writer.writerows(funk_prodinfo)
        funko_csv.close()
    
    except KeyboardInterrupt:
        print("User interrupted the scraping process.")
        
    except Exception as e:
        print(f'An error has occurred: {e}')

    finally:
        session.close()


def parse_ebay_electronics():
    try:
        user_search_term = input('Enter a keyword to search for')

        session = HTMLSession()
        ebay_electronics_info = []
        page_num = 1

        while True:

            url = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw={user_search_term}&_sacat=0&_pgn={page_num}'
            response = session.get(url)

            if response.status_code != 200:
                print(f"Failed to retrieve page. Exiting...")
                break # Exit loop on failure
            
            product_containers = response.html.find('div.s-item__info.clearfix')
            prod_titles = response.html.find('div.s-item__title')    
            prod_prices = response.html.find('span.s-item__price')

            if not product_containers: #if false (empty) then no more products
                print('No more products could be found...')
                break

            all_prods_are_adds = True #assumes all products are adds and not actual listings

            for prod_container, prod_title, prod_price in zip(product_containers, prod_titles, prod_prices):
                prod_hrefs = prod_container.find('a')
                
                if prod_hrefs:
                    prod_hreflink = prod_hrefs[0].attrs.get('href')
                    prod_info = [prod_title.text, prod_price.text, prod_hreflink]
                    
                    #if product becomes ebay placeholder we use this block of code to check and set prod adds to false
                    if prod_title.text != 'Shop on eBay' and prod_price.text != '$20.00':
                        ebay_electronics_info.append(prod_info)
                        print(prod_title.text)
                        print(prod_price.text)
                        print(prod_hreflink)
                        all_prods_are_adds = False
                    
            if all_prods_are_adds: # if product adds is True then last block determined all are adds and we break
                print('No more products only adds remain...')
                break

            print(f'Parsed page {page_num}')
            page_num += 1          
            time.sleep(0.2)

        ebay_elec_csv = open('ebay_electronic.csv', 'w', encoding = 'utf-8')
        csv_writer = csv.writer(ebay_elec_csv)
        header = csv_writer.writerow(['Title', 'Price', 'Link'])
        opcsv_content = csv_writer.writerows(ebay_electronics_info)
        ebay_elec_csv.close()

    except KeyboardInterrupt:
        print("User interrupted the scraping process.")
        
    except Exception as e:
        print(f'An error has occurred: {e}')

    finally:
        session.close()


# def parse_amazon():
#     try:
#         user_search_term = input('Enter a term/category to search for: ')
#         proxy_url = "https://71.86.129.131"
#         session = HTMLSession()
#         session.proxies = {"http": proxy_url, "https": proxy_url}
#         headers = {
#             'Host': 'fls-na.amazon.com',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
#             'Accept': '*/*',
#             'Accept-Language': 'en-US,en;q=0.5',
#             'Accept-Encoding': 'gzip, deflate, br',
#             'Content-Type': 'text/plain;charset=UTF-8',
#             'Content-Length': '379',
#             'Origin': 'https://www.amazon.com',
#             'Connection': 'keep-alive',
#             'Referer': 'https://www.amazon.com/',
#             'Cookie': 'skin=noskin; session-id=138-4190565-6001018; session-id-time=2082787201l; i18n-prefs=USD',
#             'Sec-Fetch-Dest': 'empty',
#             'Sec-Fetch-Mode': 'no-cors',
#             'Sec-Fetch-Site': 'same-site',
#             'DNT': '1',
#             'Sec-GPC': '1',
#             'TE': 'trailers'
#         }

#         amazon_prod_info = []
#         page_num = 1

#         # while True:
#         url = f'https://www.amazon.com/s?k=catnip&crid=38L0F8VD9LNCF&sprefix=catnip%2Caps%2C145&ref=nb_sb_noss_2'
#         response = session.get(url, headers=headers)
#         time.sleep(3)
#         response.html.render(sleep = 3, keep_page = True, scrolldown = 1)

#         prod_titles = response.html.find('span.a-size-base-plus a-color-base a-text-normal')
#         print(response.status_code)
#         print(prod_titles)

#     except:
#         Exception

if __name__ == "__main__":

    try:
        user_input = int(input('Enter a mode 1 to execute 2 to exit: '))
        if user_input == 2:
            exit()
        elif user_input == 1:
            choice = int(input("Stockx(Enter 1), MagicTG(Enter 2), OnePieceTCG(Enter 3), RAWSiteHTML(Enter 4), PokemonTCG(Enter 5), DigimonTCG(Enter 6), Yu-Gi-OhTCG(Enter 7), Flesh and Blood(Enter 8), FunkoPops(Enter 9), Parse Ebay(Enter 10)"))
            if choice == 1:
                parse_stockx()
            elif choice == 2:
                parse_tcgplayermtg()
            elif choice == 3:
                parseone_piecetcg()
            elif choice == 4:
                anysite_html()
            elif choice == 5:
                parse_poketcg()
            elif choice == 6:
                parse_digimon()
            elif choice == 7:
                parse_yugi()
            elif choice == 8:
                parse_flesh_and_blood()
            elif choice == 9:
                parse_funkopops()
            elif choice == 10:
                parse_ebay_electronics()
            elif choice == 11:
                parse_amazon()
            else:
                print('Invalid Choice...')
                
    except ValueError:
        print('Invalid input please enter a number')
    except KeyboardInterrupt:
        print('user interuppted the program')



