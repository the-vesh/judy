import csv

ITEM_NAME_HEADER = 'item_name'
EMPTY_FIELD_NAME = ''

def read_csv_to_dictionary_list(file_name):
    catalog = []
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            catalog.append(item)
    return map_bits_to_boolean(catalog)

def map_bits_to_boolean(catalog_list):
    for item in catalog_list:
        # clean dictionary of empty key-value pairs
        del item[EMPTY_FIELD_NAME]

        # map bits to pythonic True/False
        for field in item.keys():
            if field != ITEM_NAME_HEADER:
                item[field] = get_equivalent_boolean(item[field])

    return catalog_list

def get_equivalent_boolean(bit):
    if bit == '1':
        return True
    return False
