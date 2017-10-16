

import map_api


def _status_code_is_0(incoming_dict: dict) -> bool:

    if incoming_dict['info']['statuscode'] != 0:
        return False
    else:
        return True


class STEPS:
    def __init__(self):
        self

    def print_out(self, add_list):
        print_list = ['\nDIRECTIONS']

        for number in range(len(add_list) - 1):
            json_output = map_api.get_route_search_result(add_list[number], add_list[number + 1])

            if _status_code_is_0(json_output):
                for key in json_output['route']['legs'][0]['maneuvers']:
                    print_list.append(key['narrative'])
            else:
                break

        if _status_code_is_0(json_output):
            for i in print_list:
                print(i)
        else:
            print('\nDIRECTIONS\nNO ROUTE AVAILABLE')


class TOTALDISTANCE():
    def __init__(self):
        self

    def print_out(self, add_list):
        total_distance = 0
        for number in range(len(add_list) - 1):
            json_output = map_api.get_route_search_result(add_list[number], add_list[number + 1])
            total_distance += json_output['route']['distance']

        print('\nTOTAL DISTANCE: {} miles'.format(round(total_distance)) )


class TOTALTIME:
    def __init__(self):
        self

    def print_out(self, add_list):
        total_time = 0

        for number in range(len(add_list) -1):
            json_output = map_api.get_route_search_result(add_list[number], add_list[number + 1])
            if _status_code_is_0(json_output):
                total_time += json_output['route']['time'] / 60

        print('\nTOTAL TIME: {} minutes'.format(round(total_time)))

class LATLONG:
    def __init__(self):
        self

    def print_out(self, add_list):
        print_list = ['\nLATLONGS']

        for number in range(len(add_list) - 1):
            json_output = map_api.get_route_search_result(add_list[number], add_list[number + 1])

            location_lat = json_output['route']['locations'][0]['latLng']['lat']
            location_lng = json_output['route']['locations'][0]['latLng']['lng']

            last_location_lng = json_output['route']['locations'][-1]['latLng']['lng']
            last_location_lat = json_output['route']['locations'][-1]['latLng']['lat']

            if location_lat >= 0:
                lat_str = '{0:.2f}N'.format(location_lat)
            else:
                lat_str = '{0:.2f}S'.format(0-location_lat)

            if location_lng >= 0:
                lng_str = '{0:.2f}E'.format(location_lng)
            else:
                lng_str = '{0:.2f}W'.format(0-location_lng)

            if last_location_lat >=0:
                last_lat_str = '{0:.2f}N'.format(last_location_lat)
            else:
                last_lat_str = '{0:.2f}S'.format(0-last_location_lat)

            if last_location_lng >= 0:
                last_lng_str = '{0:.2f}E'.format(last_location_lng)
            else:
                last_lng_str = '{0:.2f}W'.format(0-last_location_lng)

            print_list.append('{} {}'.format(lat_str, lng_str))

        print_list.append('{} {}'.format(last_lat_str, last_lng_str))

        for i in print_list:
            print(i)


class ELEVATION:
    def __init__(self):
        self

    def print_out(self, add_list):
        print_list = ['\nELEVATIONS']

        for number in range(len(add_list) - 1):
            json_output = map_api.get_route_search_result(add_list[number], add_list[number + 1])

            location_lat = json_output['route']['locations'][0]['latLng']['lat']
            location_lng = json_output['route']['locations'][0]['latLng']['lng']
            last_location_lat = json_output['route']['locations'][-1]['latLng']['lat']
            last_location_lng = json_output['route']['locations'][-1]['latLng']['lng']

            elevation = map_api.get_eleva_search_result('{},{}'.format(location_lat, location_lng))
            print_list.append(str(round(elevation['elevationProfile'][0]['height'] * 3.2808)))

        last_elevation = map_api.get_eleva_search_result('{},{}'.format(last_location_lat, last_location_lng))

        print_list.append(str(round(last_elevation['elevationProfile'][0]['height'] * 3.2808)))

        for i in print_list:
            print(i)
