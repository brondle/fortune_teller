from time import sleep
import random
import cups
import os
import json

conn = cups.Connection()
printers = conn.getPrinters()
printer_name = list(printers.keys())[0]


def get_reading(data, index, key):
	textfile = open('textfile.txt', 'w')
	textfile.seek(0)
	textfile.truncate()
	card = data['tarot_interpretations'][index]
	print(card)	
	fortune = card['fortune_telling'][random
.randint(0, len(card['fortune_telling'])-1)]
	name = card['name']
	textfile.write(key + ': \n')
	textfile.write('card: ' + name + '\n')
	textfile.write('fortune: ' + fortune + '\n\n\n')
	textfile.close()
	conn.printFile(printer_name, os.path.abspath('textfile.txt'), "text_output", {"cpi": "17", "lpi":"7", "l": "true"})
	



def print_reading():
        print('printing reading')
        with open('tarot.json') as json_file:
            data = json.load(json_file)
            indices = {'past' :random.randint(0, 77), 'present': random.randint(0, 77), 'future': random.randint(0, 77)}
            for (key, value) in indices.items():
                    get_reading(data, value, key)
            
            



