from Persistence.Repositories import PruebaDiagnosticaRepository


def get_all():
    return PruebaDiagnosticaRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return PruebaDiagnosticaRepository.get_by_id(ide)
    else:
        raise TypeError("El dato debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return PruebaDiagnosticaRepository.get_by_name(name)
    else:
        raise TypeError("El dato debe ser str")


def create(pruebaDiagnostica):
    if pruebaDiagnostica.nombre == "" or not isinstance(pruebaDiagnostica.idradiologo, int):
        raise TypeError("La entidad tiene campos en blanco")
    PruebaDiagnosticaRepository.create(pruebaDiagnostica)


def update(pruebaDiagnostica):
    if pruebaDiagnostica.nombre == "" or not isinstance(pruebaDiagnostica.idradiologo, int) \
            or not isinstance(pruebaDiagnostica.id, int):
        raise TypeError("La entidad no esta bien construida")
    PruebaDiagnosticaRepository.update(pruebaDiagnostica)


def delete(pruebaDiagnostica):
    raise NotImplementedError("Esta opcion no se implementa")