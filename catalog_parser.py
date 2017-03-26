"""
Judy's catalog parsing module.

This module handles the parsing of a catalog in CSV (from a spreadsheet
software) into a wide-format Python dictionary for use with Judy.

Example input:

    item_name,isBoneless?,isBox?,isBurger?,isWrap?
    Zinger,1,0,1,0
    Bandito,1,0,0,1
    Shrooms,1,0,1,0

Note that the 'item_name' field is specially hardcoded to denote the name
of the menu item.

The True bits can be written as '1', 'true', 'True' or 'T'. Anything else
is considered False.

Written by Darren.
"""
import csv

ALL_ITEMS_KEY = 'all'
ITEM_NAME_KEY = 'item_name'
EMPTY_FIELD_NAME = ''

"""
Reads a CSV file for a catalog into a wide-format Python dictionary.

This is like the "main" function of the parser module.
"""
def parse_csv(file_name):
    return transpose_catalog_list(read_csv_to_dictionary_list(file_name))

"""
Transposes a long catalog list into the wide format.
"""
def transpose_catalog_list(catalog_list):
    # assume every catalog entry uses exactly the same schema
    transposed_catalog = spawn_catalog_sets(catalog_list[0].keys())

    for item in catalog_list:
        current_item_name = item[ITEM_NAME_KEY]

        # add to special key-value pair to contain all items
        transposed_catalog[ALL_ITEMS_KEY].add(current_item_name)

        # add to each specific key-value pair
        for key in item.keys():
            if item[key] is True:
                transposed_catalog[key].add(current_item_name)
        
    return transposed_catalog

"""
Reads a CSV file for a catalog into a long format Python dictionary.

The first line is assumed to be the header line, and must contain the field 'item_name'.
"""
def read_csv_to_dictionary_list(file_name):
    catalog_list = []
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            catalog_list.append(item)
    return map_bits_to_boolean(catalog_list)

def map_bits_to_boolean(catalog_list):
    for item in catalog_list:
        # clean dictionary of empty key-value pairs
        del item[EMPTY_FIELD_NAME]

        # map bits to pythonic True/False
        for field in item.keys():
            if field != ITEM_NAME_KEY:
                item[field] = get_equivalent_boolean(item[field])

    return catalog_list

def get_equivalent_boolean(bit):
    if bit is '1' or bit is 'True' or bit is 'true' or bit is 'T':
        return True
    return False

def spawn_catalog_sets(key_list):
    key_list = list(key_list)
    key_list.remove(ITEM_NAME_KEY)
    transposed_catalog = {}
    for key in key_list:
        transposed_catalog[key] = set()
    transposed_catalog[ALL_ITEMS_KEY] = set()
    return transposed_catalog
