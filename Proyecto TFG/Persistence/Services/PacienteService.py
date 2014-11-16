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


def get_by_numerohistorial(numerohistorial):
    if isinstance(numerohistorial, str):
        return PacienteRepository.get_by_numerohistorial(numerohistorial)
    else:
        raise TypeError("El dato debe ser str")


def create(paciente):
    if paciente.nombre == "":
        raise TypeError("Nombre paciente erroneo")
    if paciente.numerohistorial == "":
        raise TypeError("Numero de historial paciente erroneo")
    if paciente.fechanacimiento == "":
        raise TypeError("fecha nacimiento paciente erroneo")
    if paciente.sexo == "":
        raise TypeError("sexo paciente erroneo")
    if paciente.enfermedadesconocidas == "":
        raise TypeError("enfermedades conocidas paciente erroneo")
    if not isinstance(paciente.edad, int):
        raise TypeError("edad paciente erroneo")
    if not isinstance(paciente.edadconsulta, int):
        raise TypeError("edad consulta")
    return PacienteRepository.create(paciente)


def update(paciente):
    if paciente.nombre == "" or paciente.numerohistorial == "" or paciente.fechanacimiento or paciente.sexo == "" \
            or paciente.enfermedadesconocidas == "" or not isinstance(paciente.edad, int) \
            or not isinstance(paciente.edadconsulta, int) or not isinstance(paciente.id, int):
        raise TypeError("La entidad no esta bien construida")
    PacienteRepository.update(paciente)


def delete(paciente):
    raise NotImplementedError("Esta opcion no se implementa")


def get_factores(paciente):
    if paciente.nombre == "" or paciente.numerohistorial == "" or paciente.fechanacimiento or paciente.sexo == "" \
            or paciente.enfermedadesconocidas == "" or not isinstance(paciente.edad, int) \
            or not isinstance(paciente.edadconsulta, int):
        raise TypeError("La entidad tiene campos en blanco")
    return PacienteRepository.get_factores(paciente)


def get_episodios(paciente):
    if paciente.nombre == "" or paciente.numerohistorial == "" or paciente.fechanacimiento or paciente.sexo == "" \
            or paciente.enfermedadesconocidas == "" or not isinstance(paciente.edad, int) \
            or not isinstance(paciente.edadconsulta, int):
        raise TypeError("La entidad tiene campos en blanco")
    return PacienteRepository.get_episodios(paciente)