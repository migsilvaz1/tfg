from Persistence.Repositories import ImagenesRepository


def load_from_path(path):
    return ImagenesRepository.load_from_path(path)


def rebuild_imagen(data, path):
    return ImagenesRepository.rebuild_imagen(data, path)


def save_imagen(data, numhist):
    ImagenesRepository.save_imagen(data, numhist, 'imagenes_procedimiento')


def delete_imagen(identificator):
    ImagenesRepository.delete_imagen(identificator, 'imagenes_procedimiento')


def getall_imagenes():
    return ImagenesRepository.getall_imagenes('imagenes_procedimiento')


def get_imagen_by_id(identificator):
    return ImagenesRepository.get_imagen_by_id(identificator, 'imagenes_procedimiento')
