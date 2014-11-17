__author__ = 'admin'
import sys
import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
from Persistence.Services import PacienteService, ServicioService, PatologiaService, EpisodioService, ProcedimientoService, TipoProcedimientoService, RelationsService
from Persistence.Domain.Paciente import Paciente
from Persistence.Domain.Servicio import Servicio
from Persistence.Domain.Patologia import Patologia
from Persistence.Domain.Episodio import Episodio
from Persistence.Domain.Procedimiento import Procedimiento

combo_value_servicio_id = -1
combo_value_patologia_id = -1
combo_value_tipoprocedimiento_id = -1


class App():

    def delete_event(self, widget, event, data=None):
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()
        return

    def guardar_home(self, event, widget, data):
        numero_historial = data['numero_historial'].get_text()
        nombre_paciente = data['nombre_paciente'].get_text()
        fecha_nacimiento = data['fecha_nacimiento'].get_text()
        nombre_episodio = data['nombre_episodio'].get_text()
        fecha_episodio = data['fecha_episodio'].get_text()
        try:
            paciente = Paciente(1, numero_historial, nombre_paciente, fecha_nacimiento, "N", "", 0, 0)
            id_paciente = PacienteService.create(paciente)
            episodio = Episodio(1, nombre_episodio, fecha_episodio, int(id_paciente), int(combo_value_servicio_id), 1, int(combo_value_patologia_id))
            id_episodio = EpisodioService.create(episodio)
            procedimiento = Procedimiento(1, int(combo_value_tipoprocedimiento_id), 1)
            id_procedimiento = ProcedimientoService.create(procedimiento)
            RelationsService.add_procedimiento_to_episodio(int(id_episodio), int(id_procedimiento))
        except TypeError:
            builder = gtk.Builder()
            builder.add_from_file("gui - ejecutable.glade")
            window = builder.get_object("exportarbd")
            window.show()
            builder.get_object("label2").set_text(str(sys.exc_info()[1]))

    def changed_cb_servicio(self, combobox):
        global combo_value_servicio_id
        index = combobox.get_active()
        model = combobox.get_model()
        combo_value_servicio_id = model[index][0]

    def changed_cb_patologia(self, combobox):
        global combo_value_patologia_id
        index = combobox.get_active()
        model = combobox.get_model()
        combo_value_patologia_id = model[index][0]

    def changed_cb_tipoprocedimiento(self, combobox):
        global combo_value_tipoprocedimiento_id
        index = combobox.get_active()
        model = combobox.get_model()
        combo_value_tipoprocedimiento_id = model[index][0]

    def show_init(self, builder):
        window = builder.get_object("home")
        window.set_size_request(1024, 700)
        window.connect("delete_event", self.delete_event)
        window.connect("destroy", self.destroy)
        window.show()
        #Rellendando la bista
        #el tree de los pacientes
        tree = builder.get_object("treeview9")
        tree_model = gtk.TreeStore(str, str)
        cellnh = gtk.CellRendererText()
        col1 = gtk.TreeViewColumn("Numero Historial", cellnh)
        col1.add_attribute(cellnh, 'text', 0)
        celln = gtk.CellRendererText()
        col2 = gtk.TreeViewColumn("Nombre", celln)
        col2.add_attribute(celln, 'text', 1)
        tree.append_column(col1)
        tree.append_column(col2)
        tree.set_model(tree_model)

        lista_pacientes = PacienteService.get_all()
        for elem in lista_pacientes:
            tree_model.append(None, [elem.numerohistorial, elem.nombre])

        #La lista de servicios
        servicios = ServicioService.get_all()
        lista_servicios = builder.get_object('serviciohome')
        lista_servicios_model = gtk.ListStore(int, str)
        for elem in servicios:
            lista_servicios_model.append([elem.id, elem.nombre])
        cell = gtk.CellRendererText()
        lista_servicios.set_model(lista_servicios_model)
        lista_servicios.pack_start(cell)
        lista_servicios.set_attributes(cell, text=1)
        lista_servicios.connect('changed', self.changed_cb_servicio)

        #La lista de patologias
        patologias = PatologiaService.get_all()
        lista_patologias = builder.get_object('patologiahome')
        lista_patologias_model = gtk.ListStore(int, str)
        for elem in patologias:
            lista_patologias_model.append([elem.id, elem.nombre])
        cell = gtk.CellRendererText()
        lista_patologias.set_model(lista_patologias_model)
        lista_patologias.pack_start(cell)
        lista_patologias.set_attributes(cell, text=1)
        lista_patologias.connect('changed', self.changed_cb_patologia)

        #La lista de tiposprocedimientos
        tprocedimientos = TipoProcedimientoService.get_all()
        lista_tprocedimientos = builder.get_object('tipoprocedimientohome')
        lista_tprocedimientos_model = gtk.ListStore(int, str)
        for elem in tprocedimientos:
            lista_tprocedimientos_model.append([elem.id, elem.nombre])
        cell = gtk.CellRendererText()
        lista_tprocedimientos.set_model(lista_tprocedimientos_model)
        lista_tprocedimientos.pack_start(cell)
        lista_tprocedimientos.set_attributes(cell, text=1)
        lista_tprocedimientos.connect('changed', self.changed_cb_tipoprocedimiento)

        #Datos de entrada
        numero_historial = builder.get_object('nhistorialhome')
        nombre_paciente = builder.get_object('nombrepacientehome')
        fecha_nacimiento = builder.get_object('fechanacimientohome')
        nombre_episodio = builder.get_object('nombreepisodiohome')
        fecha_episodio = builder.get_object('fechaepisodiohome')
        data = {
            'numero_historial': numero_historial,
            'nombre_paciente': nombre_paciente,
            'fecha_nacimiento': fecha_nacimiento,
            'nombre_episodio': nombre_episodio,
            'fecha_episodio': fecha_episodio
        }
        button_guardar = builder.get_object('guardarhome')
        button_guardar.connect("button_press_event", self.guardar_home, data)

    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file("gui - ejecutable.glade")
        self.show_init(builder)


if __name__ == "__main__":
    app = App()
    gtk.main()