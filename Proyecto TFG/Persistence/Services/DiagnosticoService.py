from Persistence.Repositories import DiagnosticoRepository


def get_all():
    return DiagnosticoRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return DiagnosticoRepository.get_by_id(ide)
    else:
        raise TypeError("El id debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return DiagnosticoRepository.get_by_name(name)
    else:
        raise TypeError("El nombre debe ser str")


def create(diagnostico):
    if diagnostico.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    if not isinstance(diagnostico.idepisodio, int):
        raise TypeError("Debe tener una id de episoido valida")
    DiagnosticoRepository.create(diagnostico)


def update(diagnostico):
    if isinstance(diagnostico.id, int):
        raise TypeError("El id debe ser int")
    if diagnostico.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    if not isinstance(diagnostico.idepisodio, int):
        raise TypeError("Debe tener una id de episoido valida")
    DiagnosticoRepository.update(diagnostico)


def delete(diagnostico):
    raise NotImplementedError("Esta opcion no se implementa")
