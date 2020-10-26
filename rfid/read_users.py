import csv

with open('users/users.csv', mode='r') as infile:
    csv_reader = csv.reader(infile)
    users = {int(rows[0]):rows[1] for rows in csv_reader}

for id_ in users:
  print(f"{id_}\t-\t{users[id_]}")
