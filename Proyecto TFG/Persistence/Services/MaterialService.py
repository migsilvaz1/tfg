from Persistence.Repositories import MaterialRepository


def get_all():
    return MaterialRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return MaterialRepository.get_by_id(ide)
    else:
        raise TypeError("El id debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return MaterialRepository.get_by_name(name)
    else:
        raise TypeError("El nombre debe ser str")


def create(material):
    if material.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    MaterialRepository.create(material)


def update(material):
    if material.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    if not isinstance(material.id, int):
        raise TypeError("El id debe ser int")
    MaterialRepository.update(material)


def delete(material):
    raise NotImplementedError("Esta opcion no se implementa")
