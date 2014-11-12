import connection
con = connection.dbconnect()
print(con)
connection.dbdisconect(con)
