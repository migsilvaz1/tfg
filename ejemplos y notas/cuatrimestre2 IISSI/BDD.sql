CREATE SEQUENCE sec_ids
START WITH 10
INCREMENT BY 1;
--Secuencia para la creacion de numeroSocio
CREATE SEQUENCE sec_nso
START WITH 10
INCREMENT BY 1;

--Secuencia auxiliar
CREATE SEQUENCE sec_aux
START WITH 10
INCREMENT BY 1;


CREATE TABLE productos(
    codigoProducto INTEGER NOT NULL,
    nombre VARCHAR(100),
    precio FLOAT,
    popularidad INTEGER DEFAULT 0,
    edadRecomendada INTEGER,
    personaje VARCHAR(100),
    coleccion VARCHAR(100),
    stock INTEGER,
    PRIMARY KEY(codigoProducto),
    CHECK(precio> 0.0),
    CHECK(popularidad>=0),
    CHECK(edadRecomendada>=0 AND edadRecomendada<100)
);

CREATE TABLE impresos(
    id_impreso INTEGER NOT NULL,
    editorial VARCHAR(100) NOT NULL,
    precioAlquiler FLOAT NOT NULL,
    autor VARCHAR(100),
    codigoProducto INTEGER NOT NULL,
    PRIMARY KEY(id_impreso),
    FOREIGN KEY(codigoProducto) REFERENCES productos(codigoProducto),
    CHECK(precioAlquiler>0.0)
);

CREATE TABLE comics(
    id_comic INTEGER NOT NULL,
    tipoComic VARCHAR(20),
    generoComic VARCHAR(20),
    id_impreso INTEGER NOT NULL,
    PRIMARY KEY(id_comic),
    FOREIGN KEY(id_impreso) REFERENCES impresos(id_impreso),
    CHECK(tipoComic = 'grapa' OR tipoComic = 'tomo'),
    CHECK(generoComic = 'manga' OR generoComic = 'vinetas'OR generoComic = 'heroico')
);

CREATE TABLE libros(
    id_libro INTEGER NOT NULL,
    tipoLibro VARCHAR(20),
    generoLibro VARCHAR(20),
    id_impreso INTEGER NOT NULL,
    PRIMARY KEY(id_libro),
    FOREIGN KEY(id_impreso) REFERENCES impresos(id_impreso),
    CHECK(tipoLibro='bolsillo' OR tipoLibro='tapaDura' OR tipoLibro='tapaBlanda'),
    CHECK(generoLibro='aventura' OR generoLibro='cienciaFiccion' OR generoLibro='clasicos' OR generoLibro='cuentos' OR generoLibro='ensayos' OR generoLibro='novelaNarrativa' OR generoLibro='novelaPolicial' OR generoLibro='novelaHistorica' OR generoLibro='poesia' OR generoLibro='teatro' OR generoLibro='tecnicos' OR generoLibro='infantil')
);

CREATE TABLE merchandising(
    id_merchandising INTEGER NOT NULL,
    marca VARCHAR(100),
    codigoProducto INTEGER NOT NULL,
    PRIMARY KEY(id_merchandising),
    FOREIGN KEY(codigoProducto) REFERENCES productos(codigoProducto)
);


--Inserciones
INSERT INTO productos VALUES (1,'Spiderman1',15.95,0,7,'Spiderman','Asombroso Spiderman',3);
INSERT INTO productos VALUES (2,'Spiderman2',15.95,0,7,'Spiderman','Asombroso Spiderman',3);
INSERT INTO productos VALUES (3,'Figura peter parker',12.50,0,7,'Spiderman',NULL,1);
INSERT INTO productos VALUES (4,'Estudio en escarlata',20.00,0,13,NULL,NULL,5);
INSERT INTO productos VALUES (5,'La iliada',30.05,0,13,NULL,NULL,3);
INSERT INTO impresos VALUES (1,'Panini',5.0,'Stan Lee',1);
INSERT INTO comics VALUES(1,'tomo','heroico',1);
INSERT INTO impresos VALUES (2,'Panini',5.0,'Stan Lee',2);
INSERT INTO comics VALUES(2, 'tomo', 'heroico',2);
INSERT INTO impresos VALUES (3,'ABCEdiciones',5.0,'John Smith',4);
INSERT INTO libros VALUES (1,'bolsillo','novelaPolicial',3);
INSERT INTO impresos VALUES (4,'ACEditores',5.0,'Homero',5);
INSERT INTO libros VALUES (2,'tapaDura', 'clasicos',4);
INSERT INTO merchandising VALUES (1,'Marvel',3);



CREATE TABLE eventos(
    id_evento INTEGER NOT NULL,
    nombre VARCHAR(100),
    fecha DATE,
    duracion INTEGER,
    precioEntrada FLOAT,
    direccion VARCHAR(500),
    hora VARCHAR(5),
    aforo INTEGER,
    sitiosVip INTEGER,
    PRIMARY KEY(id_evento),
    CHECK(duracion>0),
    CHECK(precioEntrada>=0.0),
    CHECK(sitiosVIP>-1)
);

CREATE TABLE socios(
    numeroSocio INTEGER NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    sexo VARCHAR(10),
    edad INTEGER,
    telefono INTEGER,
    correo VARCHAR(100),
    direccion VARCHAR(500),
    vip CHAR(1) NOT NULL,
    fechaIngreso DATE,
    fechaFinSancion DATE,
    fechaNacimiento DATE,
    PRIMARY KEY(numeroSocio),
    CHECK(sexo = 'masculino' OR sexo = 'femenino'),
    CHECK(edad>=0),
    CHECK(telefono<1000000000),
    CHECK(vip = 'Y' OR vip = 'N')
);

CREATE TABLE relEveSoc(
    id_evento INTEGER NOT NULL,
    numeroSocio INTEGER NOT NULL,
    PRIMARY KEY(id_evento,numeroSocio),
    FOREIGN KEY(id_evento) REFERENCES eventos(id_evento),
    FOREIGN KEY(numeroSocio) REFERENCES socios(numeroSocio)
);

--inserciones
INSERT INTO socios VALUES (1,'Manuel Fernandez', 'masculino', 23, 954634823, 'manufer89@hotmail.com', 'Calle Los Rodeos n 2, Sevilla', 'Y', '12-3-2005', null,'9-11-1989'); 
INSERT INTO socios VALUES (2,'Mirian Benitez', 'femenino', 26, 954394211, 'miriben86@hotmail.com', 'Calle Eduardo Dato n 13, Sevilla', 'N', '7-6-2002', null, '7-5-1986');
INSERT INTO eventos VALUES (1,'Firma de libros','12-3-2012',40,3.50,'Tienda','18:30',50,0);
INSERT INTO eventos VALUES (2,'Concierto','12-6-2012',120,13.50,'calle falsa 32','19:30',150,20);
INSERT INTO relEveSoc VALUES (1,1);
INSERT INTO relEveSoc VALUES (2,1);
INSERT INTO relEveSoc VALUES (2,2);
------------------------------------------------------------------------------------------------

CREATE TABLE ventas(
    codigoVenta INTEGER NOT NULL,
    numeroSocio INTEGER,
    fechaVenta DATE NOT NULL,
    total FLOAT NOT NULL,
    pagado CHAR(1) NOT NULL,
    PRIMARY KEY(codigoVenta, fechaVenta),
    FOREIGN KEY(numeroSocio)REFERENCES socios(numeroSocio),
    CHECK(pagado = 'Y' OR pagado = 'N')
);

CREATE TABLE lineasVentas(
    codigoVenta INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    codigoProducto INTEGER NOT NULL,
    fechaVenta DATE NOT NULL,
    PRIMARY KEY(codigoVenta, fechaVenta, codigoProducto),
    FOREIGN KEY(codigoVenta, fechaVenta)REFERENCES ventas(codigoVenta, fechaVenta),
    FOREIGN KEY(codigoProducto)REFERENCES productos(codigoProducto)
);

--inserciones
INSERT INTO ventas VALUES(1,1,'17-6-2012',31.9,'Y');
INSERT INTO lineasVentas VALUES(1,1,1,'17-6-2012');
INSERT INTO lineasVentas VALUES(1,1,2,'17-6-2012');
INSERT INTO ventas VALUES(2,NULL,'18-6-2012',20.00,'Y');
INSERT INTO lineasVentas VALUES(2,1,4,'18-6-2012');

