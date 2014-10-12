from Persistence.Repositories import CentroRepository


def get_all():
    return CentroRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return CentroRepository.get_by_id(ide)
    else:
        raise TypeError("El dato debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return CentroRepository.get_by_name(name)
    else:
        raise TypeError("El dato debe ser str")


def create(centro):
    if centro.nombre == "":
        raise TypeError("La entidad tiene campos en blanco")
    CentroRepository.create(centro)


def update(centro):
    if centro.nombre == "" or not isinstance(centro.id, int):
        raise TypeError("La entidad no esta bien construida")
    CentroRepository.update(centro)


def delete(centro):
    raise NotImplementedError("Esta opcion no se implementa")