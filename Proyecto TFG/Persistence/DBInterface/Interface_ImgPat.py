from Persistence.DBInterface import Interface_Imagenes


def load_from_path(path):
    return Interface_Imagenes.load_from_path(path)


def rebuild_imagen(data, path):
    return Interface_Imagenes.rebuild_imagen(data, path)


def save_imagen(data, numhist):
    Interface_Imagenes.save_imagen(data, numhist, 'imagenes_patologia')


def delete_imagen(identificator):
    Interface_Imagenes.delete_imagen(identificator, 'imagenes_patologia')


def getall_imagenes():
    return Interface_Imagenes.getall_imagenes('imagenes_patologia')


def get_imagen_by_id(identificator):
    return Interface_Imagenes.get_imagen_by_id(identificator, 'imagenes_patologia')
