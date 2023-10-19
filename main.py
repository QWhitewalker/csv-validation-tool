import csv
import re
import json

# load config.json into python dictionary "config"
configFile = open('config.json')
config = json.load(configFile)

pattern = re.compile(config["columns"]["1"])

def regex_validator():
    if pattern.match(row[1]):
        print("match")
    else:
        print("nomatch")

with open(config["csv-file"],encoding=config["encoding"] ,errors="replace") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=config["delimiter"])
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(row[1])
            line_count += 1
        else:
            print(row[1])
            regex_validator()
            line_count += 1
            #if line_count == 5:
                #break
            #print(f'Processed {line_count} lines.')
    print(f"Processed {line_count} lines.")

def regex_corrector():
    pass