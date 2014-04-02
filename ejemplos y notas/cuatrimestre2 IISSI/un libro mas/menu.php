<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
"http://www.w3.org/TR/html4/strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
	<head>
		<title>Menu</title>
		<LINK REL=StyleSheet HREF="estilomenu.css" TYPE="text/css" MEDIA=screen>
	</head>
	<body>
		<div id="inicio"><a href="bienvenida.php" target="principal"><button><img src="img/home.png" alt="Inicio" /></button></a></div>
		<div id="info"><a href="info.html" target="principal"><button><img src="img/info.png" alt="Inicio" /></button></a></div>
		<div id="menu">
            <ul id="nav">
             <li><span>Productos</span>
                <ul>
                    <li><a href="/aplicacion/productos/nuevo.php" target="principal">Nuevo</a></li>
                    <li><a href="/aplicacion/productos/administrar.php" target="principal">Administrar</a></li>
               </ul>
            </li>
 
            <li><span>Socios</span>
                <ul>
                    <li><a href="/aplicacion/socios/nuevo.php" target="principal">Nuevo</a></li>
                    <li><a href="/aplicacion/socios/administrar.php" target="principal">Administrar</a></li>
               </ul>
            </li>            
            <li><span>Ventas y Reservas</span>
 
                <ul>
                    <li><a href="/aplicacion/ventas/nuevo.php" target="principal">Nueva</a></li>
                    <li><a href="/aplicacion/ventas/administrar.php" target="principal">Administrar</a></li>
               </ul>
            </li>
            <li><span>Eventos</span>
 
                <ul>
                    <li><a href="/aplicacion/eventos/nuevo.php" target="principal">Nuevo</a></li>
                    <li><a href="/aplicacion/eventos/administrar.php" target="principal">Administrar</a></li>
               </ul>
            </li>
        </ul>
 
    </div>
	</body>
</html>
