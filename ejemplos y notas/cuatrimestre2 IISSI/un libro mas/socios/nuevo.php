<?php
	include '../BDConexion.php';
	include 'gestionSocios.php';
?>
<html>
	<head>
		<title>Crear Nuevo Socio</title>
		<LINK REL=StyleSheet HREF="nuevo.css" TYPE="text/css" MEDIA=screen>
		<script type="text/javascript">
			function procesar() {
				  var patronFecha = /^\d{1,2}\/\d{1,2}\/\d{2,4}$/;
				  var patronCorreo = /[\w-\.]{3,}@([\w-]{2,}\.)*([\w-]{2,}\.)[\w-]{2,4}/;
				  var nombre = document.getElementById("innombre").value;
				  var edad = document.getElementById("inedad").value;
				  var telefono = document.getElementById("intelefono").value;
				  var correo = document.getElementById("incorreo").value;
				  var direccion = document.getElementById("indireccion").value;
				  var nacimiento = document.getElementById("infechanac").value;
				  var ingreso = document.getElementById("infechain").value;
				  var sancion = document.getElementById("infechafs").value;
				  if(nombre == "" || edad == "" || telefono == "" || correo == "" || direccion == "" || nacimiento == "" || ingreso == ""){
				  	alert("No se pueden dejar datos en blanco salvo los indicados.");
				  	return false;
				  }
				  var aRadios = document.getElementsByName("sexo");
                  var activo = false;
                  for( var contador=0; contador < aRadios.length; contador++ ){
                      if(aRadios[contador].checked == true)activo = true;
                  }
                  if(!activo){
                 	 alert("Seleccione un sexo.");
                 	 return false;
                  }
				  if(isNaN(edad)){
				  	alert("La edad debe ser un numero.");
				  	return false;
				  }
				  if(isNaN(telefono) || telefono>999999999){
				  	alert("El telefono debe ser un nuemro de 9 cifras.");
				  	return false;
				  }
				  if(patronFecha.test(nacimiento)==false){
				  	alert("El formato de la fecha de nacimiento es erroneo.Debe ser DD/MM/AAAA .");
				  	return false;
				  }
				  if(patronFecha.test(ingreso)==false){
				  	alert("El formato de la fecha de ingreso es erroneo.Debe ser DD/MM/AAAA .");
				  	return false;
				  }
				  if(patronFecha.test(sancion)==false && sancion!=""){
				  	alert("El formato de la fecha de sancion es erroneo.Debe ser DD/MM/AAAA .");
				  	return false;
				  }
				  if(patronCorreo.test(correo)==false){
				  	alert("El formato de la direccion de correo es erroneo.");
				  	return false;
				  }		  
				}
		</script>
	</head>
	<body>
		<?php 
			if(!isset($_REQUEST['nombre'])){
		?>
		<div id="texto"><p>Datos del socio:</p></div>
		<form id="datos" method="post" onsubmit="return procesar()">
			<div id="envoltura">
				<div id="contenido">
					<div id="grupo1">
			<label>Nombre completo:</label><div id="nombre"><input id="innombre" name="nombre" type="text" /></div>
			<label>Sexo:</label><div id="sexo"><div id="masculino"><input id="insexo" name="sexo" type="radio" value="masculino" />Masculino</div><div id="femenino"><input name="sexo" type="radio" value="femenino" />Femenino</div> </div>
			<label>Edad:</label><div id="edad"><input id="inedad" name="edad" type="text" /></div>
					</div>
					<div id="grupo2">
			<label>Tel&eacute;fono:</label><div id="telefono"><input id="intelefono" name="telefono" type="text" /></div>
			<label>Correo electr&oacute;nico:</label><div id="correo"><input id="incorreo" name="correo" type="text" /></div>
			<label>Direcci&oacute;n:</label><div id="direccion"><input id="indireccion" name="direccion" type="text" /></div>
			<label>Socio VIP:</label><div id="vip"><input id="invip" name="vip" type="checkbox" /></div>
					</div>
					<div id="grupo3">
			<label>Fecha de nacimiento:</label><div id="fechaNacimiento"><input id="infechanac" name="fechanac" type="text" /></div>
			<label>Fecha de ingreso como socio:</label><div id="fechaIngreso"><input id="infechain" name="fechain" type="text" /></div>
			<label>Fecha de fin de sancion (opcional):</label><div id="fechaFinSancion"><input id="infechafs" name="fechafs" type="text" /></div>
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
				$nombre = $_REQUEST['nombre'];
				$sexo = $_REQUEST['sexo'];
				$edad = (integer)$_REQUEST['edad'];
				$telefono = (integer)$_REQUEST['telefono'];
				$correo = $_REQUEST['correo'];
				$dir = $_REQUEST['direccion'];
				$fnaci = $_REQUEST['fechanac'];
				$fechaIn = $_REQUEST['fechain'];
				if(isset($_REQUEST['vip'])){
					$vip = "Y";
				}else{
					$vip = "N";
				}
				if(isset($_REQUEST['fechafs'])){
					$finSan= $_REQUEST['fechafs'];
				}else{
					$finSan = NULL;
				}
				$con = conectar();
				$numSoc = insertarSocio($con, $nombre, $sexo, $edad, $telefono, $correo, $dir, $vip, $fechaIn, $finSan, $fnaci);
				desconectar($con);
				if(isset($numSoc)){
					echo "<div id='textofin'>Se ha creado correctamente el socio nº: $numSoc.</div>";
				}else{
					header("Location: ../error.php");
					exit;
				}
			}
		?>
	</body>
</html>
