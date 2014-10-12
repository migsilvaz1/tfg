from Persistence.Repositories import MaterialRepository


def get_all():
    return MaterialRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return MaterialRepository.get_by_id(ide)
    else:
        raise TypeError("El dato debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return MaterialRepository.get_by_name(name)
    else:
        raise TypeError("El dato debe ser str")


def create(material):
    if material.nombre == "":
        raise TypeError("La entidad tiene campos en blanco")
    MaterialRepository.create(material)


def update(material):
    if material.nombre == "" or not isinstance(material.id, int):
        raise TypeError("La entidad no esta bien construida")
    MaterialRepository.update(material)


def delete(material):
    raise NotImplementedError("Esta opcion no se implementa")
