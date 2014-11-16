from Persistence.Repositories import ServicioRepository


def get_all():
    return ServicioRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return ServicioRepository.get_by_id(ide)
    else:
        raise TypeError("El id debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return ServicioRepository.get_by_name(name)
    else:
        raise TypeError("El nombre debe ser str")


def create(servicio):
    if servicio.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    return ServicioRepository.create(servicio)


def update(servicio):
    if servicio.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    if not isinstance(servicio.id, int):
        raise TypeError("El id debe ser int")
    ServicioRepository.update(servicio)


def delete(servicio):
    raise NotImplementedError("Esta opcion no se implementa")