import requests

class krogerClient:
    def __init__(self):
        self.token = None

    def authenticate(self):
        """authenticate to kroger api and get access token
        """

        api_key = self.read_api_key()

        url = "https://api.kroger.com/v1/connect/oauth2/token"

        headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': f'Basic {api_key}',
            }
        
        payload = {
                'grant_type':"client_credentials",
                'scope':['product.compact'],
            }
        

        response = requests.post(url, headers=headers, data=payload)

        # set access token in krogerClient obj
        self.token = response.json().get('access_token')

    def read_api_key(self):
        """read in the local base64 encoded cred file

        returns:
        --------
        api_key : str
            base64 encoded credential
        """    
    
        try:
            # windows compatible
            f = open('.//api_key.txt')
        except:
            # linux compatible
            f = open('./api_key.txt')

        line = f.read()
        api_key = line.strip()
            
        return api_key

    def product_search_term(self, location_id, term, limit=5):
        """send GET request to search kroger products by term

        parameters:
        -----------
        location_id : str
            the kroger store id number
        term : str
            product search term
        limit : int
            the number of products to return

        returns:
        --------
        response.json() : str
            product info in json format
        """
        
        headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.token}',
            }

        params = {
        'filter.term': f'{term}',
        'filter.locationId': f'{location_id}',
        'filter.fulfillment': 'csp',
        'filter.limit': limit
        }

        response = requests.get('https://api.kroger.com/v1/products', headers=headers, params=params)

        return response.json()
    
    def product_details(self, location_id, product_id):
        """Provides access to the details of a specific product by using the productId

        parameters:
        -----------
        location_id : str
            the kroger store id number
        product_id : str
            the product id number
        
        returns:
        --------
        response.json() : str
            product info in json format
        """
        
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.token}',
            }

        params = {
            'filter.locationId' : f'{location_id}',
            'filter.fulfillment' : 'csp'
        }

        response = requests.get(f'https://api.kroger.com/v1/products/{product_id}', headers=headers, params=params)

        return response.json()