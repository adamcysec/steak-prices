import requests
from krogerlib import krogerClient
import csv
from datetime import datetime
from os.path import exists

def main():
    kClient = krogerClient() 
    kClient.authenticate()

    terms = ['steak ribeye', 'steak sirlon', 'steak tbone', 'steak top loin']

    # search kroger for each type of steak
    for term in terms:
        products = find_steaks(kClient, term)
        out_csv(products, term)
    
def find_steaks(kClient, term):
    """query kroger for steak products

    parameters:
    -----------
    kClient : krogerClient
        the kroger client object
    term : str
        the product term to search

    returns:
    --------
    products : list
        contains json object for each product found
    """
    
    location_id = '03400179' # my local kroger
    limit = 50

    data = kClient.product_search_term(location_id, term, limit)
    
    products = []

    for item in data['data']:
        product_id = item['productId']
        try:
            brand = item['brand']
        except:
            brand = None

        product_name = item['description']

        # skip products for dog food
        if 'Dog Food' in product_name:
            continue

        reg_price = item['items'][0]['price']['regular']
        onSale_price = item['items'][0]['price']['promo']

        if onSale_price == 0:
            onSale_price = None

        today_date = datetime.now().strftime("%F")

        data_json = {'date': today_date, 'store':'kroger', 'name': product_name, 'id': product_id, 'brand': brand, 'price': reg_price, 'sale_price': onSale_price}
        products.append(data_json)

    return products

def out_csv(products, term):
    """save steak data to a csv file

    parameters:
    -----------
    products : list
        contains json object for each product found
    term : str
        the steak search term used
    """
    
    steak_name = term.replace(' ', '_')
    
    file_name = f"kroger_data_{steak_name}.csv"

    file_exists = exists(f"./{file_name}")
    
    with open(file_name, 'a', newline='') as csvfile:
        fieldnames = ['date', 'name', 'store', 'id', 'brand', 'price', 'sale_price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()
        
        for product in products:
            writer.writerow(product)
    
    print(f"file saved: ./{file_name}")

if __name__ == '__main__':
    main()