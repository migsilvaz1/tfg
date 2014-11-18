__author__ = 'admin'
import sys
import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
from Persistence.Services import PacienteService, ServicioService, PatologiaService, EpisodioService, ProcedimientoService, TipoProcedimientoService, RelationsService
from Persistence.Domain.Paciente import Paciente
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

    def hide_window(self, widget, event):
        window = widget.get_toplevel().get_toplevel().get_toplevel()
        window.hide()
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
            alert = self.builder.get_object("windowerror")
            alert.set_position(gtk.WIN_POS_CENTER)
            alert.show()
            self.builder.get_object("labelerror").set_text(str(sys.exc_info()[1]))
            button_aceptar = self.builder.get_object("buttonerror")
            button_aceptar.connect("button_press_event", self.hide_window)
        self.create_tree_pacientes()
        self.builder.get_object('nhistorialhome').set_text("")
        self.builder.get_object('nombrepacientehome').set_text("")
        self.builder.get_object('fechanacimientohome').set_text("")
        self.builder.get_object('nombreepisodiohome').set_text("")
        self.builder.get_object('fechaepisodiohome').set_text("")
        self.lista_servicios.set_active(-1)
        self.lista_patologias.set_active(-1)
        self.lista_tprocedimientos.set_active(-1)
        return

    def changed_cb_servicio(self, combobox):
        global combo_value_servicio_id
        index = combobox.get_active()
        model = combobox.get_model()
        combo_value_servicio_id = model[index][0]
        return

    def changed_cb_patologia(self, combobox):
        global combo_value_patologia_id
        index = combobox.get_active()
        model = combobox.get_model()
        combo_value_patologia_id = model[index][0]
        return

    def changed_cb_tipoprocedimiento(self, combobox):
        global combo_value_tipoprocedimiento_id
        index = combobox.get_active()
        model = combobox.get_model()
        combo_value_tipoprocedimiento_id = model[index][0]
        return

    def create_tree_pacientes(self):
        self.tree_model.clear()
        lista_pacientes = PacienteService.get_all()
        for elem in lista_pacientes:
            self.tree_model.append(None, [elem.numerohistorial, elem.nombre])
        return

    def datos_paciente(self, widget, event, data):
        self.window.hide()
        window = self.builder.get_object("datospaciente")
        window.set_size_request(1024, 700)
        window.connect("delete_event", self.delete_event)
        window.connect("destroy", self.destroy)
        window.show()
        tree = self.builder.get_object("treeview12")
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
        tree.connect("row-activated", self.update_datos_paciente(tree.get_selection()))
        #sacar los datos del paciente seleccionado
        print(self.tree.get_selection())
        return

    def update_datos_paciente(self, selection):
        #sacar los datos del paciente seleccionado
        print(self.tree.get_selection())
        return

    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("gui - ejecutable.glade")
        self.window = self.builder.get_object("home")
        self.window.set_size_request(1024, 700)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.show()
        #Rellendando la vista
        #el tree de los pacientes
        self.tree = self.builder.get_object("treeview9")
        self.tree_model = gtk.TreeStore(str, str)
        cellnh = gtk.CellRendererText()
        col1 = gtk.TreeViewColumn("Numero Historial", cellnh)
        col1.add_attribute(cellnh, 'text', 0)
        celln = gtk.CellRendererText()
        col2 = gtk.TreeViewColumn("Nombre", celln)
        col2.add_attribute(celln, 'text', 1)
        self.tree.append_column(col1)
        self.tree.append_column(col2)
        self.tree.set_model(self.tree_model)
        self.create_tree_pacientes()

        #La lista de servicios
        servicios = ServicioService.get_all()
        self.lista_servicios = self.builder.get_object('serviciohome')
        self.lista_servicios_model = gtk.ListStore(int, str)
        for elem in servicios:
            self.lista_servicios_model.append([elem.id, elem.nombre])
        cell = gtk.CellRendererText()
        self.lista_servicios.set_model(self.lista_servicios_model)
        self.lista_servicios.pack_start(cell)
        self.lista_servicios.set_attributes(cell, text=1)
        self.lista_servicios.connect('changed', self.changed_cb_servicio)

        #La lista de patologias
        patologias = PatologiaService.get_all()
        self.lista_patologias = self.builder.get_object('patologiahome')
        self.lista_patologias_model = gtk.ListStore(int, str)
        for elem in patologias:
            self.lista_patologias_model.append([elem.id, elem.nombre])
        cell = gtk.CellRendererText()
        self.lista_patologias.set_model(self.lista_patologias_model)
        self.lista_patologias.pack_start(cell)
        self.lista_patologias.set_attributes(cell, text=1)
        self.lista_patologias.connect('changed', self.changed_cb_patologia)

        #La lista de tiposprocedimientos
        tprocedimientos = TipoProcedimientoService.get_all()
        self.lista_tprocedimientos = self.builder.get_object('tipoprocedimientohome')
        self.lista_tprocedimientos_model = gtk.ListStore(int, str)
        for elem in tprocedimientos:
            self.lista_tprocedimientos_model.append([elem.id, elem.nombre])
        cell = gtk.CellRendererText()
        self.lista_tprocedimientos.set_model(self.lista_tprocedimientos_model)
        self.lista_tprocedimientos.pack_start(cell)
        self.lista_tprocedimientos.set_attributes(cell, text=1)
        self.lista_tprocedimientos.connect('changed', self.changed_cb_tipoprocedimiento)

        #Datos de entrada
        numero_historial = self.builder.get_object('nhistorialhome')
        nombre_paciente = self.builder.get_object('nombrepacientehome')
        fecha_nacimiento = self.builder.get_object('fechanacimientohome')
        nombre_episodio = self.builder.get_object('nombreepisodiohome')
        fecha_episodio = self.builder.get_object('fechaepisodiohome')
        data = {
            'numero_historial': numero_historial,
            'nombre_paciente': nombre_paciente,
            'fecha_nacimiento': fecha_nacimiento,
            'nombre_episodio': nombre_episodio,
            'fecha_episodio': fecha_episodio
        }
        button_guardar = self.builder.get_object('guardarhome')
        button_guardar.connect("button_press_event", self.guardar_home, data)
        self.tree.connect("row-activated", self.datos_paciente)


if __name__ == "__main__":
    app = App()
    gtk.main()