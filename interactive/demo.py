#!/usr/bin/python3.5
import sys
import csv
import time

COMMA = ','
QUOTE = '"'
TRUE_BIT = '1'
FALSE_BIT = '0'

def read_bitmaps(file_name):
    bitmap_to_item = {}
    with open(file_name) as csvfile:
        reader = csv.reader(csvfile, delimiter = COMMA, quotechar = QUOTE)
        for line in reader:
            item_name, bitmap = line
            bitmap_to_item[bitmap] = item_name
    return bitmap_to_item

def get_bit(answer):
    if answer is 'y':
        return TRUE_BIT
    return FALSE_BIT

def main(bitmap_file_name):
    bitmap_to_item = read_bitmaps(bitmap_file_name)
    
    answer = ''
    current_bitmap = 'X'

    # ask root question
    start = time.time()
    print('QUESTION: %s' % bitmap_to_item[current_bitmap])

    while True:
        answer = input('  ANSWER: ')
        current_bitmap += get_bit(answer)

        if current_bitmap in bitmap_to_item:
            if '?' in bitmap_to_item[current_bitmap]:
                print('QUESTION: %s' % bitmap_to_item[current_bitmap])
            else:
                print('    ITEM: %s' % bitmap_to_item[current_bitmap])
                end = time.time()
                print('\n---- Experimenter\'s Use ----')
                print(' TREE FILE: %s' % bitmap_file_name)
                print('TIME TAKEN: %.3f SECONDS' % (end-start))
                break
    return

main(sys.argv[1])
