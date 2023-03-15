import pyodbc

server = '<server_name>'
database = '<database_name>'
username = '<username>'
password = '<password>'

conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = conn.cursor()

# execute a query
cursor.execute('SELECT * FROM <table_name>')

# fetch the results
results = cursor.fetchall()

# print the results
for row in results:
    print(row)

# close the connection
conn.close()
