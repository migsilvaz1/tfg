from Persistence.Repositories import RelationsRepository
from Persistence.Domain import Material, Procedimiento, Episodio, Complicacion, PruebaDiagnostica


def add_material_to_procedimiento(procedimiento, material):
    RelationsRepository.delete_procedimiento_mataterial(procedimiento, material)


def remove_material_from_procedimiento(procedimiento, material):
    RelationsRepository.delete_procedimiento_mataterial(procedimiento, material)


def add_procedimiento_to_episodio(episodio, procedimiento):
    RelationsRepository.create_episodio_procedimiento(episodio, procedimiento)


def remove_procedimiento_from_episodio(episodio, procedimiento):
    RelationsRepository.delete_episodio_procedimiento(episodio, procedimiento)


def add_complicacion_to_procedimiento(complicacion, procedimiento):
    RelationsRepository.create_complicacion_procedimiento(complicacion, procedimiento)


def remove_complicacion_from_procedimiento(complicacion, procedimiento):
    RelationsRepository.delete_complicacion_procedimiento(complicacion, procedimiento)


def add_pdiagnostica_to_episodio(episodio, pdiagnostica):
    RelationsRepository.create_episodio_pdiagnostica(episodio, pdiagnostica)


def remove_pdiagnostica_to_episodio(episodio, pdiagnostica):
    RelationsRepository.delete_episodio_procedimiento(episodio, pdiagnostica)