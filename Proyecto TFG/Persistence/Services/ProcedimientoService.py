from Persistence.Repositories import ProcedimientoRepository, EvolucionRepository, TipoProcedimientoRepository


def get_all():
    return ProcedimientoRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return ProcedimientoRepository.get_by_id(ide)
    else:
        raise TypeError("El id debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return ProcedimientoRepository.get_by_name(name)
    else:
        raise TypeError("El nombre debe ser str")


def create(procedimiento):
    if procedimiento.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    if not isinstance(procedimiento.id, int):
        raise TypeError("El id debe ser int")
    ProcedimientoRepository.create(procedimiento)


def update(procedimiento):
    if procedimiento.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    if not isinstance(procedimiento.id, int):
        raise TypeError("El id debe ser int")
    ProcedimientoRepository.update(procedimiento)


def delete(procedimiento):
    raise NotImplementedError("Esta opcion no se implementa")


def get_evolucion(procedimiento):
    if not isinstance(procedimiento.idevolucion, int):
        raise TypeError("El procedimiento no tiene evolucion asociada")
    return EvolucionRepository.get_by_id(procedimiento.idevolucion)


def get_tipoprocedimiento(procedimiento):
    if not isinstance(procedimiento.idtipop, int):
        raise TypeError("El procedimiento no tiene procedimiento tipo asociado")
    return TipoProcedimientoRepository.get_by_id(procedimiento.idtipop)


def get_episodios(procedimiento):
    if procedimiento.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    if not isinstance(procedimiento.id, int):
        raise TypeError("El id debe ser int")
    return ProcedimientoRepository.get_episodios(procedimiento)


def get_imagenes(procedimiento):
    if procedimiento.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    if not isinstance(procedimiento.id, int):
        raise TypeError("El id debe ser int")
    return ProcedimientoRepository.get_imagenes(procedimiento)


def get_documentos(procedimiento):
    if procedimiento.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    if not isinstance(procedimiento.id, int):
        raise TypeError("El id debe ser int")
    return ProcedimientoRepository.get_documentos(procedimiento)


def get_materiales(procedimiento):
    if procedimiento.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    if not isinstance(procedimiento.id, int):
        raise TypeError("El id debe ser int")
    return ProcedimientoRepository.get_materiales(procedimiento)


def get_complicaciones(procedimiento):
    if procedimiento.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    if not isinstance(procedimiento.id, int):
        raise TypeError("El id debe ser int")
    return ProcedimientoRepository.get_complicaciones(procedimiento)