import pandas as pd
import numpy as np

number_variable = 70

string_variable = 'Hi, there'

even_numbers = [2,4,6,8]

my_dictionary = {
    'animal': 'Bear',
    'name': 'Joe',
    'favorite food': ['honey', 'corn'],
    'honey': {
        'color': 'yellow',
        'residue': 'sticky',
        'where': 'forest'     
    }
}

def PriceMatch(online, store):
    if online > 100:
        cost_difference = online - store
        print(f'{online} online cost is more expensive than {store} store cost. Amount: {online} - {store} = {cost_difference}') 

    else: 
        cost_difference = store - online
        print(f'{store} store cost is less expensive than {online} online cost. Amount: {online} - {store} = {cost_difference}')  

online = 150 
store = 100 


PriceMatch(online,store)
