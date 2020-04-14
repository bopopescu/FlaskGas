import mysql.connector as mariadb

mariadb_connection = mariadb.connect(
    user='root',
    password='piotr',
    database='db1')
cursor = mariadb_connection.cursor()
imie = ''
cursor.execute("SELECT name FROM test LIMIT 1")

print(cursor.execute)
print('eny')
def szs():
    print('gg')
print('gg') 