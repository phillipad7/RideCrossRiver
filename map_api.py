

import json
import urllib.parse
import urllib.request

MAPQUEST_API_KEY = 'DiHmG9xQAEZbJjG0WF0iKfCz6GmSJoog'
MAPQUEST_ROUTE_RESOURCE_URL = 'http://open.mapquestapi.com/directions/v2/route?'
MAPQUEST_ELEVA_RESOURCE_URL = 'http://open.mapquestapi.com/elevation/v1/profile?'


def _search_route_url(address_from: str, address_to: str) -> str:
    '''
    Build a route query url with given start and ending address
    '''
    query_parameters = \
        [
            ('key', MAPQUEST_API_KEY), ('from', address_from), ('to', address_to)
        ]
    return MAPQUEST_ROUTE_RESOURCE_URL + urllib.parse.urlencode(query_parameters)


def _search_elevation_url(address_latlng: str) -> str:
    '''
    Build an elevation query url with given string of latitude and longitude
    '''
    query_parameters = [('key', MAPQUEST_API_KEY), ('latLngCollection', address_latlng)]
    return MAPQUEST_ELEVA_RESOURCE_URL + urllib.parse.urlencode(query_parameters)


def get_route_search_result(address_from: str, address_to: str) -> dict:
    '''
    Return the result from the route query url
    '''
    response = None
    try:
        response = urllib.request.urlopen(_search_route_url(address_from, address_to))

        print('type of response: {}'.format(response))
        
        json_text = response.read().decode(encoding='utf-8')
        return json.loads(json_text)
    except:
        print('\nMAPQUEST ERRORER')
    finally:
        if response != None:
            response.close()


def get_eleva_search_result(lat_and_lng: str):
    '''
    Return the elevation result from the given string of latitude and longitude
    '''
    response = None
    try:
        response = urllib.request.urlopen(_search_elevation_url(lat_and_lng))
        json_text = response.read().decode(encoding='utf -8')
        return json.loads(json_text)

    except:
        print('\nMAPQUEST ERROR')

    finally:
        if response != None:
            response.close()

def se():
    pass

##
##if __name__ == '__main__':
##    print('1')
##    print(_search_route_url('irvine, ca', 'santa monica, ca'))
##    get_route_search_result('irvine, ca', 'santa monica, ca')



