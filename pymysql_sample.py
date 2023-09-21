import csv
import pymysql

# MySQL connection parameters
host = 'localhost'
user = 'your_username'
password = 'your_password'
database = 'your_database_name'

# CSV file path
csv_file = 'your_csv_file.csv'

# Establish a MySQL connection
connection = pymysql.connect(host=host, user=user, password=password, database=database)
cursor = connection.cursor()

# Define the SQL INSERT statement
insert_query = f"INSERT INTO your_table_name (column1_name, column2_name, ...) VALUES (%s, %s, ...)"

# Read and insert records from the CSV file
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row if present
    records_to_insert = [row for row in csv_reader]

try:
    cursor.executemany(insert_query, records_to_insert)
    connection.commit()
    print("Records inserted successfully.")
except pymysql.Error as e:
    connection.rollback()
    print(f"Error: {e}")
finally:
    connection.close()
