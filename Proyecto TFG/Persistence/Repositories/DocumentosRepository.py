from Persistence.DBCon import connection


def load_from_path(path):
    #path example C:\\Users\\admin\\Desktop\\Repositorio Documentos\\HORARIOS-SANTAYFERIA.pdf
    chunks = path.split('\\')
    nombre = chunks[len(chunks)-1]
    d = open(path, 'rb').read()
    doc = d.encode('base64')
    return [nombre, doc]


def rebuild_doc(data, path):
    total_path = path + '\\copy of ' + data[0]
    doc = data[1].decode('base64')
    fout = open(total_path, 'wb')
    fout.write(doc)


def save_doc(data, id_proc):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    print(data[0], data[1])
    query = ("INSERT INTO documentos_procedimiento VALUES(NULL,'%s', '%s', '%d')" % (data[0], data[1], id_proc))
    cursor.execute(query)
    cnx.commit()
    connection.dbdisconect(cnx)


def delete_doc(identificator):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("DELETE FROM documentos_procedimiento WHERE id_doc = '%d'" % identificator)
    cursor.execute(query)
    cnx.commit()
    connection.dbdisconect(cnx)


def get_all_doc():
    cnx = connection.dbconnect()
    result = []
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT doc_name, doc FROM documentos_procedimiento")
    cursor.execute(query)
    connection.dbdisconect(cnx)
    for (image_name, image) in cursor:
        result.append([image_name, image])
    return result


def get_doc_by_id(identificator):
    cnx = connection.dbconnect()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT doc_name, doc FROM documentos_procedimiento WHERE id_doc = '%d'" % identificator)
    cursor.execute(query)
    row = cursor.fetchone()
    connection.dbdisconect(cnx)
    return [row[0], row[1]]

