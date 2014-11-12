from Persistence.Repositories import ProcedimientoRepository, EvolucionRepository, TipoProcedimientoRepository


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
    if procedimiento.nombre == "" or not isinstance(procedimiento.id, int):
        raise TypeError("La entidad tiene campos en blanco")
    ProcedimientoRepository.create(procedimiento)


def update(procedimiento):
    if procedimiento.nombre == "" or not isinstance(procedimiento.idevolucion, int) or not isinstance(procedimiento.id, int):
        raise TypeError("La entidad no esta bien construida")
    ProcedimientoRepository.update(procedimiento)


def delete(procedimiento):
    raise NotImplementedError("Esta opcion no se implementa")


def get_evolucion(procedimiento):
    if procedimiento.nombre == "" or not isinstance(procedimiento.id, int):
        raise TypeError("La entidad tiene campos en blanco")
    return EvolucionRepository.get_by_id(procedimiento.idevolucion)


def get_tipoprocedimiento(procedimiento):
    if procedimiento.nombre == "" or not isinstance(procedimiento.id, int):
        raise TypeError("La entidad tiene campos en blanco")
    return TipoProcedimientoRepository.get_by_id(procedimiento.idtipop)


def get_episodios(procedimiento):
    if procedimiento.nombre == "" or not isinstance(procedimiento.id, int):
        raise TypeError("La entidad tiene campos en blanco")
    return ProcedimientoRepository.get_episodios(procedimiento)


def get_imagenes(procedimiento):
    if procedimiento.nombre == "" or not isinstance(procedimiento.id, int):
        raise TypeError("La entidad tiene campos en blanco")
    return ProcedimientoRepository.get_imagenes(procedimiento)


def get_documentos(procedimiento):
    if procedimiento.nombre == "" or not isinstance(procedimiento.id, int):
        raise TypeError("La entidad tiene campos en blanco")
    return ProcedimientoRepository.get_documentos(procedimiento)


def get_materiales(procedimiento):
    if procedimiento.nombre == "" or not isinstance(procedimiento.id, int):
        raise TypeError("La entidad tiene campos en blanco")
    return ProcedimientoRepository.get_materiales(procedimiento)


def get_complicaciones(procedimiento):
    if procedimiento.nombre == "" or not isinstance(procedimiento.id, int):
        raise TypeError("La entidad tiene campos en blanco")
    return ProcedimientoRepository.get_complicaciones(procedimiento)