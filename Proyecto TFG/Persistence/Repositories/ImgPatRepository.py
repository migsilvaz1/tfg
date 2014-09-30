from Persistence.Repositories import ImagenesRepository


def load_from_path(path):
    return ImagenesRepository.load_from_path(path)


def rebuild_imagen(data, path):
    return ImagenesRepository.rebuild_imagen(data, path)


def save_imagen(data, numhist):
    ImagenesRepository.save_imagen(data, numhist, 'imagenes_patologia')


def delete_imagen(identificator):
    ImagenesRepository.delete_imagen(identificator, 'imagenes_patologia')


def getall_imagenes():
    return ImagenesRepository.getall_imagenes('imagenes_patologia')


def get_imagen_by_id(identificator):
    return ImagenesRepository.get_imagen_by_id(identificator, 'imagenes_patologia')
