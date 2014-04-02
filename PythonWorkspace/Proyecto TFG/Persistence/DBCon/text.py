from Persistence.DBCon import connection


con = connection.dbconnect()
print(con)
dcon = connection.dbdisconect(con)
print(dcon)


