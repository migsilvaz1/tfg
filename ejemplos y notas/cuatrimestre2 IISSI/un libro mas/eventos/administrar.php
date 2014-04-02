<?php
	include '../BDConexion.php';
	include 'gestionEventos.php';
?>
<html>
	<head>
		<title>Administrar Eventos</title>
		<LINK REL=StyleSheet HREF="administrar.css" TYPE="text/css" MEDIA=screen>
		<script type="text/javascript">
			function procesar() {
				  var nombre = document.getElementsByName("nombre")[0].value;
				  var fecha = document.getElementsByName("fecha")[0].value;
				  if((nombre!="") && (fecha!="")){
				  	alert("No se puede realizar la busqueda por ambos criterios a la vez.");
				  	return false;
				  }
				  var patronFecha = /^\d{1,2}\/\d{1,2}\/\d{2,4}$/;
				  if(fecha!="" && patronFecha.test(fecha)==false){
				  	alert("El formato de la fecha es erroneo.Debe ser DD/MM/AAAA");
				  	return false;
				  }
				  
				}
		</script>
	</head>
	<body>
		<?php 
			if(!isset($_REQUEST['nombre']) || !isset($_REQUEST['fecha'])){
		?>
				<div id="texto"><p>Se puede realizar una b&uacute;squeda de eventos por el nombre o por una fecha. Dejar en blanco para mostraran todos los eventos: </p></div>
				<form id="bpor" method="post" onsubmit="return procesar()">
					<div id="envoltura">
						<div id="contenido">
							<div id="grupo1">
					<label>Nombre del evento:</label><div id="nombre"><input name="nombre" type="text" /></div>
					<label>Fecha del evento:</label><div id="fecha"><input name="fecha" type="text" /></div>
							</div>
						</div>
					</div>
					<div id="buscar"><input type="submit" value="Buscar" /></div>
				</form>
		<?php
			}else{
				$con = conectar();
				if((!empty($_REQUEST['nombre']) || !empty($_REQUEST['fecha'])) && !(empty($_REQUEST['nombre']) && empty($_REQUEST['fecha']))){
					echo "<p id='texto'>Resultados: </p>";
					echo "<table id='tabla'><tr>
							<td>Nombre</td>
							<td>Fecha</td>
							<td>Precio</td>
							<td>Aforo</td>
							<td>Acci&oacute;n</td></tr>";
					if(!empty($_REQUEST['nombre'])){
						$lista = consultarEvento($con, $_REQUEST['nombre']);
					}elseif(!empty($_REQUEST['fecha'])){
						$lista = consPorFecha($con, $_REQUEST['fecha']);
					}
					for($n=0; $n< sizeof($lista); $n++){
						$evento = $lista[$n];
						$codigo = $evento['ID_EVENTO'];
						$nombre = $evento['NOMBRE'];
						$fecha = $evento['FECHA'];
						$precio = $evento['PRECIOENTRADA'];
						$aforo = $evento['AFORO'];
						echo "<tr><td>$nombre</td>
							<td>$fecha</td>
							<td>$precio</td>
							<td>$aforo</td>";
						echo "<td>
							<a href='modificar.php?cod=$codigo'><button><img src='../img/page_edit.png' alt='Modificar' /></button></a>
							<a href='eliminar.php?cod=$codigo'><button><img src='../img/delete.png' alt='Eliminar' /></button></a>
						</td></tr>";
						}
					echo "</table>";
				}elseif(empty($_REQUEST['nombre']) && empty($_REQUEST['fecha'])){
					$innombre = "";
					$lista = consultarEvento($con, $innombre);
					echo "<p id='texto'>Resultados: </p>";
					echo "<table id='tabla'><tr>
							<td>Nombre</td>
							<td>Fecha</td>
							<td>Precio</td>
							<td>Aforo</td>
							<td>Acci&oacute;n</td></tr>";
					for($n=0; $n< sizeof($lista); $n++){
						$evento = $lista[$n];
						$codigo = $evento['ID_EVENTO'];
						$nombre = $evento['NOMBRE'];
						$fecha = $evento['FECHA'];
						$precio = $evento['PRECIOENTRADA'];
						$aforo = $evento['AFORO'];
						echo "<tr><td>$nombre</td>
							<td>$fecha</td>
							<td>$precio</td>
							<td>$aforo</td>";
						echo "<td>
							<a href='modificar.php?cod=$codigo'><button><img src='../img/page_edit.png' alt='Modificar' /></button></a>
							<a href='eliminar.php?cod=$codigo'><button><img src='../img/delete.png' alt='Eliminar' /></button></a>
						</td></tr>";
						}
					echo "</table>";
				}else{
					desconectar($con);
					header("Location: ../error.php");
					exit;
				}
				desconectar($con);
				
			}
		?>
	</body>
</html>
