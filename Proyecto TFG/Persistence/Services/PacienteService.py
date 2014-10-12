from Persistence.Repositories import PacienteRepository


def get_all():
    return PacienteRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return PacienteRepository.get_by_id(ide)
    else:
        raise TypeError("El dato debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return PacienteRepository.get_by_name(name)
    else:
        raise TypeError("El dato debe ser str")


def get_by_numeroHistorial(numeroHistorial):
    if isinstance(numeroHistorial, str):
        return PacienteRepository.get_by_numeroHistorial(numeroHistorial)
    else:
        raise TypeError("El dato debe ser str")


def create(paciente):
    if paciente.nombre == "" or paciente.numerohistorial == "" or paciente.fechanacimiento or paciente.sexo == "" \
            or paciente.enfermedadesconocidas == "" or not isinstance(paciente.edad, int) \
            or not isinstance(paciente.edadconsulta, int):
        raise TypeError("La entidad tiene campos en blanco")
    PacienteRepository.create(paciente)


def update(paciente):
    if paciente.nombre == "" or paciente.numerohistorial == "" or paciente.fechanacimiento or paciente.sexo == "" \
            or paciente.enfermedadesconocidas == "" or not isinstance(paciente.edad, int) \
            or not isinstance(paciente.edadconsulta, int) or not isinstance(paciente.id, int):
        raise TypeError("La entidad no esta bien construida")
    PacienteRepository.update(paciente)


def delete(paciente):
    raise NotImplementedError("Esta opcion no se implementa")
