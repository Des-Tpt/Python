import csv
with open('datacsv.csv', newline='') as f: #Thay thế datacsv.csv bằng đường dẫn của file csv.
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row[0], "\t", row[1])