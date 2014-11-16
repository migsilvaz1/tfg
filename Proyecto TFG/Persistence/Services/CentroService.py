from Persistence.Repositories import CentroRepository


def get_all():
    return CentroRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return CentroRepository.get_by_id(ide)
    else:
        raise TypeError("La id debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return CentroRepository.get_by_name(name)
    else:
        raise TypeError("El nombre debe ser str")


def create(centro):
    if centro.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    CentroRepository.create(centro)


def update(centro):
    if centro.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    if not isinstance(centro.id, int):
        raise TypeError("La id debe ser int")
    CentroRepository.update(centro)


def delete(centro):
    raise NotImplementedError("Esta opcion no se implementa")