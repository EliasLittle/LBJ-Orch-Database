import csv

library_file = []
# Users/EliasL/Documents/Code/Projects/Orchestra_Database/library.csv
with open('library.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        values = []
        for val in row:
            values.append(val)
        library_file.append(values)

del library_file[0]

formatted_file = []


def sorf(str):
    strU = str.upper().replace("ORCH", "").replace("ESTRA", "").replace("PIANO", "")
    if any(strU.replace(" ", "") == x for x in(["STRINGS", "STRING", "S"])):
        return "String"
    elif any(strU.replace(" ", "") == x for x in(["FULL", "F"])):
        return "Full"
    elif "OR" in strU:
        return"Both"
    elif strU is None or strU == "":
        return "N/A"
    else:
        return"Other"


for row in library_file:
    writers = row[1].replace("\"", "").split("/")
    if len(writers) == 2:
        comp, arr = writers
    else:
        comp, arr = writers[0], ""

    title = row[2].replace('\"', '')

    if "PIANO" in row[3].upper():
        piano = 'Y'
    else:
        piano = 'N/A'

    comments = ("Notes: %s Scanned: %s Issues: %s" %
                (row[5], row[6], row[7])).replace("\"", "")

    formatted_file.append([int(row[0]), comp, arr, title, sorf(row[3]),
                           row[4], "N/A", piano, "", comments])

with open('formatted_library.csv', mode='w') as new_file:
    csv_writer = csv.writer(new_file)
    for row in formatted_file:
        csv_writer.writerow(row)
