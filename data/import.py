
import os
import MySQLdb
import csv

db = MySQLdb.connect(os.environ.get('DATABASE_URI'))

cursor = db.cursor()
banks = set()
branches = set()

with open("./data/bank_branches.csv") as csv_file:
    csvfile = csv.reader(csv_file, delimiter=',')
    all_value = []
    for row in csvfile:
        if (row[1] == 'bank_id'): continue
        # (ifsc,bank_id,branch,address,city,district,state,bank_name)
        banks.add((int(row[1]), row[7]))
        branches.add((row[0], int(row[1]), row[2], row[3], row[4], row[5], row[6]))

def create_tables():
    # Create sql table called bank
    cursor.execute("""CREATE TABLE IF NOT EXISTS bank (
        id int auto_increment not null primary key,
        name varchar(255) not null
    )
    """)

    # Create sql table called branch
    cursor.execute("""CREATE TABLE IF NOT EXISTS branch (
        id int auto_increment not null primary key,
        ifsc VARCHAR(255) not null,
        bank_id INT,
        branch VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci,
        address VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci,
        city VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci,
        district VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci,
        state VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci
    )
    """)

def create_banks(records, dryRun = False):
    for bank in records:
        if dryRun is True:
            print(bank)
            continue

        # Inserting data in bank_info table
        query = ("INSERT INTO bank (id, name) VALUES (%s,%s)")
        cursor.execute(query, tuple(bank))

def create_branches(records, dryRun = False):    
    for branch in records:
        if dryRun is True:
            print(branch)
            continue

        branches_query = ("INSERT INTO branch (ifsc, bank_id, branch, address, city, district, state) VALUES (%s, %s, %s, %s, %s, %s, %s)")
        cursor.execute(branches_query, tuple(branch))

dry = False
create_tables()
create_banks(banks, dry)
create_branches(branches, dry)

db.commit()