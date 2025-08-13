import sys
import csv

def main():
    if len(sys.argv) != 3:
        print("Usage: python scourgify.py before.csv after.csv")
        sys.exit(1)

    before = sys.argv[1]
    after = sys.argv[2]
    clean_data(before, after)

def clean_data(before, after):
    try:
        with open(before, 'r') as file:
            reader = csv.DictReader(file)
            rows = []
            for row in reader:
                # Combine first and last name
                full_name = f"{row['first']} {row['last']}"
                rows.append({'name': full_name, 'house': row['house']})

        with open(after, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'house'])
            writer.writeheader()
            writer.writerows(rows)

    except FileNotFoundError:
        print(f"File {before} not found.")
        sys.exit(1)

if __name__ == '__main__':
    main()
