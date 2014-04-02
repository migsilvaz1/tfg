CREATE TABLE autores(
    id_autor INTEGER NOT NULL,
    nombre VARCHAR(100),
    sexo VARCHAR(9),
    nacionalidad VARCHAR(50),
    rol VARCHAR(9),
    PRIMARY KEY(id_autor),
    CHECK(sexo ='masculino' OR sexo = 'femenino'),
    CHECK(rol = 'grafista'OR rol = 'guionista' OR rol = 'dibujante' OR rol = 'traductor')
);

CREATE TABLE colecciones(
    nombreColeccion VARCHAR(100) NOT NULL,
    numeroProductos INTEGER,
    PRIMARY KEY(nombreColeccion),
    CHECK(numeroProductos>0)
);

CREATE TABLE personajes(
    id_personaje INTEGER NOT NULL,
    nombre VARCHAR(100),
    apodo VARCHAR(50), 
    PRIMARY KEY(id_personaje),
    UNIQUE(nombre, apodo)
);

CREATE TABLE productos(
    id_producto INTEGER NOT NULL,
    nombre VARCHAR(100),
    precio NUMBER(5,2) NOT NULL,
    edadRecomendada INTEGER,
    PRIMARY KEY(id_producto),
    CHECK(precio> 0.0),
    CHECK(edadRecomendada>=0 AND edadRecomendada<100)
);

CREATE TABLE relColeccionProducto(
    id_producto INTEGER NOT NULL,
    nombreColeccion VARCHAR(100) NOT NULL,
    PRIMARY KEY(nombreColeccion, id_producto),
    FOREIGN KEY(nombreColeccion) REFERENCES colecciones(nombreColeccion),
    FOREIGN KEY(id_producto) REFERENCES productos(id_producto)
);

CREATE TABLE relPersonajeProducto(
    id_personaje INTEGER NOT NULL,
    id_producto INTEGER NOT NULL,
    PRIMARY KEY(id_personaje, id_producto),
    FOREIGN KEY(id_personaje) REFERENCES personajes(id_personaje),
    FOREIGN KEY(id_producto) REFERENCES productos(id_producto)
);

CREATE TABLE merchandising(
    id_merchandising INTEGER NOT NULL,
    marca VARCHAR(20),
    id_producto INTEGER NOT NULL,
    PRIMARY KEY(id_merchandising),
    FOREIGN KEY(id_producto) REFERENCES productos(id_producto)
);

CREATE TABLE impresos(
    id_impreso INTEGER NOT NULL,
    editorial VARCHAR(20) NOT NULL,
    precioAlquiler NUMBER(5,2) NOT NULL,
    id_producto INTEGER NOT NULL,
    PRIMARY KEY(id_impreso),
    FOREIGN KEY(id_producto) REFERENCES productos(id_producto),
    CHECK(precioAlquiler>0.0)
);

CREATE TABLE comics(
    id_comic INTEGER NOT NULL,
    tipoComic VARCHAR(5),
    generoComic VARCHAR(7),
    id_impreso INTEGER NOT NULL,
    PRIMARY KEY(id_comic),
    FOREIGN KEY(id_impreso) REFERENCES impresos(id_impreso),
    CHECK(tipoComic = 'grapa' OR tipoComic = 'tomo'),
    CHECK(generoComic = 'manga' OR generoComic = 'viñetas'OR generoComic = 'heroico')
);

CREATE TABLE libros(
    id_libro INTEGER NOT NULL,
    tipoLibro VARCHAR(10),
    generoLibro VARCHAR(15),
    id_impreso INTEGER NOT NULL,
    PRIMARY KEY(id_libro),
    FOREIGN KEY(id_impreso) REFERENCES impresos(id_impreso),
    CHECK(tipoLibro='bolsillo' OR tipoLibro='tapaDura' OR tipoLibro='tapaBlanda'),
    CHECK(generoLibro='aventura' OR generoLibro='cienciaFiccion' OR generoLibro='clasicos' OR generoLibro='cuentos' OR generoLibro='ensayos' OR generoLibro='novelaNarrativa' OR generoLibro='novelaPolicial' OR generoLibro='novelaHistorica' OR generoLibro='poesia' OR generoLibro='teatro' OR generoLibro='tecnicos' OR generoLibro='infantil')
);

CREATE TABLE relAutorImpreso(
    id_autor INTEGER NOT NULL,
    id_impreso INTEGER NOT NULL,
    PRIMARY KEY(id_autor, id_impreso),
    FOREIGN KEY(id_autor) REFERENCES autores(id_autor),
    FOREIGN KEY(id_impreso) REFERENCES impresos(id_impreso)
);

CREATE TABLE eventos(
    id_evento INTEGER NOT NULL,
    nombre VARCHAR(100),
    fecha DATE,
    duracion INTEGER,
    precioEntrada NUMBER(5,2),
    sitiosVip INTEGER,
    PRIMARY KEY(id_evento),
    CHECK(duracion>0),
    CHECK(precioEntrada>=0.0),
    CHECK(sitiosVIP>0)
);

CREATE TABLE localizaciones(
    id_localizacion INTEGER NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    correo VARCHAR(100),
    PRIMARY KEY (id_localizacion)
);

CREATE TABLE relProductosLocalizaciones(
    id_producto INTEGER NOT NULL,
    id_localizacion INTEGER NOT NULL,
    PRIMARY KEY (id_producto,id_localizacion),
    FOREIGN KEY(id_producto) REFERENCES productos(id_producto),
    FOREIGN KEY(id_localizacion) REFERENCES localizaciones(id_localizacion)
);

CREATE TABLE webs(
    id_web INTEGER NOT NULL,
    id_localizacion INTEGER NOT NULL,
    dominio VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_web),
    FOREIGN KEY (id_localizacion) REFERENCES localizaciones(id_localizacion)
);

CREATE TABLE lugaresFisicos(
    id_lugarFisico INTEGER NOT NULL,
    id_localizacion INTEGER NOT NULL,
    direccion VARCHAR(200),
    telefono INTEGER,
    fax INTEGER,
    PRIMARY KEY(id_lugarFisico),
    FOREIGN KEY(id_localizacion) REFERENCES localizaciones(id_localizacion),
    CHECK(telefono<1000000000),
    CHECK(fax<10000000000)
);

CREATE TABLE lugaresEventos(
    id_lugarEvento INTEGER NOT NULL,
    id_lugarFisico INTEGER NOT NULL,
    aforo INTEGER,
    id_evento INTEGER NOT NULL,
    PRIMARY KEY(id_lugarEvento),
    FOREIGN KEY(id_lugarFisico) REFERENCES lugaresFisicos(id_lugarFisico),
    FOREIGN KEY(id_evento) REFERENCES eventos(id_evento),
    CHECK(aforo<999)
);

CREATE TABLE almacenes(
    id_almacen INTEGER NOT NULL,
    id_lugarFisico INTEGER NOT NULL,
    PRIMARY KEY(id_almacen),
    FOREIGN KEY(id_lugarFisico)REFERENCES lugaresFisicos(id_lugarFisico)
);

CREATE TABLE stockAlmacenes(
    id_almacen INTEGER NOT NULL,
    id_producto INTEGER NOT NULL,
    numero INTEGER,
    ubicacionProducto VARCHAR(500),
    PRIMARY KEY(id_almacen, id_producto),
    FOREIGN KEY(id_almacen) REFERENCES almacenes(id_almacen),
    FOREIGN KEY(id_producto) REFERENCES productos(id_producto),
    CHECK(numero>=0)
);

CREATE TABLE tiendas(
    id_tienda INTEGER NOT NULL,
    id_lugarFisico INTEGER NOT NULL,
    horario VARCHAR(50),
    PRIMARY KEY(id_tienda),
    FOREIGN KEY(id_lugarFisico) REFERENCES lugaresFisicos(id_lugarFisico)
);

CREATE TABLE stockTiendas(
    id_tienda INTEGER NOT NULL,
    id_producto INTEGER NOT NULL,
    cantidad INTEGER,
    PRIMARY KEY(id_tienda, id_producto),
    FOREIGN KEY(id_producto) REFERENCES productos(id_producto),
    FOREIGN KEY(id_tienda) REFERENCES tiendas(id_tienda),
    CHECK(cantidad>=0)
);

CREATE TABLE socios(
    numeroSocio INTEGER NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    sexo VARCHAR(9),
    edad INTEGER,
    telefono INTEGER,
    correo VARCHAR(100),
    direccion VARCHAR(500),
    vip char(1) NOT NULL,
    fechaIngreso DATE,
    cantidadGastada NUMBER(5,2) DEFAULT 0.0,
    fechaFinSancion DATE,
    fechaNacimiento DATE,
    PRIMARY KEY(numeroSocio),
    CHECK(sexo = 'masculino'OR sexo = 'femenino'),
    CHECK(edad>=0),
    CHECK(numeroSocio>0),
    CHECK(telefono<1000000000),
    CHECK(vip = 'Y' OR vip = 'N')
);

CREATE TABLE relEventosSocios(
    id_evento INTEGER NOT NULL,
    numeroSocio INTEGER NOT NULL,
    PRIMARY KEY(id_evento,numeroSocio),
    FOREIGN KEY(id_evento) REFERENCES eventos(id_evento),
    FOREIGN KEY(numeroSocio) REFERENCES socios(numeroSocio)
);

CREATE TABLE proveedores(
    id_proveedor INTEGER NOT NULL,
    nombre VARCHAR(100),
    diaReparto VARCHAR(10),
    direccion VARCHAR(100),
    telefono INTEGER,
    fax INTEGER,
    correo VARCHAR(100),
    personaDeContacto VARCHAR (100),
    PRIMARY KEY(id_proveedor),
    CHECK(diaReparto = 'lunes'OR diaReparto = 'martes'OR diaReparto = 'miercoles'OR diaReparto = 'jueves'OR diaReparto = 'viernes' OR diaReparto = 'sabado'OR diaReparto = 'domingo'),
    CHECK(telefono<1000000000),
    CHECK(fax<10000000000)
);

CREATE TABLE pedidos(
    numeroPedido INTEGER NOT NULL,
    fecha DATE,
    satisfecho char(1),
    id_proveedor INTEGER NOT NULL,
    PRIMARY KEY(numeroPedido),
    FOREIGN KEY(id_proveedor) REFERENCES proveedores(id_proveedor),
    CHECK(satisfecho = 'Y'OR satisfecho = 'N')  
);

CREATE TABLE lineasPedidos(
    numeroPedido INTEGER NOT NULL,
    id_producto INTEGER NOT NULL,
    cantidad INTEGER,
    PRIMARY KEY(numeroPedido, id_producto),
    FOREIGN KEY(numeroPedido) REFERENCES pedidos(numeroPedido),
    FOREIGN KEY(id_producto) REFERENCES productos(id_producto),
    CHECK(cantidad>1)
);

--secuencia para la creacion de ID

CREATE SEQUENCE sec_ids
START WITH 1
INCREMENT BY 1;

--Secuencia para la creacion de numeroSocio

CREATE SEQUENCE sec_numeroSocio
START WITH 1
INCREMENT BY 1;

--Secuencia para la creacion de numeroPedido

CREATE SEQUENCE sec_numeroPedido
START WITH 1
INCREMENT BY 1;

--Metodos para automatizar las inserciones en las tablas

CREATE OR REPLACE PROCEDURE nuevoAutor(
    w_nombre IN autores.nombre%TYPE,
    w_sexo IN autores.sexo%TYPE,
    w_nacionalidad IN autores.nacionalidad%TYPE,
    w_rol IN autores.rol%TYPE)
    IS
        --autorExiste VARCHAR(100) DEFAULT NULL;
    BEGIN
        --SELECT autores.nombre INTO autorExiste FROM autores WHERE autores.nombre =w_nombre;
        --IF autorExiste IS NULL THEN
            INSERT INTO autores(id_autor,nombre,sexo,nacionalidad,rol) VALUES (sec_ids.NEXTVAL,w_nombre, w_sexo, w_nacionalidad, w_rol);
            COMMIT;
        --END IF;
END nuevoAutor;

CREATE OR REPLACE PROCEDURE nuevaColeccion(
    w_nombreColeccion IN colecciones.nombreColeccion%TYPE,
    w_numeroProductos IN colecciones.numeroProductos%TYPE)
    IS
    BEGIN
        INSERT INTO colecciones(nombreColeccion,numeroProductos) VALUES (w_nombreColeccion, w_numeroProductos);
        COMMIT;
END nuevaColeccion;

CREATE OR REPLACE PROCEDURE nuevoPersonaje(
    w_nombre IN personajes.nombre%TYPE,
    w_apodo IN personajes.apodo%TYPE)
    IS
    BEGIN
        INSERT INTO personajes(id_personaje,nombre,apodo) VALUES (sec_ids.NEXTVAL, w_nombre, w_apodo);
        COMMIT;
END nuevoPersonaje;

CREATE OR REPLACE PROCEDURE nuevoProducto(
    w_nombre IN productos.nombre%TYPE,
    w_precio IN productos.precio%TYPE,
    w_edadRecomendada IN productos.edadRecomendada%TYPE)
    IS
    BEGIN
        INSERT INTO productos(id_producto,nombre,precio,edadRecomendada) VALUES (sec_ids.NEXTVAL,w_nombre,w_precio,w_edadRecomendada);
        COMMIT;
END nuevoProducto;

CREATE OR REPLACE PROCEDURE nuevaRelColeccionProducto(
    w_nombreColeccion IN relColeccionProducto.nombreColeccion%TYPE,
    w_id_producto IN relColeccionProducto.id_producto%TYPE)
    IS
    BEGIN
        INSERT INTO relColeccionProducto(nombreColeccion,id_producto) VALUES (w_nombreColeccion, w_id_producto);
        COMMIT;
END nuevaRelColeccionProducto;

CREATE OR REPLACE PROCEDURE nuevaRelPersonajeProducto(
    w_id_personaje IN relPersonajeProducto.id_personaje%TYPE,
    w_id_producto IN relPersonajeProducto.id_producto%TYPE)
    IS
    BEGIN
        INSERT INTO relPersonajeProducto(id_personaje,id_producto) VALUES (w_id_personaje, w_id_producto);
        COMMIT;
END nuevaRelPersonajeProducto;

CREATE OR REPLACE PROCEDURE nuevoMerchandising(
    w_marca IN merchandising.marca%TYPE,
    w_id_producto IN merchandising.id_producto%TYPE)
    IS
    BEGIN
        INSERT INTO merchandising(id_merchandising,marca, id_producto) VALUES (sec_ids.NEXTVAL,w_marca, w_id_producto);
        COMMIT;
END nuevoMerchandising;

CREATE OR REPLACE PROCEDURE nuevoImpreso(
    w_editorial IN impresos.editorial%TYPE,
    w_precioAlquiler IN impresos.precioAlquiler%TYPE,
    w_id_producto IN impresos.id_producto%TYPE)
    IS
    BEGIN
        INSERT INTO impresos(id_impreso,editorial,precioAlquiler, id_producto) VALUES (sec_ids.NEXTVAL,w_editorial, w_precioAlquiler, w_id_producto);
        COMMIT;
END nuevoImpreso;

CREATE OR REPLACE PROCEDURE nuevoComic(
    w_tipoComic IN comics.tipoComic%TYPE,
    w_generoComic IN comics.generoComic%TYPE,
    w_id_impreso IN comics.id_impreso%TYPE)
    IS
    BEGIN
        INSERT INTO comics(id_comic,tipoComic,generoComic, id_impreso) VALUES (sec_ids.NEXTVAL,w_tipoComic, w_generoComic, w_id_impreso);
        COMMIT;
END nuevoComic;

CREATE OR REPLACE PROCEDURE nuevoLibro(
    w_tipoLibro IN libros.tipoLibro%TYPE,
    w_generoLibro IN libros.generoLibro%TYPE,
    w_impreso IN libros.id_impreso%TYPE)
    IS
    BEGIN
        INSERT INTO libros(id_libro,tipoLibro,generoLibro, id_impreso) VALUES (sec_ids.NEXTVAL,w_tipoLibro, w_generoLibro, w_impreso);
        COMMIT;
END nuevoLibro;

CREATE OR REPLACE PROCEDURE nuevaRelAutorImpreso(
    w_id_autor IN relAutorImpreso.id_autor%TYPE,
    w_id_impreso IN relAutorImpreso.id_impreso%TYPE)
    IS
    BEGIN
        INSERT INTO relAutorImpreso(id_autor,id_impreso) VALUES (w_id_autor, w_id_impreso);
        COMMIT;
END nuevaRelAutorImpreso;

CREATE OR REPLACE PROCEDURE nuevaLocalizacion(
    w_nombre IN localizaciones.nombre%TYPE,
    w_correo IN localizaciones.correo%TYPE)
    IS
    BEGIN
        INSERT INTO localizaciones(id_localizacion,nombre,correo) VALUES (sec_ids.NEXTVAL,w_nombre,w_correo);
        COMMIT;
END nuevaLocalizacion;

CREATE OR REPLACE PROCEDURE nuevaRelProductLocaliz(
    w_id_producto IN relProductosLocalizaciones.id_producto%TYPE,
    w_id_localizacion IN relProductosLocalizaciones.id_localizacion%TYPE)
    IS
    BEGIN
        INSERT INTO relProductosLocalizaciones(id_producto,id_localizacion) VALUES (w_id_producto,w_id_localizacion);
        COMMIT;
END nuevaRelProductLocaliz;

CREATE OR REPLACE PROCEDURE nuevoEvento(
    w_nombre IN eventos.nombre%TYPE,
    w_fecha IN eventos.fecha%TYPE,
    w_duracion IN eventos.duracion%TYPE,
    w_precioEntrada IN eventos.precioEntrada%TYPE,
    w_sitiosVip IN eventos.sitiosVip%TYPE)
        IS
    BEGIN
        INSERT INTO eventos(id_evento,nombre,fecha,duracion,precioEntrada,sitiosVip) VALUES (sec_ids.NEXTVAL,w_nombre,w_fecha,w_duracion,w_precioEntrada,w_sitiosVip);
        COMMIT;
END nuevoEvento;

CREATE OR REPLACE PROCEDURE nuevaWeb(
    w_id_localizacion IN webs.id_localizacion%TYPE,
    w_dominio IN webs.dominio%TYPE)
    IS
    BEGIN
        INSERT INTO webs(id_web,id_localizacion,dominio) VALUES (sec_ids.NEXTVAL,w_id_localizacion,w_dominio);
        COMMIT;
END nuevaWeb;

CREATE OR REPLACE PROCEDURE nuevoLugarFisico(
    w_id_localizacion IN lugaresFisicos.id_localizacion%TYPE,
    w_direccion IN lugaresFisicos.direccion%TYPE,
    w_telefono IN lugaresFisicos.telefono%TYPE,
    w_fax IN lugaresFisicos.fax%TYPE)
    IS
    BEGIN
        INSERT INTO lugaresFisicos(id_lugarFisico,id_localizacion,direccion,telefono,fax) VALUES (sec_ids.NEXTVAL,w_id_localizacion,w_direccion,w_telefono,w_fax);
        COMMIT;
END nuevoLugarFisico;

CREATE OR REPLACE PROCEDURE nuevoLugarEventos(
    w_id_lugarFisico IN lugaresEventos.id_lugarFisico%TYPE,
    w_aforo IN lugaresEventos.aforo%TYPE,
    w_id_evento IN lugaresEventos.id_evento%TYPE)
    IS
    BEGIN
        INSERT INTO lugaresEventos(id_lugarEvento,id_lugarFisico,aforo, id_evento) VALUES (sec_ids.NEXTVAL,w_id_lugarFisico,w_aforo, w_id_evento);
        COMMIT;
END nuevoLugarEventos;

CREATE OR REPLACE PROCEDURE nuevoAlmacen(
    w_id_lugarFisico IN almacenes.id_lugarFisico%TYPE)
    IS
    BEGIN
            INSERT INTO almacenes(id_almacen,id_lugarFisico) VALUES (sec_ids.NEXTVAL,w_id_lugarFisico);
            COMMIT;
END nuevoAlmacen;

CREATE OR REPLACE PROCEDURE nuevoStockAlmacen( 
    w_id_almacen IN stockAlmacenes.id_almacen%TYPE,
    w_id_producto IN stockAlmacenes.id_producto%TYPE,
    w_numero IN stockAlmacenes.numero%TYPE,
    w_ubicacionProducto IN stockAlmacenes.ubicacionProducto%TYPE)
    IS
    BEGIN
        INSERT INTO stockAlmacenes(id_almacen,id_producto,numero,ubicacionProducto) VALUES (w_id_almacen,w_id_producto,w_numero,w_ubicacionProducto);
        COMMIT;
END nuevoStockAlmacen;

CREATE OR REPLACE PROCEDURE nuevaTienda(
    w_id_lugarFisico IN tiendas.id_lugarFisico%TYPE,
    w_horario IN tiendas.horario%TYPE)
    IS
    BEGIN
        INSERT INTO tiendas(id_tienda,id_lugarFisico,horario) VALUES (sec_ids.NEXTVAL,w_id_lugarFisico,w_horario);
        COMMIT;
END nuevaTienda;

CREATE OR REPLACE PROCEDURE nuevoStockTienda( 
    w_id_tienda IN stockTiendas.id_tienda%TYPE,
    w_id_producto IN stockTiendas.id_producto%TYPE,
    w_cantidad IN stockTiendas.cantidad%TYPE)
    IS
    BEGIN
        INSERT INTO stockTiendas(id_tienda,id_producto,cantidad) VALUES (w_id_tienda,w_id_producto,w_cantidad);
        COMMIT;
END nuevoStockTienda;

CREATE OR REPLACE PROCEDURE nuevoSocio(
    w_nombre IN socios.nombre%TYPE,
    w_sexo IN socios.sexo%TYPE,
    w_edad IN socios.edad%TYPE,
    w_telefono IN socios.telefono%TYPE,
    w_correo IN socios.correo%TYPE,
    w_direccion IN socios.direccion%TYPE,
    w_vip IN socios.vip%TYPE,
    w_fechaIngreso IN socios.fechaIngreso%TYPE,
    w_cantidadGastada IN socios.cantidadGastada%TYPE,
    w_fechaFinSancion IN socios.fechaFinSancion%TYPE,
    w_fechaNacimiento IN socios.fechaNacimiento%TYPE)
    IS
    BEGIN
        INSERT INTO socios(numeroSocio,nombre,sexo,edad,telefono,correo,direccion,vip,fechaIngreso,cantidadGastada,fechaFinSancion,fechaNacimiento) VALUES (sec_numeroSocio.NEXTVAL, w_nombre,w_sexo,w_edad,w_telefono,w_correo,w_direccion,w_vip,w_fechaIngreso,w_cantidadGastada,w_fechaFinSancion, w_fechaNacimiento);
        COMMIT;
END nuevoSocio;

CREATE OR REPLACE PROCEDURE nuevaRelEventosSocios(
    w_id_evento IN relEventosSocios.id_evento%TYPE,
    w_numeroSocio IN relEventosSocios.numeroSocio%TYPE)
    IS
    BEGIN
        INSERT INTO relEventosSocios(id_evento,numeroSocio) VALUES (w_id_evento,w_numeroSocio);
        COMMIT;
END nuevaRelEventosSocios;

CREATE OR REPLACE PROCEDURE nuevoProveedor(
    w_nombre IN proveedores.nombre%TYPE,
    w_diaReparto IN proveedores.diaReparto%TYPE,
    w_direccion IN proveedores.direccion%TYPE,
    w_telefono IN proveedores.telefono%TYPE,
    w_fax IN proveedores.fax%TYPE,
    w_correo IN proveedores.correo%TYPE,
    w_personaDeContacto IN proveedores.personaDeContacto%TYPE)
    IS
    BEGIN
        INSERT INTO proveedores(id_proveedor,nombre,diaReparto,direccion,telefono,fax,correo,personaDeContacto) VALUES (sec_ids.NEXTVAL,w_nombre,w_diaReparto,w_direccion,w_telefono,w_fax,w_correo,w_personaDeContacto);
        COMMIT;
END nuevoProveedor;

CREATE OR REPLACE PROCEDURE nuevoPedido(
    w_fecha IN pedidos.fecha%TYPE,
    w_satisfecho IN pedidos.satisfecho%TYPE,
    w_id_proveedor IN pedidos.id_proveedor%TYPE)
    IS
    BEGIN
        INSERT INTO pedidos(numeroPedido,fecha,satisfecho,id_proveedor) VALUES (sec_numeroPedido.NEXTVAL, w_fecha, w_satisfecho, w_id_proveedor);
        COMMIT;
END nuevoPedido;

CREATE OR REPLACE PROCEDURE nuevaLineaPedido(
    w_numeroPedido IN lineasPedidos.numeroPedido%TYPE,
    w_id_producto IN lineasPedidos.id_producto%TYPE,
    w_cantidad IN lineasPedidos.cantidad%TYPE)
    IS
    BEGIN
        INSERT INTO lineasPedidos(numeroPedido,id_producto,cantidad) VALUES (w_numeroPedido,w_id_producto,w_cantidad);
        COMMIT;
END nuevaLineaPedido;

--Metodos para los requisitos de informacion

CREATE OR REPLACE VIEW autoresPorSexo AS
    SELECT nombre, nacionalidad, rol FROM autores ORDER BY sexo, id_autor;
CREATE OR REPLACE VIEW autoresPorNacionalidad AS
    SELECT nombre, nacionalidad, rol FROM autores ORDER BY nacionalidad, id_autor;
CREATE OR REPLACE VIEW autoresPorRol AS
    SELECT nombre, nacionalidad, rol FROM autores ORDER BY rol, id_autor;

CREATE OR REPLACE VIEW productosPorPrecio AS
    SELECT nombre, precio, edadRecomendada FROM productos ORDER BY precio, id_producto;
CREATE OR REPLACE VIEW productosPorEdad AS
    SELECT nombre, precio, edadRecomendada FROM productos ORDER BY edadRecomendada, id_producto;

CREATE OR REPLACE VIEW eventosPorFecha AS
    SELECT nombre, fecha, duracion, precioEntrada, sitiosVip FROM eventos ORDER BY fecha, id_evento;
CREATE OR REPLACE VIEW eventosPorPrecio AS
    SELECT nombre, fecha, duracion, precioEntrada, sitiosVip FROM eventos ORDER BY precioEntrada, id_evento;

CREATE OR REPLACE VIEW sociosPorSexo AS
    SELECT numeroSocio, nombre, sexo, edad, telefono, correo, direccion, vip, fechaIngreso, cantidadGastada, fechaFinSancion, fechaNacimiento FROM socios ORDER BY sexo, numeroSocio;
CREATE OR REPLACE VIEW sociosPorEdad AS
    SELECT numeroSocio, nombre, sexo, edad, telefono, correo, direccion, vip, fechaIngreso, cantidadGastada, fechaFinSancion, fechaNacimiento FROM socios ORDER BY edad, numeroSocio;
CREATE OR REPLACE VIEW sociosPorFecha AS
    SELECT numeroSocio, nombre, sexo, edad, telefono, correo, direccion, vip, fechaIngreso, cantidadGastada, fechaFinSancion, fechaNacimiento FROM socios ORDER BY fechaNacimiento, numeroSocio;
CREATE OR REPLACE VIEW sociosPorIngreso AS
    SELECT numeroSocio, nombre, sexo, edad, telefono, correo, direccion, vip, fechaIngreso, cantidadGastada, fechaFinSancion, fechaNacimiento FROM socios ORDER BY fechaIngreso, numeroSocio;

--Cursor que devuelve los socios cuyo aniversario es la fecha actual

DECLARE CURSOR aniversarioSocios
    IS
        SELECT nombre, correo FROM socios WHERE fechaIngreso = SYSDATE;
    BEGIN
        FOR fila IN aniversarioSocios LOOP
            EXIT WHEN aniversarioSocios%NOTFOUND;
            DBMS_OUTPUT.PUT_LINE(fila.nombre+'-'+fila.correo);
        END LOOP;
        
    END;

--Metodos para obtener las claves primarias a partir de otros datos

CREATE OR REPLACE FUNCTION getIdAutor(
    w_nombre IN autores.nombre%TYPE,
    w_rol IN autores.rol%TYPE)
    RETURN INTEGER
    IS 
        w_id_autor autores.id_autor%TYPE;
    BEGIN
        SELECT id_autor INTO w_id_autor FROM autores WHERE nombre= w_nombre AND rol= w_rol;
        RETURN w_id_autor;
END getIdAutor;

CREATE OR REPLACE FUNCTION getIdPersonaje(
    w_nombre IN personajes.nombre%TYPE)
    RETURN INTEGER
    IS 
        w_id_personaje personajes.id_personaje%TYPE;
    BEGIN
        SELECT id_personaje    INTO w_id_personaje FROM personajes WHERE nombre= w_nombre;
        RETURN w_id_personaje;
END getIdPersonaje;

CREATE OR REPLACE FUNCTION getIdProducto(
    w_nombre IN productos.nombre%TYPE)
    RETURN INTEGER
    IS 
        w_id_producto productos.id_producto%TYPE;
    BEGIN
        SELECT id_producto INTO w_id_producto FROM productos WHERE nombre=w_nombre;
        RETURN w_id_producto;
END getIdProducto;

CREATE OR REPLACE FUNCTION getIdImpreso(
    w_id_producto IN impresos.id_producto%TYPE)
    RETURN INTEGER
    IS
        w_id_impreso impresos.id_impreso%TYPE;
    BEGIN
        SELECT id_impreso INTO w_id_impreso FROM impresos WHERE id_producto=w_id_producto;
        RETURN w_id_impreso;
END getIdImpreso;

CREATE OR REPLACE FUNCTION getIdEvento(
    w_nombre IN eventos.nombre%TYPE,
    w_fecha IN eventos.fecha%TYPE)
    RETURN INTEGER
    IS
	    w_id_evento eventos.id_evento%TYPE;
    BEGIN
	SELECT id_evento INTO w_id_evento FROM eventos WHERE nombre=w_nombre AND fecha=w_fecha;
	RETURN w_id_evento;
END getIdEvento;

CREATE OR REPLACE FUNCTION getIdLocalizacion(
    w_correo IN localizaciones.correo%TYPE)
    RETURN INTEGER
    IS 
        w_id_localizacion localizaciones.id_localizacion%TYPE;
    BEGIN
        SELECT id_localizacion INTO w_id_localizacion FROM localizaciones WHERE correo= w_correo;
        RETURN w_id_localizacion;
END getIdLocalizacion;

CREATE OR REPLACE FUNCTION getIdLugarFisico(
    w_direccion IN lugaresFisicos.direccion%TYPE)
    RETURN INTEGER
    IS 
        w_id_lugarFisico lugaresFisicos.id_lugarFisico%TYPE;
    BEGIN
        SELECT id_lugarFisico INTO w_id_lugarFisico FROM lugaresfisicos WHERE direccion= w_direccion;
        RETURN w_id_lugarFisico;
END getIdLugarFisico;

CREATE OR REPLACE FUNCTION getIdAlmacen(
    w_direccion IN lugaresFisicos.direccion%TYPE)
    RETURN INTEGER
    IS 
        w_id_almacen almacenes.id_almacen%TYPE;
        w_id_lugarFisico lugaresFisicos.id_lugarFisico%TYPE;
    BEGIN
        SELECT id_lugarFisico INTO w_id_lugarFisico FROM lugaresFisicos WHERE direccion=w_direccion;
        SELECT id_almacen INTO w_id_almacen FROM almacenes WHERE id_lugarFisico=w_id_lugarFisico;
        RETURN w_id_almacen;
END getIdAlmacen;

CREATE OR REPLACE FUNCTION getIdTienda(
    w_direccion IN lugaresFisicos.direccion%TYPE)
    RETURN INTEGER
    IS
        w_id_tienda tiendas.id_tienda%TYPE;
        w_id_lugarFisico lugaresFisicos.id_lugarFisico%TYPE;
    BEGIN
        SELECT id_lugarFisico INTO w_id_lugarFisico FROM lugaresFisicos WHERE direccion = w_direccion;
        SELECT id_tienda INTO w_id_tienda FROM tiendas WHERE id_lugarFisico= w_id_lugarFisico;
        RETURN w_id_tienda;
END getIdTienda;

CREATE OR REPLACE FUNCTION getNumeroSocio(
    w_nombre IN socios.nombre%TYPE,
    w_telefono IN socios.telefono%TYPE)
    RETURN INTEGER
    IS 
        w_numeroSocio socios.numeroSocio%TYPE;
    BEGIN
        SELECT numeroSocio    INTO w_numeroSocio FROM socios WHERE nombre=w_nombre AND telefono=w_telefono;
        RETURN w_numeroSocio;
END getNumeroSocio;

CREATE OR REPLACE FUNCTION getIdProveedor(
    w_nombre IN proveedores.nombre%TYPE)
    RETURN INTEGER
    IS 
        w_id_proveedor proveedores.id_proveedor%TYPE;
    BEGIN
        SELECT id_proveedor INTO w_id_proveedor FROM proveedores WHERE nombre= w_nombre;
        RETURN w_id_proveedor;
END getIdProveedor;

CREATE OR REPLACE FUNCTION getNumeroPedido(
    w_nombre IN proveedores.nombre%TYPE,
    w_fecha IN pedidos.fecha%TYPE)
    RETURN INTEGER
    IS 
        w_numeroPedido pedidos.numeroPedido%TYPE; 
        w_id_proveedor proveedores.id_proveedor%TYPE;
    BEGIN
        SELECT id_proveedor INTO w_id_proveedor FROM proveedores WHERE nombre=w_nombre;
        SELECT numeroPedido INTO w_numeroPedido FROM pedidos WHERE fecha= w_fecha AND id_proveedor= w_id_proveedor;
        RETURN w_numeroPedido;
END getNumeroPedido;

--Inserciones en la base de datos utilizando los metodos

-- Autor
EXECUTE nuevoAutor ('Charles Xavier', 'masculino', 'ingles', 'grafista');
EXECUTE nuevoAutor ('Andrea Fuentes', 'femenino', 'español', 'guionista');
EXECUTE nuevoAutor ('Arthur Conan Doyle', 'masculino', 'escoces', 'guionista');
EXECUTE nuevoAutor ('Homero', 'masculino', 'griego', 'guionista');

-- Coleccion
EXECUTE nuevaColeccion ('El sorprendente Spiderman', 3);

-- Personaje
EXECUTE nuevoPersonaje ('Peter Parker', 'SpiderMan');
EXECUTE nuevoPersonaje ('Sherlock Holmes', null);

-- Productos 
EXECUTE nuevoProducto ('Spiderman1',15,7);
EXECUTE nuevoProducto ('Spiderman2',15,7);
EXECUTE nuevoProducto ('Figura peter parker',12,7);
EXECUTE nuevoProducto ('Estudio en escarlata',20,13);
EXECUTE nuevoProducto ('La iliada',30,13);

-- RelColeccionProducto
EXECUTE nuevaRelColeccionProducto ('El sorprendente Spiderman', getIdProducto('Spiderman1'));
EXECUTE nuevaRelColeccionProducto ('El sorprendente Spiderman', getIdProducto('Spiderman2'));
EXECUTE nuevaRelColeccionProducto ('El sorprendente Spiderman', getIdProducto('Figura peter parker'));

-- Rel personaje producto
EXECUTE nuevaRelPersonajeProducto (getIdPersonaje('Peter Parker'), getIdProducto('Spiderman1'));
EXECUTE nuevaRelPersonajeProducto (getIdPersonaje('Peter Parker'), getIdProducto('Spiderman2'));
EXECUTE nuevaRelPersonajeProducto (getIdPersonaje('Peter Parker'), getIdProducto('Figura peter parker'));
EXECUTE nuevaRelPersonajeProducto (getIdPersonaje('Sherlock Holmes'), getIdProducto('Estudio en escarlata'));
                                                                                                                                                                                                                                                                                                                        
-- Merchandising
EXECUTE nuevoMerchandising ('Marvel', getIdProducto('Figura peter parker'));

-- Impreso
EXECUTE nuevoImpreso ('Cantaro', 8, getIdProducto('Estudio en escarlata'));
EXECUTE nuevoImpreso ('Gredos', 4, getIdProducto('La iliada'));
EXECUTE nuevoImpreso ('Panini', 5, getIdProducto('Spiderman1'));
EXECUTE nuevoImpreso ('Panini', 6, getIdProducto('Spiderman2'));

-- Comic
EXECUTE nuevoComic ('tomo','heroico', getIdImpreso(getIdProducto('Spiderman1')));
EXECUTE nuevoComic ('tomo', 'heroico',getIdImpreso(getIdProducto('Spiderman2')));

-- Libro
EXECUTE nuevoLibro ('bolsillo', 'novelaPolicial', getIdImpreso(getIdProducto('Estudio en escarlata')));
EXECUTE nuevoLibro ('tapaDura', 'poesia', getIdImpreso(getIdProducto('La iliada')));

-- RelAutorImpreso
EXECUTE nuevaRelAutorImpreso (getIdAutor('Charles Xavier','grafista'), getIdImpreso(getIdProducto('Spiderman1')));
EXECUTE nuevaRelAutorImpreso (getIdAutor('Andrea Fuentes', 'guionista'), getIdImpreso(getIdProducto('Spiderman2')));
EXECUTE nuevaRelAutorImpreso (getIdAutor('Arthur Conan Doyle', 'guionista'), getIdImpreso(getIdProducto('Estudio en escarlata')));
EXECUTE nuevaRelAutorImpreso (getIdAutor('Homero', 'guionista'), getIdImpreso(getIdProducto('La iliada')));

-- Evento 
EXECUTE nuevoEvento ('Firma de libros','16-09-2012',24,5,10);

-- Localizaciones
EXECUTE nuevaLocalizacion ('Pagina web','paginaweb@unlibromas.com');
EXECUTE nuevaLocalizacion ('Tienda Los Naranjos','tiendalosnaranjos@unlibromas.com');
EXECUTE nuevaLocalizacion ('Almacen Los Naranjos','almacenlosnaranjos@unlibromas.com');

-- Rel producto localizaciones
EXECUTE nuevaRelProductLocaliz (getIdProducto('Spiderman1'),getIdLocalizacion('tiendalosnaranjos@unlibromas.com'));
EXECUTE nuevaRelProductLocaliz (getIdProducto('Spiderman1'),getIdLocalizacion('almacenlosnaranjos@unlibromas.com'));
EXECUTE nuevaRelProductLocaliz (getIdProducto('Spiderman2'),getIdLocalizacion('tiendalosnaranjos@unlibromas.com'));
EXECUTE nuevaRelProductLocaliz (getIdProducto('Spiderman2'),getIdLocalizacion('almacenlosnaranjos@unlibromas.com'));
EXECUTE nuevaRelProductLocaliz (getIdProducto('Figura peter parker'),getIdLocalizacion('tiendalosnaranjos@unlibromas.com'));
EXECUTE nuevaRelProductLocaliz (getIdProducto('Figura peter parker'),getIdLocalizacion('almacenlosnaranjos@unlibromas.com'));
EXECUTE nuevaRelProductLocaliz (getIdProducto('Estudio en escarlata'),getIdLocalizacion('tiendalosnaranjos@unlibromas.com'));
EXECUTE nuevaRelProductLocaliz (getIdProducto('Estudio en escarlata'),getIdLocalizacion('almacenlosnaranjos@unlibromas.com'));
EXECUTE nuevaRelProductLocaliz (getIdProducto('La iliada'),getIdLocalizacion('tiendalosnaranjos@unlibromas.com'));
EXECUTE nuevaRelProductLocaliz (getIdProducto('La iliada'),getIdLocalizacion('almacenlosnaranjos@unlibromas.com'));

-- Web
EXECUTE nuevaWeb (getIdLocalizacion('paginaweb@unlibromas.com'),'www.1libromas.com');

-- Lugar fisico
EXECUTE nuevoLugarFisico (getIdLocalizacion('paginaweb@unlibromas.com'),'Calle Los Naranjos nº 14, Sevilla',954768544,954333242); 
EXECUTE nuevoLugarFisico (getIdLocalizacion('paginaweb@unlibromas.com'),'Calle Los Naranjos nº 15, Sevilla',954768545,954333243);

-- Lugar evento
EXECUTE nuevoLugarEventos (getIdLugarFisico('Calle Los Naranjos nº 15, Sevilla'),300, getIdEvento('Firma de libros','16-09-2012'));

-- Almacen
EXECUTE nuevoAlmacen (getIdLugarFisico('Calle Los Naranjos nº 14, Sevilla'));

-- Stockalmacen
EXECUTE nuevoStockAlmacen (getIdAlmacen('Calle Los Naranjos nº 14, Sevilla'),getIdProducto('Spiderman1'),5,'Pasillo 1');
EXECUTE nuevoStockAlmacen (getIdAlmacen('Calle Los Naranjos nº 14, Sevilla'),getIdProducto('Spiderman2'),3,'Pasillo 1');
EXECUTE nuevoStockAlmacen (getIdAlmacen('Calle Los Naranjos nº 14, Sevilla'),getIdProducto('Figura peter parker'),4,'Pasillo 3');
EXECUTE nuevoStockAlmacen (getIdAlmacen('Calle Los Naranjos nº 14, Sevilla'),getIdProducto('Estudio en escarlata'),5,'Pasillo 2');
EXECUTE nuevoStockAlmacen (getIdAlmacen('Calle Los Naranjos nº 14, Sevilla'),getIdProducto('La iliada'),4,'Pasillo 2');

-- Tienda
EXECUTE nuevaTienda (getIdLugarFisico('Calle Los Naranjos nº 15, Sevilla'),'De Lunes a sabado de 10 a 22');

-- Stock tienda 
EXECUTE nuevoStockTienda (getIdTienda('Calle Los Naranjos nº 15, Sevilla'),getIdProducto('Spiderman1'),5);
EXECUTE nuevoStockTienda (getIdTienda('Calle Los Naranjos nº 15, Sevilla'),getIdProducto('Spiderman2'),3);
EXECUTE nuevoStockTienda (getIdTienda('Calle Los Naranjos nº 15, Sevilla'),getIdProducto('Figura peter parker'),4);
EXECUTE nuevoStockTienda (getIdTienda('Calle Los Naranjos nº 15, Sevilla'),getIdProducto('Estudio en escarlata'),5);
EXECUTE nuevoStockTienda (getIdTienda('Calle Los Naranjos nº 15, Sevilla'),getIdProducto('La iliada'),4);

-- Socios
EXECUTE nuevoSocio ('Manuel Fernandez', 'masculino', 23, 954634823, 'manufer89@hotmail.com', 'Calle Los Rodeos nº 2, Sevilla', 'Y', '12-03-2005', 243.75,  null, '09-11-1989'); 
EXECUTE nuevoSocio ('Mirian Benitez', 'femenino', 26, 954394211, 'miriben86@hotmail.com', 'Calle Eduardo Dato nº 13, Sevilla', 'N', '07-06-2002', 243.90, null, '07-05-1986');

-- RelEventoSocio
EXECUTE nuevaRelEventosSocios (getIdEvento('Firma de libros','16-09-2012'),getNumeroSocio('Manuel Fernandez',954634823));

-- Proveedor
EXECUTE nuevoProveedor('Panini','lunes','Calle la Mayor 3, Madrid', 951543621, 951543621, 'atencionalcliente@panini.com','Enrique Grodillo')

-- Pedido
EXECUTE nuevoPedido('10-06-2012','N', getIdProveedor('Panini'));

-- Linea Pedido
EXECUTE nuevaLineaPedido (getNumeroPedido('Panini', '10-06-2012'),getIdProducto('Spiderman2'),5);





















