import csv
import json

def main():
    csv_file = input("Enter the csv file name (e.g. file.csv): ")
    json_file = input("Enter the json file name (e.g. file.json): ")

    data = []

    try:
        with open(csv_file, 'r', encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        exit(f"❌ Error: The file '{csv_file}' was not found.")
    except Exception as e:
        exit(f"❌ Error reading CSV file: {e}")

    if not data:
        exit("No data in the CSV file, no JSON file created")

    try:
        with open(json_file, 'w', encoding="utf-8") as file:
            file.write(json.dumps(data, indent=4))
            print(f"✅ Successfully converted {csv_file} to {json_file}")
    except Exception as e:
        exit(f"❌ Error writing JSON file: {e}")


if __name__ == '__main__':
    main()