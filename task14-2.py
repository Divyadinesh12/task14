#write python script
import requests
base_url="https://www.openbrewerydb.org/"
#fetches brewey on a given states
def get_brweries_by_state(state):
      response=requests.get(f"{base_url}?by_state={state}")
      if response.status_code == 200:
       return response.json()
#list the name of breweries present in the specified state
def  list_brewerystate(states):
    breweries_by_state={}
    for state in states:
        breweries=get_brweries_by_state(state)
        breweries_by_state[state]=[brewery['name'] for brewery in breweries]
        return breweries_by_state
# count the number of brewery
def count_brewery_by_state(states):
    breweries_count_by_states={}
    for state in states:
        breweries=get_brweries_by_state(state)
        breweries_count_by_states[state]=len(breweries)
        return breweries_count_by_states
# count the number of types of breweries in individual cities of specified states
def count_types_by_city(states):
    types_by_city={}
    for state in states:
       breweries=get_brweries_by_state(state)
       for brewery in breweries:
           city=brewery['city'] 
           if city not in types_by_city:
               types_by_city[city]=set()
    types_by_city[city].add(brewery['brewery_type'])    
    return  types_by_city 
#count and list breweries  with website       
def count_websites(states):
    websites_by_states={}
    for state in states:
        breweries=get_brweries_by_state(state)
        websites_by_states[state]=[brewery['website_url']for brewery in breweries if brewery ['website_url']]
        return websites_by_states
states=['Alaska,Maine,New york']
brewery_list=list_brewerystate(states)
print(brewery_list)
brewery_count=count_brewery_by_state(states)
print(brewery_count)
types_by_city=count_types_by_city(states)
print(types_by_city)
websites_by_state=count_websites(states)
print(websites_by_state)


   



