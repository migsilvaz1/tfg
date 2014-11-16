from Persistence.Repositories import ComplicacionRepository


def get_all():
    return ComplicacionRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return ComplicacionRepository.get_by_id(ide)
    else:
        raise TypeError("La id debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return ComplicacionRepository.get_by_name(name)
    else:
        raise TypeError("El nombre debe ser str")


def create(complicacion):
    if complicacion.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    if complicacion.mortalidadtemprana == "":
        raise TypeError("La mortalidad temprana no puede estar en blanco")
    if complicacion.mortalidadtardia == "":
        raise TypeError("La mortalidad tardia no puede estar en blanco")
    return ComplicacionRepository.create(complicacion)


def update(complicacion):
    if not isinstance(complicacion.id, int):
        raise TypeError("La id debe ser int")
    if complicacion.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    if complicacion.mortalidadtemprana == "":
        raise TypeError("La mortalidad temprana no puede estar en blanco")
    if complicacion.mortalidadtardia == "":
        raise TypeError("La mortalidad tardia no puede estar en blanco")
    ComplicacionRepository.update(complicacion)


def delete(complicacion):
    raise NotImplementedError("Esta opcion no se implementa")