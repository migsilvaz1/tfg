<?php
	include '../BDConexion.php';
	include 'gestionEventos.php';
?>
<html>
	<head>
		<title>Crear Nuevo Evento</title>
		<LINK REL=StyleSheet HREF="nuevo.css" TYPE="text/css" MEDIA=screen>
		<script type="text/javascript">
			function procesar() {
				  var ctrl = document.getElementsByTagName("input");
				  var check = false;
				  for(var i=0; i<ctrl.length; i++){
				  	if(ctrl[i].value =="")check = true;
				  }
				  if(check){
				  	alert("No puede haber datos en blanco.");
				  	return false;
				  }
				  var fecha = document.getElementsByName("fecha")[0].value;
				  var patronFecha = /^\d{1,2}\/\d{1,2}\/\d{2,4}$/;
				  if(patronFecha.test(fecha)==false){
				  	alert("El formato de la fecha es erroneo.Debe ser DD/MM/AAAA .");
				  	return false;
				  }
				  var hora = document.getElementsByName("hora")[0].value;
				  var patronHora = /^([0-5]\d):([0-5]\d)$/;
				  if(patronHora.test(hora)==false){
				  	alert("El formato de la hora debe ser numerico. Debe ser HH:MM .");
				  	return false;
				  }
				  var duracion = document.getElementsByName("dur")[0].value;
				  if(isNaN(duracion)){
				  	alert("La duracion debe ser un número entero.");
				  	return false;
				  }
				  var precEntrada = document.getElementsByName("precio")[0].value;
				  if(isNaN(precEntrada)){
				  	alert("El precio debe ser un número real.");
				  	return false;
				  }
				  var aforo = document.getElementsByName("aforo")[0].value;
				  if(isNaN(aforo)){
				  	alert("El aforo debe ser un número entero.");
				  	return false;
				  }
				  var sitiosVip = document.getElementsByName("svip")[0].value;
				  if(isNaN(sitiosVip)){
				  	alert("Las plazas vip debe ser un número entero.");
				  	return false;
				  }
				}
		</script>
	</head>
	<body>
		<?php
			if(!isset($_REQUEST['nombre'])){
		?>
				<div id="texto"><p>Itroduzca todos los datos para crear el nuevo evento: </p></div>
				<form id="datos" method="post" onsubmit="return procesar()">
					<div id="envoltura">
						<div id="contenido">
							<div id="grupo1">
					<label>Nombre del evento:</label><div id="nombre"><input name="nombre" type="text" /></div>
					<label>Fecha:</label><div id="fecha"><input name="fecha" type="text" /></div>
					<label>Direcci&oacute;n:</label><div id="direccion"><input name="dir" type="text" /></div>
					<label>Hora de inicio:</label><div id="hora"><input name="hora" type="text" /></div>
							</div>
							<div id="grupo2">
					<label>Duraci&oacute;n en minutos:</label><div id="duracion"><input name="dur" type="text" /></div>
					<label>Precio de la entrada (€):</label><div id="precioEntrada"><input name="precio" type="text" /></div>
					<label>Aforo total:</label><div id="aforo"><input name="aforo" type="text" /></div>
					<label>Plazas para socios Vip:</label><div id="SitiosVip"><input name="svip" type="text" /></div>
							</div>
						</div>
					</div>
					<div id="botones">
					<div id="limpiar"><input type="reset" value="Limpiar" /></div>
					<div id="crear"><input type="submit" value="Crear" /></div>
					</div>
				</form>
				<?php
			}else{
				$nom = $_REQUEST['nombre'];
				$fecha = $_REQUEST['fecha'];
				$dur = (integer)$_REQUEST['dur'];
				$preEnt =(integer) $_REQUEST['precio'];
				$dir = $_REQUEST['dir'];
				$hora =(integer) $_REQUEST['hora'];
				$aforo =(integer) $_REQUEST['aforo'];
				$vip =(integer) $_REQUEST['svip'];
				$con = conectar();
				insertarEvento($con, $nom, $fecha, $dur, $preEnt, $dir, $hora, $aforo, $vip);
				echo "<div id='textofin'>Se ha creado correctamente el evento.</div>";
				desconectar($con);
			}
		?>
	</body>
</html>
