__author__ = 'admin'
import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
from Persistence.Services import PacienteService
from Persistence.Domain.Paciente import Paciente


class App():
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file("gui - ejecutable.glade")
        builder.connect_signals({'button_save1': self.quit})
        window = builder.get_object("home")
        window.set_size_request(1024, 700)
        window.show()
        tree = builder.get_object("treeview9")
        model = gtk.TreeStore(str, str, str)
        cellp = gtk.CellRendererText()
        col1 = gtk.TreeViewColumn("Saludo", cellp)
        col1.add_attribute(cellp, 'background', 0)
        cellt = gtk.CellRendererText()
        col2 = gtk.TreeViewColumn("Despedida", cellt)
        col2.add_attribute(cellt, 'text', 1)
        tree.append_column(col1)
        tree.append_column(col2)
        tree.set_model(model)
        #p = Paciente(1, '28AS', 'Mr james', '2014-01-01', 'H', 'Ninguna enfermedad', 32, 32)
        #PacienteService.create(p)
        lista_pacientes = PacienteService.get_all()
        for elem in lista_pacientes:
            model.append(None, ['red', elem.nombre, "adios"])

    def quit(self):
        gtk.main_quit()


if __name__ == "__main__":
    app = App()
    gtk.main()