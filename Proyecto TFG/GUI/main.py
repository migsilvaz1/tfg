import sys
import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
from Persistence.Services import PacienteService, ServicioService, PatologiaService, EpisodioService, \
    ProcedimientoService, TipoProcedimientoService, RelationsService, CentroService, ComplicacionService, \
    DiagnosticoService, EvolucionService, FactorService, MaterialService, PruebaDiagnosticaService, RadiologoService, \
    QuerysService
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
combo_value_centro_id = -1
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

    def changed_cb_centro(self, combobox):
        global combo_value_centro_id
        index = combobox.get_active()
        model = combobox.get_model()
        combo_value_centro_id = model[index][0]
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
        self.container.remove(self.box_datos_paciente)
        self.container.pack_start(self.box_home)
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
        self.container.remove(self.container.get_children()[2])
        self.container.pack_start(self.box_datos_paciente)
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
        self.builder.get_object("buttonsave5").get_image().show()

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

    def show_epatologias(self, event):
        tree_listapatologias_model = gtk.TreeStore(int, str)
        cellid = gtk.CellRendererText()
        cellid.set_visible(False)
        celln = gtk.CellRendererText()
        col1 = gtk.TreeViewColumn("Nombre", celln)
        col1.add_attribute(celln, 'text', 1)
        self.tree.remove_column(self.tree.get_columns()[0])
        self.tree.remove_column(self.tree.get_columns()[0])
        self.tree.append_column(col1)
        patologias = PatologiaService.get_all()
        for elem in patologias:
            tree_listapatologias_model.append(None, [elem.id, elem.nombre])
        self.tree.set_model(tree_listapatologias_model)
        self.container.remove(self.container.get_children()[2])
        self.container.pack_start(self.box_epatologia)

        #Labels
        p = PatologiaService.get_by_id(1)
        self.builder.get_object("label129").set_text(p.nombre)
        self.builder.get_object("label108").set_text(str(QuerysService.porcentaje_complicaciones_patologia(p)))
        self.builder.get_object("label111").set_text(str(QuerysService.pacientes_factores_patologia(p)))
        self.builder.get_object("label113").set_text(str(QuerysService.edad_media_pacientes_patologia(p)))
        self.builder.get_object("label122").set_text(str(QuerysService.sexo_patologia(p, 'H')))
        self.builder.get_object("label124").set_text(str(QuerysService.sexo_patologia(p, 'M')))
        self.builder.get_object("label126").set_text(str(QuerysService.mortalidad_temprana_patologia(p)))
        #Tree de procedimientos
        tree_curados_procedimiento = self.builder.get_object("treeview18")
        tree_curados_model = gtk.TreeStore(str, int)
        cellprocedimiento = gtk.CellRendererText()
        col1 = gtk.TreeViewColumn("Procedimiento", cellprocedimiento)
        col1.add_attribute(cellprocedimiento, 'text', 0)
        celln = gtk.CellRendererText()
        col2 = gtk.TreeViewColumn("Pacientes Curados", celln)
        col2.add_attribute(celln, 'text', 1)
        tree_curados_procedimiento.append_column(col1)
        tree_curados_procedimiento.append_column(col2)
        procedimientos = ProcedimientoService.get_all()
        for elem in procedimientos:
            tipop = TipoProcedimientoService.get_by_id(elem.idtipop)
            curados = QuerysService.curacion_patologia_procedimiento(p, tipop)
            tree_curados_model.append(None, [tipop.nombre, curados])
        tree_curados_procedimiento.set_model(tree_curados_model)

        #buttons
        inicio = self.builder.get_object("button19")
        inicio.get_image().show()
        inicio.connect("button_press_event", self.go_home)
        imprimir = self.builder.get_object("button_save1")
        imprimir.get_image().show()
        return

    def go_home(self, event, widget):
        self.tree.remove_column(self.tree.get_columns()[0])
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
        self.container.remove(self.container.get_children()[2])
        self.container.pack_start(self.box_home)
        return

    def show_egenerales(self, event):
        return

    def show_importar(self, event):
        self.box_importar.set_position(gtk.WIN_POS_CENTER)
        self.box_importar.show()
        aceptar = self.builder.get_object("button15")
        aceptar.get_image().show()
        cancelar = self.builder.get_object("button14")
        cancelar.get_image().show()
        cancelar.connect("button_press_event", self.hide_window)
        return

    def show_exportar(self, event):
        self.box_exportar.set_position(gtk.WIN_POS_CENTER)
        self.box_exportar.show()
        aceptar = self.builder.get_object("button12")
        aceptar.get_image().show()
        cancelar = self.builder.get_object("button11")
        cancelar.get_image().show()
        cancelar.connect("button_press_event", self.hide_window)
        return

    def datos_episodio(self, widget, event, data):
        self.container.remove(self.container.get_children()[2])
        self.container.pack_start(self.box_episodio)
        iterador = self.tree_episodios.get_selection().get_selected()[1]
        episodio_id = self.tree_episodios_model.get_value(iterador, 0)
        episodio = EpisodioService.get_by_id(episodio_id)

        #comboboxes
        centros = CentroService.get_all()
        lista_centros = self.builder.get_object('combobox6')
        lista_centros_model = gtk.ListStore(int, str)
        for elem in centros:
            lista_centros_model.append([elem.id, elem.nombre])
        cell = gtk.CellRendererText()
        lista_centros.set_model(lista_centros_model)
        lista_centros.pack_start(cell)
        lista_centros.set_attributes(cell, text=1)
        lista_centros.connect('changed', self.changed_cb_centro)

        servicios = ServicioService.get_all()
        lista_servicios = self.builder.get_object('combobox1')
        lista_servicios_model = gtk.ListStore(int, str)
        for elem in servicios:
            lista_servicios_model.append([elem.id, elem.nombre])
        cell = gtk.CellRendererText()
        lista_servicios.set_model(lista_servicios_model)
        lista_servicios.pack_start(cell)
        lista_servicios.set_attributes(cell, text=1)
        lista_servicios.connect('changed', self.changed_cb_servicio)

        patologias = PatologiaService.get_all()
        lista_patologias = self.builder.get_object('combobox4')
        lista_patologias_model = gtk.ListStore(int, str)
        for elem in patologias:
            lista_patologias_model.append([elem.id, elem.nombre])
        cell = gtk.CellRendererText()
        lista_patologias.set_model(lista_patologias_model)
        lista_patologias.pack_start(cell)
        lista_patologias.set_attributes(cell, text=1)
        lista_patologias.connect('changed', self.changed_cb_patologia)


        cellid_procedimientos = gtk.CellRendererText()
        cellid_procedimientos.set_visible(False)
        celln_procedimientos = gtk.CellRendererText()
        col1_procedimientos = gtk.TreeViewColumn("Nombre", celln_procedimientos)
        col1_procedimientos.add_attribute(celln_procedimientos, 'text', 1)
        self.tree_procedimientos.append_column(col1_procedimientos)
        self.tree_procedimientos.set_model(self.tree_procedimientos_model)
        for elem in EpisodioService.get_procedimientos(episodio):
            self.tree_procedimientos_model.append(None, [elem.id, ProcedimientoService.get_tipoprocedimiento(elem).nombre])
        self.tree_procedimientos.connect("row-activated", self.datos_procedimiento)

        tree_pdiag = self.builder.get_object("treeview17")
        tree_pdiag_model = gtk.TreeStore(int, str)
        cellid_pdiag = gtk.CellRendererText()
        cellid_pdiag.set_visible(False)
        celln_pdiag = gtk.CellRendererText()
        col1_pdiag = gtk.TreeViewColumn("Nombre", celln_pdiag)
        col1_pdiag.add_attribute(celln_pdiag, 'text', 1)
        tree_pdiag.append_column(col1_pdiag)
        tree_pdiag.set_model(tree_pdiag_model)
        for elem in EpisodioService.get_pruebas(episodio):
            tree_pdiag_model.append(None, [elem.id, elem.nombre])

        #Inicializado de atributos
        self.builder.get_object("entry8").set_text(episodio.nombre)
        self.builder.get_object("entry9").set_text(str(episodio.fecha))
        self.builder.get_object("entry11").set_text(EpisodioService.get_diagnosticos(episodio)[0].nombre)
        self.builder.get_object("buttonerror1").get_image().show()
        self.builder.get_object("buttonerror3").get_image().show()
        self.builder.get_object("buttonerror4").get_image().show()
        self.builder.get_object("buttonerror2").get_image().show()
        return

    def datos_procedimiento(self, widget, event, data):
        self.container.remove(self.container.get_children()[2])
        self.container.pack_start(self.box_procedimiento)
        iterador = self.tree_procedimientos.get_selection().get_selected()[1]
        prod_id = self.tree_procedimientos_model.get_value(iterador, 0)
        procedimiento = ProcedimientoService.get_by_id(prod_id)

        #treematerial
        tree_material = self.builder.get_object("treeview1")
        tree_material_model = gtk.TreeStore(int, str)
        cellid = gtk.CellRendererText()
        cellid.set_visible(False)
        celln_m = gtk.CellRendererText()
        col = gtk.TreeViewColumn("Nombre", celln_m)
        col.add_attribute(celln_m, 'text', 1)
        tree_material.append_column(col)
        tree_material.set_model(tree_material_model)
        for elem in ProcedimientoService.get_materiales(procedimiento):
            tree_material_model.append(None, [elem.id, elem.nombre])

        #treecomplicaciones
        tree_comp = self.builder.get_object("treeview2")
        tree_comp_model = gtk.TreeStore(int, str)
        cellid = gtk.CellRendererText()
        cellid.set_visible(False)
        celln_c = gtk.CellRendererText()
        col = gtk.TreeViewColumn("Nombre", celln_c)
        col.add_attribute(celln_c, 'text', 1)
        tree_comp.append_column(col)
        tree_comp.set_model(tree_comp_model)
        for elem in ProcedimientoService.get_complicaciones(procedimiento):
            tree_comp_model.append(None, [elem.id, elem.nombre])

        #comboboxtipoprod
        tprocedimientos = TipoProcedimientoService.get_all()
        lista_tprocedimientos = self.builder.get_object('combobox5')
        lista_tprocedimientos_model = gtk.ListStore(int, str)
        for elem in tprocedimientos:
            lista_tprocedimientos_model.append([elem.id, elem.nombre])
        cell = gtk.CellRendererText()
        lista_tprocedimientos.set_model(lista_tprocedimientos_model)
        lista_tprocedimientos.pack_start(cell)
        lista_tprocedimientos.set_attributes(cell, text=1)
        lista_tprocedimientos.connect('changed', self.changed_cb_tipoprocedimiento)
        resultado_evolucion = self.builder.get_object("entry10").set_text(EvolucionService.get_by_id(procedimiento.idevolucion).resultado)
        notas_evolucion = self.builder.get_object("entry12").set_text(EvolucionService.get_by_id(procedimiento.idevolucion).notas)
        anadir_material = self.builder.get_object("button16")
        anadir_material.get_image().show()
        eliminar_material = self.builder.get_object("button20")
        eliminar_material.get_image().show()
        anadir_complicacion = self.builder.get_object("button21")
        anadir_complicacion.get_image().show()
        eliminar_complicacion = self.builder.get_object("button22")
        eliminar_complicacion.get_image().show()
        anadir_imagen = self.builder.get_object("button23")
        anadir_imagen.get_image().show()
        eliminar = self.builder.get_object("button24")
        eliminar.get_image().show()
        guardar = self.builder.get_object("button3")
        guardar.get_image().show()
        inicio = self.builder.get_object("button4")
        inicio.get_image().show()
        return

    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("gui - ejecutable.glade")
        self.window = self.builder.get_object("vistabasica")
        self.window.set_size_request(900, 600)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.show()

        #boxes
        self.container = self.builder.get_object("hbox20")
        self.box_home = self.builder.get_object("boxhome")
        self.box_datos_paciente = self.builder.get_object("boxdatospaciente")
        self.box_epatologia = self.builder.get_object("table12")
        self.box_exportar = self.builder.get_object("exportarbd")
        self.box_importar = self.builder.get_object("importarbd")
        self.box_episodio = self.builder.get_object("table3")
        self.box_procedimiento = self.builder.get_object("table1")
        self.container.pack_start(self.box_home)

        #conexiones del menu
        #CREAR
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
        #ESTADISTICAS
        menu_item_epatologias = self.builder.get_object("estadisticaspatologias")
        menu_item_epatologias.connect("activate", self.show_epatologias)
        menu_item_egenerales = self.builder.get_object("estadisticasgenerales")
        menu_item_egenerales.connect("activate", self.show_egenerales)
        #DATOS
        menu_item_exportar = self.builder.get_object("exportarb")
        menu_item_exportar.connect("activate", self.show_exportar)
        menu_item_importar = self.builder.get_object("importarb")
        menu_item_importar.connect("activate", self.show_importar)

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

        #Ver datos episodio
        self.tree_episodios.connect("row-activated", self.datos_episodio)

        #tree procedimientos
        self.tree_procedimientos = self.builder.get_object("treeview14")
        self.tree_procedimientos_model = gtk.TreeStore(int, str)


if __name__ == "__main__":
    app = App()
    gtk.main()