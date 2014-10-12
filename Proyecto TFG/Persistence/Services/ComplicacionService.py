from Persistence.Repositories import ComplicacionRepository


def get_all():
    return ComplicacionRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return ComplicacionRepository.get_by_id(ide)
    else:
        raise TypeError("El dato debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return ComplicacionRepository.get_by_name(name)
    else:
        raise TypeError("El dato debe ser str")


def create(complicacion):
    if complicacion.nombre == "" or complicacion.mortalidadtemprana == "" or complicacion.mortalidadtardia == "":
        raise TypeError("La entidad tiene campos en blanco")
    ComplicacionRepository.create(complicacion)


def update(complicacion):
    if complicacion.nombre == "" or complicacion.mortalidadtemprana == "" or complicacion.mortalidadtardia == ""\
            or not isinstance(complicacion.id, int):
        raise TypeError("La entidad no esta bien construida")
    ComplicacionRepository.update(complicacion)


def delete(complicacion):
    raise NotImplementedError("Esta opcion no se implementa")