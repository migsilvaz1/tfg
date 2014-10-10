from Persistence.Repositories import BlobRepository


def load_from_path(path):
    return BlobRepository.load_from_path(path)


def rebuild_imagen(data, path):
    return BlobRepository.rebuild_imagen(data, path)


def save_imagen(data, numhist):
    BlobRepository.save_imagen(data, numhist, 'imagenes_patologia')


def delete_imagen(identificator):
    BlobRepository.delete_imagen(identificator, 'imagenes_patologia')


def getall_imagenes():
    return BlobRepository.getall_imagenes('imagenes_patologia')


def get_imagen_by_id(identificator):
    return BlobRepository.get_imagen_by_id(identificator, 'imagenes_patologia')
