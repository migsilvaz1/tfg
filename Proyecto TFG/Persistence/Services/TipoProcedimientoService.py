from Persistence.Repositories import TipoProcedimientoRepository


def get_all():
    return TipoProcedimientoRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return TipoProcedimientoRepository.get_by_id(ide)
    else:
        raise TypeError("El id debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return TipoProcedimientoRepository.get_by_name(name)
    else:
        raise TypeError("El nombre debe ser str")


def create(Tipop):
    if Tipop.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    TipoProcedimientoRepository.create(Tipop)


def update(Tipop):
    if Tipop.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    if not isinstance(Tipop.id, int):
        raise TypeError("El id debe ser int")
    TipoProcedimientoRepository.update(Tipop)


def delete(Tipop):
    raise NotImplementedError("Esta opcion no se implementa")
