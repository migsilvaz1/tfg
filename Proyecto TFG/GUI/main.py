__author__ = 'admin'
import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
from Persistence.Services import PacienteService, ServicioService, PatologiaService
from Persistence.Domain.Paciente import Paciente


class App():

    def delete_event(self, widget, event, data=None):
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()
        return

    def guardar_home(self, event, widget, data):
        n = data[''].get_text()
        print(n)

    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file("gui - ejecutable.glade")

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
        lista_servicios_model = gtk.ListStore(str)
        for elem in servicios:
            lista_servicios_model.append([elem.nombre])
        cell = gtk.CellRendererText()
        lista_servicios.set_model(lista_servicios_model)
        lista_servicios.pack_start(cell)
        lista_servicios.set_attributes(cell, text=0)

        #La lista de patologias
        patologias = PatologiaService.get_all()
        lista_patologias = builder.get_object('patologiahome')
        lista_patologias_model = gtk.ListStore(str)
        for elem in patologias:
            lista_patologias_model.append([elem.nombre])
        cell = gtk.CellRendererText()
        lista_patologias.set_model(lista_patologias_model)
        lista_patologias.pack_start(cell)
        lista_patologias.set_attributes(cell, text=0)

        #Datos de entrada
        numero_historial = builder.get_object('nhistorialhome')
        nombre_paciente = builder.get_object('nombrepacientehome')
        fecha_nacimiento = builder.get_object('fechanacimientohome')
        nombre_episodio = builder.get_object('nombreepisodiohome')
        fecha_episodio = builder.get_object('fechaepisodiohome')
        nombre_procedimiento = builder.get_object('nombreprocedimientohome')
        data = {
            'numero_historial': numero_historial,
            'nombre_paciente': nombre_paciente,
            'fecha_nacimiento': fecha_nacimiento,
            'nombre_episodio': nombre_episodio,
            'fecha_episodio': fecha_episodio,
            'nombre_procedimiento': nombre_procedimiento
        }
        button_guardar = builder.get_object('guardarhome')
        button_guardar.connect("button_press_event", self.guardar_home, data)


if __name__ == "__main__":
    app = App()
    gtk.main()