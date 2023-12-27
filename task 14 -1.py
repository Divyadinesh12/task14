#write python program using oops concept
#first install request module using pip install requests command
import requests
#define countrydata class
class countrydata:
#constructor for taking input
    def __init__(self):
        self.url="https://restcountries.com/v3.1/all"
        self.data=self.fetch_data()
# create method to fetch data from the url
    def fetch_data(self):
        response=requests.get(self.url)
        if response.status_code==200:
            return response.json()
        else:
            print("error")
            return None
# create method it shows name of country ,currencies and symbol
    def country_info(self):
        if self.data:
            for country in self.data:
                name=country['name']['common']
                currencies=country['currencies']
                print(name)
                print("currencies:")
                for currency,details in currencies.items():
                    print(f"{currency}:{details['symbol']}")
                print()
# displsy country with dollar as its currency
    def dollar_countries(self):
        if self.data:
          countries=[country['name']['common']for country in self.data if 'USD' in country.get('currencies',{})]
          print(countries) 
# display country with euro as its currency 
    def euro_countries(self):
        if self.data:
            e_countries=[country['name']['common']for country in self.data if 'EUR' in country.get('currencies',{})]
            print(e_countries)  
        


country_data=countrydata()
country_data.country_info()
country_data.dollar_countries()
country_data.euro_countries()