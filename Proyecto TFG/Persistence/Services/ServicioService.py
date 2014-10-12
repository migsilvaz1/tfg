from Persistence.Repositories import ServicioRepository


def get_all():
    return ServicioRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return ServicioRepository.get_by_id(ide)
    else:
        raise TypeError("El dato debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return ServicioRepository.get_by_name(name)
    else:
        raise TypeError("El dato debe ser str")


def create(servicio):
    if servicio.nombre == "":
        raise TypeError("La entidad tiene campos en blanco")
    ServicioRepository.create(servicio)


def update(servicio):
    if servicio.nombre == "" or not isinstance(servicio.id, int):
        raise TypeError("La entidad no esta bien construida")
    ServicioRepository.update(servicio)


def delete(servicio):
    raise NotImplementedError("Esta opcion no se implementa")