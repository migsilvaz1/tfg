from Persistence.DBCon import connection


def load_from_path(path):
    #path example C:\\Users\\admin\\Desktop\\Repositorio Documentos\\HORARIOS-SANTAYFERIA.pdf
    chunks = path.split('\\')
    nombre = chunks[len(chunks)-1]
    im = open(path, 'rb').read()
    image = im.encode('base64')
    return [nombre, image]


def rebuild_imagen(data, path):
    total_path = path + '\\copy of ' + data[0]
    imagen = data[1].decode('base64')
    fout = open(total_path, 'wb')
    fout.write(imagen)


def save_imagen(data, numhist, table):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    print(data[0], data[1])
    query = ("INSERT INTO " + table + " VALUES(NULL,'%s', '%s', '%d')" % (data[0], data[1], numhist))
    cursor.execute(query)
    cnx.commit()
    connection.dbdisconect(cnx)


def delete_imagen(identificator, table):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM " + table + " WHERE id_imagen = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    connection.dbdisconect(cnx)


def getall_imagenes(table):
    cnx = connection.dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT image_name, image FROM " + table)
    cursor.execute(query)
    connection.dbdisconect(cnx)
    for (image_name, image) in cursor:
        result.append([image_name, image])
    return result


def get_imagen_by_id(identificator, table):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT image_name, image FROM " + table + " WHERE id_imagen = '%d'" % identificator)
    cursor.execute(query)
    row = cursor.fetchone()
    connection.dbdisconect(cnx)
    return [row[0], row[1]]
