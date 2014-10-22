from Persistence.Repositories import TipoProcedimientoRepository


def get_all():
    return TipoProcedimientoRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return TipoProcedimientoRepository.get_by_id(ide)
    else:
        raise TypeError("El dato debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return TipoProcedimientoRepository.get_by_name(name)
    else:
        raise TypeError("El dato debe ser str")


def create(Tipop):
    if Tipop.nombre == "":
        raise TypeError("La entidad tiene campos en blanco")
    TipoProcedimientoRepository.create(centro)


def update(Tipop):
    if Tipop.nombre == "" or not isinstance(Tipop.id, int):
        raise TypeError("La entidad no esta bien construida")
    TipoProcedimientoRepository.update(Tipop)


def delete(Tipop):
    raise NotImplementedError("Esta opcion no se implementa")
