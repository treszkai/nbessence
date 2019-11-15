import json
import logging
import sys

import yaml

def print_block(block_type, lines, file, begin=True):
    if begin:
        begin_char = '-'
    else:
        begin_char = ' '
    print(f'{begin_char} {block_type}: |-', file=file)
    for line in lines:
        print('    ' + line.rstrip('\n'), file=file)


def print_cell(cell: dict, file):
    cell_type = cell['cell_type']
    if cell_type == 'code':
        print_block('code', cell['source'], file)
        try:
            print_block('output', cell['outputs'][0]['text'], file, begin=False)
        except IndexError:
            pass
    elif cell_type == 'markdown':
        print_block('markdown', cell['source'], file)
    elif cell_type == 'raw':
        print_block('raw', cell['source'], file)
    else:
        logging.error(f'Skipping unnown cell type {cell_type}.\n'
                      f'Contents: {cell}')


def nb_to_essence(nb_path, output_path):
    with open(nb_path, 'r') as f:
        in_dict = json.load(f)

    with open(output_path, 'w') as f:
        for cell in in_dict['cells']:
            print_cell(cell, f)


if __name__ == '__main__':
    nb_path = sys.argv[1]
    output_path = nb_path + 'e'
    nb_to_essence(nb_path, output_path)