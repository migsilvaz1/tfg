from Persistence.Repositories import ProcedimientoRepository


def get_all():
    return ProcedimientoRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return ProcedimientoRepository.get_by_id(ide)
    else:
        raise TypeError("El dato debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return ProcedimientoRepository.get_by_name(name)
    else:
        raise TypeError("El dato debe ser str")


def create(procedimiento):
    if procedimiento.nombre == "" or not isinstance(procedimiento.idevolucion, int):
        raise TypeError("La entidad tiene campos en blanco")
    ProcedimientoRepository.create(procedimiento)


def update(procedimiento):
    if procedimiento.nombre == "" or not isinstance(procedimiento.idevolucion, int) or not isinstance(procedimiento.id, int):
        raise TypeError("La entidad no esta bien construida")
    ProcedimientoRepository.update(procedimiento)


def delete(procedimiento):
    raise NotImplementedError("Esta opcion no se implementa")