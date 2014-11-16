from Persistence.Repositories import PruebaDiagnosticaRepository, RadiologoRepository


def get_all():
    return PruebaDiagnosticaRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return PruebaDiagnosticaRepository.get_by_id(ide)
    else:
        raise TypeError("El id debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return PruebaDiagnosticaRepository.get_by_name(name)
    else:
        raise TypeError("El nombre debe ser str")


def create(pruebaDiagnostica):
    if pruebaDiagnostica.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    return PruebaDiagnosticaRepository.create(pruebaDiagnostica)


def update(pruebaDiagnostica):
    if pruebaDiagnostica.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    if not isinstance(pruebaDiagnostica.id, int):
        raise TypeError("El id debe ser int")
    PruebaDiagnosticaRepository.update(pruebaDiagnostica)


def delete(pruebaDiagnostica):
    raise NotImplementedError("Esta opcion no se implementa")


def get_radiologo(pruebaDiagnostica):
    if not isinstance(pruebaDiagnostica.idradiologo, int):
        raise TypeError("La prueba no tiene radiologo asociado")
    return RadiologoRepository.get_by_id(pruebaDiagnostica.idradiologo)


def get_imagenes(pruebaDiagnostica):
    return