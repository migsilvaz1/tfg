__author__ = 'admin'
import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
from Persistence.Services import PacienteService
from Persistence.Domain.Paciente import Paciente


class App():

    def delete_event(self, widget, event, data=None):
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()
        return

    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file("gui - ejecutable.glade")

        window = builder.get_object("home")
        window.set_size_request(1024, 700)
        window.connect("delete_event", self.delete_event)
        window.connect("destroy", self.destroy)
        window.show()

        tree = builder.get_object("treeview9")
        model = gtk.TreeStore(str, str)

        cellnh = gtk.CellRendererText()
        col1 = gtk.TreeViewColumn("Numero Historial", cellnh)
        col1.add_attribute(cellnh, 'text', 0)

        celln = gtk.CellRendererText()
        col2 = gtk.TreeViewColumn("Nombre", celln)
        col2.add_attribute(celln, 'text', 1)
        tree.append_column(col1)
        tree.append_column(col2)

        tree.set_model(model)

        #p = Paciente(1, '28AS', 'Mr james', '2014-01-01', 'H', 'Ninguna enfermedad', 32, 32)
        #PacienteService.create(p)
        lista_pacientes = PacienteService.get_all()
        for elem in lista_pacientes:
            model.append(None, [elem.numerohistorial, elem.nombre])


if __name__ == "__main__":
    app = App()
    gtk.main()