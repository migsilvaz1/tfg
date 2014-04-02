<?php
	if(empty($_GET['cod'])){
		header("Location: ../error.php");
		exit;
	}
	include '../BDConexion.php';
	include 'gestionEventos.php';
	ob_start(); 
?>
<html>
	<head>
		<title>Consultar Evento</title>
		<LINK REL=StyleSheet HREF="modificar.css" TYPE="text/css" MEDIA=screen>
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
				  var patronFecha = /^\n{1,2}\-\n{1,2}\-\n{4}$/;
				  if(patronFecha.test(fecha)==false){
				  	alert("El formato de la fecha es erroneo.Debe ser DD-MM-AAAA .");
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
			$con = conectar();
			$codev = $_GET['cod'];
			$evento = consPorCod($con, $codev);
			if(!isset($_REQUEST['nombre'])){
		?>
				<div id="texto"><p>Puede modificar los datos del evento: </p></div>
				<form id="datos" method="post">
					<div id="envoltura">
						<div id="contenido">
							<div id="grupo1">
					<label>Nombre del evento:</label><div id="nombre"><input name="nombre" type="text" value="<?php echo $evento['NOMBRE']; ?>" /></div>
					<label>Fecha:</label><div id="fecha"><input name="fecha" type="text" value="<?php echo $evento['FECHA']; ?>" /></div>
					<label>Direcci&oacute;n:</label><div id="direccion"><input name="dir" type="text" value="<?php echo $evento['DIRECCION']; ?>" /></div>
							</div>
							<div id="grupo2">
					<label>Hora de inicio:</label><div id="hora"><input name="hora" type="text" value="<?php echo $evento['HORA']; ?>" /></div>
					<label>Duraci&oacute;n en minutos:</label><div id="duracion"><input name="dur" type="text" value="<?php echo $evento['DURACION']; ?>" /></div>
					<label>Precio de la entrada (€):</label><div id="precioEntrada"><input name="precio" type="text" value="<?php echo $evento['PRECIOENTRADA']; ?>" /></div>
							</div>
							<div id="grupo3">
					<label>Aforo total:</label><div id="aforo"><input name="aforo" type="text" value="<?php echo $evento['AFORO']; ?>" /></div>
					<label>Plazas para socios Vip:</label><div id="SitiosVip"><input name="svip" type="text" value="<?php echo $evento['SITIOSVIP']; ?>" /></div>
							</div>
						</div>
					</div>
					<div id="modificar"><input type="submit" value="Modificar" /></div>
				</form>
				<div id="envoltura">
				<div id="apuntados">
		<?php
				$socios = consultarSociosApuntados($con, $evento['NOMBRE']);
				if(!empty($socios)){
					echo "<div id=textomedio1>Socios apuntados al evento:</div>";
					echo "<table id='tabla'><tr>
							<td>N&uacute;mero del Socio</td>
							<td>Nombre del Socio</td>
							<td>Vip</td>
							<td>Telefono</td></tr>";
					for($n=0;$n<sizeof($socios);$n++){
						$socio = $socios[$n];
						$num = $socio['NUMEROSOCIO'];
						$nom = $socio['NOMBRE'];
						$vip = $socio['VIP'];
						$tel = $socio['TELEFONO'];
				?>
				<tr><td><?php echo $num ?></td>
					<td><?php echo $nom ?></td>
					<td><input name='vip' type='checkbox' <?php if($vip == 'Y')echo "checked=''";	?> /></td>
					<td><?php echo $tel ?></td>
				</tr>
				<?php
					}
					echo "</table>";
				}else{
					echo "<div id='textomedio1'>No hay socios apuntados al evento:</div>";
				}
				?>
				</div>
				<div id="fapuntar">
				<div id="textomedio2">Puede apuntar a un socio a este evento, o quitarlo de el:</div>
				<form id="apuntar" method="post">
					<div id="envoltura">
						<div id="contenido">
							<div id="grupo1">
					<label>Introduzca el n&uacute;mero de socio:</label><div id="nsocio"><input name="nsoc" type="text" /></div>
					<label>Seleccione la acci&oacute;n:</label><div id="accion"><input name="accion" type="radio" value="apuntar"/>Apuntar <input name="accion" type="radio" value="quitar" />Quitar </div>
							</div>
						</div>
					</div>
					<div id="aceptar"><input type="submit" value="Aceptar" /></div>
				</form>
				</div>
				</div>
				<?php
			if(isset($_REQUEST['nsoc'])){
				if($_REQUEST['accion'] == "apuntar"){
					apuntarAEvento($con, (integer)$_REQUEST['nsoc'], $codev);
				}elseif($_REQUEST['accion'] == "quitar"){
					quitarDeEvento($con, (integer)$_REQUEST['nsoc'], $codev);
				}
				header("Location:modificar.php?cod=$codev");
			}
			
		}else{
			if(isset($_REQUEST['nombre'])){
				$codev = $_GET['cod'];
				$nom = $_REQUEST['nombre'];
				$fecha = $_REQUEST['fecha'];
				$dur = (integer)$_REQUEST['dur'];
				$preEnt = (integer)$_REQUEST['precio'];
				$dir = $_REQUEST['dir'];
				$hora = (integer)$_REQUEST['hora'];
				$aforo = (integer)$_REQUEST['aforo'];
				$vip = (integer)$_REQUEST['svip'];
				modificarEvento($con, $codev, $nom, $fecha, $dur, $preEnt, $dir, $hora, $aforo, $vip);
				header("Location:modificar.php?cod=$codev");
			}
		}
		desconectar($con);
		?>
	</body>
</html>