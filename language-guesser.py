import csv


language_dict = dict()

with open('letter-frequency.txt', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')

    for i in range(len(csv_reader)):
        row = csv_reader[i]

        if i == 0:
            for language in row:
                language_dict[language] = dict()
        else:
            for language in row:
