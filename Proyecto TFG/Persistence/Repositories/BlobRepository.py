from Persistence.DBCon import connection


def load_from_path(path):
    #path example C:\\Users\\admin\\Desktop\\Repositorio Documentos\\HORARIOS-SANTAYFERIA.pdf
    chunks = path.split('\\')
    nombre = chunks[len(chunks)-1]
    b = open(path, 'rb').read()
    blob = b.encode('base64')
    return [nombre, blob]


def rebuild_blob(data, path):
    total_path = path + '\\copy of ' + data[0]
    blob = data[1].decode('base64')
    fout = open(total_path, 'wb')
    fout.write(blob)


def save_blob(data, table, referenced):
    fk = referenced.id
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    print(data[0], data[1])
    query = ("INSERT INTO " + table + " VALUES(NULL,'%s', '%s', '%d')" % (data[0], data[1], fk))
    cursor.execute(query)
    cnx.commit()
    connection.dbdisconect(cnx)


def delete_imagen(identificator, table, blob_type):
    if blob_type == "doc":
        pk = 'id_doc'
    elif blob_type == "image":
        pk = 'id_image'
    else:
        raise TypeError('Not supported BLOB type')
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM " + table + " WHERE " + pk + " = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    connection.dbdisconect(cnx)


def getall_blob_from_entity(foreignkey, entity, table, blob_type):
    if blob_type == "doc":
        first = 'doc_name, doc'
    elif blob_type == "image":
        first = 'image_name, image'
    else:
        raise TypeError('Not supported BLOB type')
    cnx = connection.dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT " + first + " FROM " + table + "WHERE " + foreignkey + " = '%d'" % entity.id)
    cursor.execute(query)
    connection.dbdisconect(cnx)
    for (name, blob) in cursor:
        result.append([name, blob])
    return result


def get_blob_by_id(ide, table, blob_type):
    if blob_type == "doc":
        first = 'doc_name, doc'
        pk = 'id_doc'
    elif blob_type == "image":
        first = 'image_name, image'
        pk = 'id_image'
    else:
        raise TypeError('Not supported BLOB type')
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT " + first + " FROM " + table + " WHERE " + pk + " = '%d'" % ide)
    cursor.execute(query)
    row = cursor.fetchone()
    connection.dbdisconect(cnx)
    return [row[0], row[1]]
