from Persistence.Repositories import EvolucionRepository


def get_all():
    return EvolucionRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return EvolucionRepository.get_by_id(ide)
    else:
        raise TypeError("El id debe ser int")


def create(evolucion):
    if evolucion.resultado == "":
        raise TypeError("El resultado no puede estar en blanco")
    EvolucionRepository.create(evolucion)


def update(evolucion):
    if evolucion.resultado == "":
        raise TypeError("El resultado no puede estar en blanco")
    if not isinstance(evolucion.id, int):
        raise TypeError("El id debe ser int")
    EvolucionRepository.update(evolucion)


def delete(evolucion):
    raise NotImplementedError("Esta opcion no se implementa")