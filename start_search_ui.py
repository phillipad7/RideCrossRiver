# Chaoyi Wang ID: 75959618
# Project 3
# This module is used to reads the input and constructs the objects that
# will generate the program's output

import bunch_outputs


def get_num_of_addresses() -> int:
    '''
    Return the number of addresses the search will encounter
    '''
    while True:
        try:
            num_of_addresses = int(input())
            if num_of_addresses > 1:
                return num_of_addresses
            else:
                print('You must specify at least two locations')
        except:
            print('The first line must specify a positive integer number of locations.')


def get_addresses(this_many: int) -> list:
    '''
    Return a list of addresses with this_many from user input
    '''
    add_list = []
    for number in range(this_many):
        add_list.append(input())
    return add_list


def get_num_of_outputs() -> int:
    '''
    Return the number of desired outputs the search would like to show
    '''
    try:
        num_of_addresses = int(input())
        if num_of_addresses > 0:
            return num_of_addresses
        else:
            print('ERROR10: There must be a positive integer number of generators.')
    except ValueError:
        print('ERROR12: There must be a positive integer number of generators.')


def get_desired_outputs(add_list: [], this_many: int):
    '''
    Print out the search result with user desired categories,
    '''
    output_choices = {'STEPS': bunch_outputs.STEPS(),
                      'TOTALTIME': bunch_outputs.TOTALTIME(),
                      'LATLONG': bunch_outputs.LATLONG(),
                      'ELEVATION': bunch_outputs.ELEVATION(),
                      'TOTALDISTANCE': bunch_outputs.TOTALDISTANCE()
                      }
    desired_output = []

    if _is_int(this_many):
        try:
            for number in range(this_many):
                t = input()
                desired_output.append(output_choices[t])

        except KeyError:
            if t == '':
                print('Invalid output type: undefined')
            else:
                print('invalid output type: {}'.format(t))
        else:
            for i in desired_output:
                i.print_out(add_list)


def display_copyright() -> None:
    '''
    Print copyright statement
    '''
    print('\nDirections Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')


def _is_int(numb) -> bool:
    '''
    Return True if the given parameter is integer, return False if not
    '''
    if type(numb) == int:
        return True
    else:
        return False


if __name__ == '__main__':
    try:
        address_list = get_addresses(get_num_of_addresses())
        num_of_output = get_num_of_outputs()
        get_desired_outputs(address_list, num_of_output)

    except:
        print('\nNO ROUTE FOUND')
    else:
        display_copyright()