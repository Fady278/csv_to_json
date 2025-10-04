import csv
import json

def main():
    csv_file = input("Enter the csv file name (e.g. file.csv): ")
    json_file = input("Enter the json file name (e.g. file.json): ")

    data = []

    with open(csv_file, 'r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    with open(json_file, 'w', encoding="utf-8") as json_file:
        json_file.write(json.dumps(data, indent=4))

if __name__ == '__main__':
    main()