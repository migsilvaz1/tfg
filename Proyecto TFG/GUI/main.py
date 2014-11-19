__author__ = 'admin'
import sys
import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
from Persistence.Services import PacienteService, ServicioService, PatologiaService, EpisodioService, \
    ProcedimientoService, TipoProcedimientoService, RelationsService, CentroService, ComplicacionService, \
    DiagnosticoService, EvolucionService, FactorService, MaterialService, PruebaDiagnosticaService, RadiologoService
from Persistence.Domain.Paciente import Paciente
from Persistence.Domain.Episodio import Episodio
from Persistence.Domain.Procedimiento import Procedimiento
from Persistence.Domain.Centro import Centro
from Persistence.Domain.Complicacion import Complicacion
from Persistence.Domain.Diagnostico import Diagnostico
from Persistence.Domain.Evolucion import Evolucion
from Persistence.Domain.Factor import Factor
from Persistence.Domain.Material import Material
from Persistence.Domain.Patologia import Patologia
from Persistence.Domain.PruebaDiagnostica import PruebaDiagnostica
from Persistence.Domain.Radiologo import Radiologo
from Persistence.Domain.Servicio import Servicio
from Persistence.Domain.TipoProcedimiento import TipoProcedimiento


combo_value_servicio_id = -1
combo_value_patologia_id = -1
combo_value_tipoprocedimiento_id = -1


class App():

    def delete_event(self, widget, event, data=None):
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()
        return

    def create_tree_pacientes(self):
        self.tree_model.clear()
        lista_pacientes = PacienteService.get_all()
        for elem in lista_pacientes:
            self.tree_model.append(None, [elem.id, elem.numerohistorial, elem.nombre])
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

    def hide_window(self, widget, event):
        window = widget.get_toplevel().get_toplevel().get_toplevel()
        window.hide()
        return

    def datospaciente_to_home(self, widget, event):
        self.builder.get_object('nhistorialhome1').set_text("")
        self.builder.get_object('nombrepacientehome1').set_text("")
        self.builder.get_object('fechanacimientohome1').set_text("")
        self.builder.get_object('nombreepisodiohome1').set_text("")
        self.builder.get_object('fechaepisodiohome1').set_text("")
        self.lista_servicios.set_active(-1)
        self.lista_patologias.set_active(-1)
        self.lista_tprocedimientos.set_active(-1)
        self.box_home.show()
        self.box_datos_paciente.hide()
        return

    def guardar_home(self, event, widget):
        numero_historial = self.builder.get_object('nhistorialhome1').get_text()
        nombre_paciente = self.builder.get_object('nombrepacientehome1').get_text()
        fecha_nacimiento = self.builder.get_object('fechanacimientohome1').get_text()
        nombre_episodio = self.builder.get_object('nombreepisodiohome1').get_text()
        fecha_episodio = self.builder.get_object('fechaepisodiohome1').get_text()
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
            button_aceptar.get_image().show()
        self.create_tree_pacientes()
        self.builder.get_object('nhistorialhome1').set_text("")
        self.builder.get_object('nombrepacientehome1').set_text("")
        self.builder.get_object('fechanacimientohome1').set_text("")
        self.builder.get_object('nombreepisodiohome1').set_text("")
        self.builder.get_object('fechaepisodiohome1').set_text("")
        self.lista_servicios.set_active(-1)
        self.lista_patologias.set_active(-1)
        self.lista_tprocedimientos.set_active(-1)
        return

    def datos_paciente(self, widget, event, data):
        self.box_home.hide()
        self.box_datos_paciente.show()
        inicio = self.builder.get_object("homedatospaciente")
        inicio.get_image().show()
        inicio.connect("button_press_event", self.datospaciente_to_home)
        iterador = self.tree.get_selection().get_selected()[1]
        paciente_id = self.tree_model.get_value(iterador, 0)
        paciente = PacienteService.get_by_id(paciente_id)
        self.builder.get_object("nombredatospaciente").set_text(paciente.nombre)
        self.builder.get_object("nhistorialdatospaciente").set_text(paciente.numerohistorial)
        self.builder.get_object("fechadatospaciente").set_text(str(paciente.fechanacimiento))
        self.builder.get_object("sexodatospaciente").set_text(paciente.sexo)
        self.builder.get_object("enfermedadesdatospaciente").set_text(paciente.enfermedadesconocidas)

        #Construccion de trees
        self.tree_facrores_riesgo_model.clear()
        factores = PacienteService.get_factores(paciente)
        for elem in factores:
            self.tree_facrores_riesgo_model.append(None, [elem.id, elem.nombre])

        self.tree_episodios_model.clear()
        episodios = PacienteService.get_episodios(paciente)
        for elem in episodios:
            self.tree_episodios_model.append(None, [elem.id, elem.nombre])
        self.builder.get_object("anadirfactordatospaciente").get_image().show()
        self.builder.get_object("quitarfactordatospaciente").get_image().show()

    def show_nservicio(self, widget):
        popup = self.builder.get_object("new_servicio")
        popup.connect("delete_event", self.delete_event)
        popup.set_position(gtk.WIN_POS_CENTER)
        popup.set_size_request(300, 150)
        button = self.builder.get_object("button_ca")
        button.connect("button_press_event", self.hide_window)
        button.get_image().show()
        popup.show()
        save = self.builder.get_object("button13")
        save.get_image().show()
        data = 'servicio'
        save.connect("button_press_event", self.save_popup, data)
        return

    def show_ncentro(self, widget):
        popup = self.builder.get_object("new_centro")
        popup.connect("delete_event", self.delete_event)
        popup.set_position(gtk.WIN_POS_CENTER)
        popup.set_size_request(300, 150)
        button = self.builder.get_object("button_cancel")
        button.connect("button_press_event", self.hide_window)
        button.get_image().show()
        popup.show()
        save = self.builder.get_object("button_save")
        data = 'centro'
        save.connect("button_press_event", self.save_popup, data)
        save.get_image().show()
        return

    def show_nmaterial(self, widget):
        popup = self.builder.get_object("new_material")
        popup.connect("delete_event", self.delete_event)
        popup.set_position(gtk.WIN_POS_CENTER)
        popup.set_size_request(300, 150)
        button = self.builder.get_object("button_cance1")
        button.connect("button_press_event", self.hide_window)
        button.get_image().show()
        popup.show()
        save = self.builder.get_object("button_sa1")
        save.get_image().show()
        data = 'material'
        save.connect("button_press_event", self.save_popup, data)
        return

    def show_nradiologo(self, widget):
        popup = self.builder.get_object("new_radiologo")
        popup.connect("delete_event", self.delete_event)
        popup.set_position(gtk.WIN_POS_CENTER)
        popup.set_size_request(300, 150)
        button = self.builder.get_object("button_can")
        button.connect("button_press_event", self.hide_window)
        button.get_image().show()
        popup.show()
        save = self.builder.get_object("button_")
        save.get_image().show()
        data = 'radiologo'
        save.connect("button_press_event", self.save_popup, data)
        return

    def show_nfactor(self, widget):
        popup = self.builder.get_object("new_factor")
        popup.connect("delete_event", self.delete_event)
        popup.set_position(gtk.WIN_POS_CENTER)
        popup.set_size_request(300, 150)
        button = self.builder.get_object("button_cance")
        button.connect("button_press_event", self.hide_window)
        button.get_image().show()
        popup.show()
        save = self.builder.get_object("button_sa")
        save.get_image().show()
        data = 'factor'
        save.connect("button_press_event", self.save_popup, data)
        return

    def show_npatologia(self, widget):
        popup = self.builder.get_object("new_patologia")
        popup.connect("delete_event", self.delete_event)
        popup.set_position(gtk.WIN_POS_CENTER)
        popup.set_size_request(300, 150)
        button = self.builder.get_object("button_canc")
        button.connect("button_press_event", self.hide_window)
        button.get_image().show()
        popup.show()
        save = self.builder.get_object("button_s")
        save.get_image().show()
        data = 'patologia'
        save.connect("button_press_event", self.save_popup, data)
        return

    def show_ntprocedimiento(self, widget):
        popup = self.builder.get_object("new_tipoprocedimiento")
        popup.connect("delete_event", self.delete_event)
        popup.set_position(gtk.WIN_POS_CENTER)
        popup.set_size_request(300, 150)
        button = self.builder.get_object("button_cance2")
        button.connect("button_press_event", self.hide_window)
        button.get_image().show()
        popup.show()
        save = self.builder.get_object("button_sa2")
        save.get_image().show()
        data = 'tprocedimiento'
        save.connect("button_press_event", self.save_popup, data)
        print('vuelvo')
        return

    def save_popup(self, event, widget, data):
        if data == 'servicio':
            try:
                nombre = self.builder.get_object("entry1").get_text()
                s = Servicio(0, nombre)
                ServicioService.create(s)
                self.builder.get_object("entry1").set_text("")
                self.lista_servicios_model.append([s.id, s.nombre])
            except TypeError:
                alert = self.builder.get_object("windowerror")
                alert.set_position(gtk.WIN_POS_CENTER)
                alert.show()
                self.builder.get_object("labelerror").set_text(str(sys.exc_info()[1]))
                button_aceptar = self.builder.get_object("buttonerror")
                button_aceptar.connect("button_press_event", self.hide_window)
                button_aceptar.get_image().show()
            popup = self.builder.get_object("new_servicio")
            popup.hide()
        if data == 'centro':
            try:
                nombre = self.builder.get_object("entry").get_text()
                c = Centro(0, nombre)
                CentroService.create(c)
                self.builder.get_object("entry").set_text("")
            except TypeError:
                alert = self.builder.get_object("windowerror")
                alert.set_position(gtk.WIN_POS_CENTER)
                alert.show()
                self.builder.get_object("labelerror").set_text(str(sys.exc_info()[1]))
                button_aceptar = self.builder.get_object("buttonerror")
                button_aceptar.connect("button_press_event", self.hide_window)
                button_aceptar.get_image().show()
            popup = self.builder.get_object("new_centro")
            popup.hide()
        if data == 'material':
            try:
                nombre = self.builder.get_object("entry3").get_text()
                m = Material(0, nombre)
                MaterialService.create(m)
                self.builder.get_object("entry3").set_text("")
            except TypeError:
                alert = self.builder.get_object("windowerror")
                alert.set_position(gtk.WIN_POS_CENTER)
                alert.show()
                self.builder.get_object("labelerror").set_text(str(sys.exc_info()[1]))
                button_aceptar = self.builder.get_object("buttonerror")
                button_aceptar.connect("button_press_event", self.hide_window)
                button_aceptar.get_image().show()
            popup = self.builder.get_object("new_material")
            popup.hide()
        if data == 'radiologo':
            try:
                nombre = self.builder.get_object("entry4").get_text()
                r = Radiologo(0, nombre)
                RadiologoService.create(r)
                self.builder.get_object("entry4").set_text("")
            except TypeError:
                alert = self.builder.get_object("windowerror")
                alert.set_position(gtk.WIN_POS_CENTER)
                alert.show()
                self.builder.get_object("labelerror").set_text(str(sys.exc_info()[1]))
                button_aceptar = self.builder.get_object("buttonerror")
                button_aceptar.connect("button_press_event", self.hide_window)
                button_aceptar.get_image().show()
            popup = self.builder.get_object("new_radiologo")
            popup.hide()
        if data == 'factor':
            try:
                nombre = self.builder.get_object("entry7").get_text()
                f = Factor(0, nombre)
                FactorService.create(f)
                self.builder.get_object("entry7").set_text("")
            except TypeError:
                alert = self.builder.get_object("windowerror")
                alert.set_position(gtk.WIN_POS_CENTER)
                alert.show()
                self.builder.get_object("labelerror").set_text(str(sys.exc_info()[1]))
                button_aceptar = self.builder.get_object("buttonerror")
                button_aceptar.connect("button_press_event", self.hide_window)
                button_aceptar.get_image().show()
            popup = self.builder.get_object("new_factor")
            popup.hide()
        if data == 'patologia':
            try:
                nombre = self.builder.get_object("entry6").get_text()
                p = Patologia(0, nombre)
                PatologiaService.create(p)
                self.builder.get_object("entry6").set_text("")
                self.lista_patologias_model.append([p.id, p.nombre])
            except TypeError:
                alert = self.builder.get_object("windowerror")
                alert.set_position(gtk.WIN_POS_CENTER)
                alert.show()
                self.builder.get_object("labelerror").set_text(str(sys.exc_info()[1]))
                button_aceptar = self.builder.get_object("buttonerror")
                button_aceptar.connect("button_press_event", self.hide_window)
                button_aceptar.get_image().show()
            popup = self.builder.get_object("new_patologia")
            popup.hide()
        if data == 'tprocedimiento':
            try:
                nombre = self.builder.get_object("entry2").get_text()
                tp = TipoProcedimiento(0, nombre)
                TipoProcedimientoService.create(tp)
                self.builder.get_object("entry2").set_text("")
                self.lista_servicios_model.append([tp.id, tp.nombre])
            except TypeError:
                alert = self.builder.get_object("windowerror")
                alert.set_position(gtk.WIN_POS_CENTER)
                alert.show()
                self.builder.get_object("labelerror").set_text(str(sys.exc_info()[1]))
                button_aceptar = self.builder.get_object("buttonerror")
                button_aceptar.connect("button_press_event", self.hide_window)
                button_aceptar.get_image().show()
            popup = self.builder.get_object("new_tipoprocedimiento")
            popup.hide()
        return

    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("gui - ejecutable.glade")
        self.window = self.builder.get_object("vistabasica")
        self.window.set_size_request(1024, 700)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.show()

        #boxs
        self.container = self.builder.get_object("hbox20")
        self.box_home = self.builder.get_object("boxhome")
        self.box_datos_paciente = self.builder.get_object("boxdatospaciente")

        #empaquetados
        self.container.pack_start(self.box_home)
        self.container.pack_start(self.box_datos_paciente)
        self.box_datos_paciente.hide()

        #conexiones del menu
        menu_item_nuevoservicio = self.builder.get_object("nuevoservicio")
        menu_item_nuevoservicio.connect("activate", self.show_nservicio)
        menu_item_nuevocentro = self.builder.get_object("nuevocentro")
        menu_item_nuevocentro.connect("activate", self.show_ncentro)
        menu_item_nuevomaterial = self.builder.get_object("nuevomaterial")
        menu_item_nuevomaterial.connect("activate", self.show_nmaterial)
        menu_item_nuevoradiologo = self.builder.get_object("nuevoradiologo")
        menu_item_nuevoradiologo.connect("activate", self.show_nradiologo)
        menu_item_nuevofactor = self.builder.get_object("nuevofactor")
        menu_item_nuevofactor.connect("activate", self.show_nfactor)
        menu_item_nuevapatologia = self.builder.get_object("nuevapatologia")
        menu_item_nuevapatologia.connect("activate", self.show_npatologia)
        menu_item_nuevotipoprocedimiento = self.builder.get_object("nuevotipoprocedimiento")
        menu_item_nuevotipoprocedimiento.connect("activate", self.show_ntprocedimiento)

        #rellenado del tree con los pacientes
        self.tree = self.builder.get_object("treeview8")
        self.tree_model = gtk.TreeStore(int, str, str)
        cellid = gtk.CellRendererText()
        cellid.set_visible(False)
        cellnh = gtk.CellRendererText()
        col1 = gtk.TreeViewColumn("Numero Historial", cellnh)
        col1.add_attribute(cellnh, 'text', 1)
        celln = gtk.CellRendererText()
        col2 = gtk.TreeViewColumn("Nombre", celln)
        col2.add_attribute(celln, 'text', 2)
        self.tree.append_column(col1)
        self.tree.append_column(col2)
        self.tree.set_model(self.tree_model)
        self.create_tree_pacientes()

        #RELLENADO DE LA BOX INICIAL
        #La lista de servicios
        servicios = ServicioService.get_all()
        self.lista_servicios = self.builder.get_object('serviciohome1')
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
        self.lista_patologias = self.builder.get_object('patologiahome1')
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
        self.lista_tprocedimientos = self.builder.get_object('tipoprocedimientohome1')
        self.lista_tprocedimientos_model = gtk.ListStore(int, str)
        for elem in tprocedimientos:
            self.lista_tprocedimientos_model.append([elem.id, elem.nombre])
        cell = gtk.CellRendererText()
        self.lista_tprocedimientos.set_model(self.lista_tprocedimientos_model)
        self.lista_tprocedimientos.pack_start(cell)
        self.lista_tprocedimientos.set_attributes(cell, text=1)
        self.lista_tprocedimientos.connect('changed', self.changed_cb_tipoprocedimiento)

        #Boton Guardarhome
        self.button_guardar = self.builder.get_object('guardarhome1')
        self.button_guardar.connect("button_press_event", self.guardar_home)
        self.button_guardar.get_image().show()

        #Ver datos paciente
        self.tree.connect("row-activated", self.datos_paciente)

        #Tree factores
        self.tree_facrores_riesgo = self.builder.get_object("factoresdatospaciente")
        self.tree_facrores_riesgo_model = gtk.TreeStore(int, str)
        cellid_factores = gtk.CellRendererText()
        cellid_factores.set_visible(False)
        cellnh_factores = gtk.CellRendererText()
        col1_factores = gtk.TreeViewColumn("Nombre", cellnh_factores)
        col1_factores.add_attribute(cellnh_factores, 'text', 1)
        self.tree_facrores_riesgo.append_column(col1_factores)
        self.tree_facrores_riesgo.set_model(self.tree_facrores_riesgo_model)

        #Tree episodios
        self.tree_episodios = self.builder.get_object("episodiosdatospaciente")
        self.tree_episodios_model = gtk.TreeStore(int, str)
        cellid_episodios = gtk.CellRendererText()
        cellid_episodios.set_visible(False)
        cellnh_episodios = gtk.CellRendererText()
        col1_episodios = gtk.TreeViewColumn("Nombre", cellnh_episodios)
        col1_episodios.add_attribute(cellnh_episodios, 'text', 1)
        self.tree_episodios.append_column(col1_episodios)
        self.tree_episodios.set_model(self.tree_episodios_model)


if __name__ == "__main__":
    app = App()
    gtk.main()