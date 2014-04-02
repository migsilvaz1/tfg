<?php
	if(empty($_GET['cod'])){
		header("Location: ../error.php");
		exit;
	}
	include '../BDConexion.php';
	include 'gestionSocios.php';
?>
<html>
	<head>
		<title>Modificar Socio</title>
		<LINK REL=StyleSheet HREF="modificar.css" TYPE="text/css" MEDIA=screen>
		<script type="text/javascript">
			function procesar() {
				  var ctrl = new Array(document.getElementsByName("nombre")[0].value, document.getElementsByName("edad")[0].value, document.getElementsByName("telefono")[0].value, 
				  document.getElementsByName("correo")[0].value, document.getElementsByName("direccion")[0].value, document.getElementsByName("fechanac")[0].value, document.getElementsByName("fechain")[0].value);
				  var check = false;
				  var sel = false;
				  for(var i=0; i<ctrl.length; i++){
				  	if(ctrl[i] =="")check = true;
				  }
				  var aRadios = document.getElementsByName("sexo");
                 for( var contador=0; contador < aRadios.length; contador++ ){
                     if(aRadios[contador].checked == true)sel = true;
                 }
				  if(check || !sel){
				  	alert("No puede haber datos en blanco.");
				  	return false;
				  }
				  var numero = document.getElementsByName("numero")[0].value;
				  var edad = document.getElementsByName("edad")[0].value;
				  var telefono = document.getElementsByName("telefono")[0].value;
				  if(isNaN(numero)){
				  	alert("El número de socio debe ser un número entero.");
				  	return false;
				  }
				  if(isNaN(edad)){
				  	alert("La edad debe ser un número entero.");
				  	return false;
				  }
				  if((isNaN(telefono)) || (telefono.length != 9)){
				  	alert("El telefono debe ser un número entero de 9 cifras.");
				  	return false;
				  }
				  var fechanac = document.getElementsByName("fechanac")[0].value;
				  var fechain = document.getElementsByName("fechain")[0].value;
				  var fechafs = document.getElementsByName("fechafs")[0].value;
				  var patronFecha = /^\d{1,2}\/\d{1,2}\/\d{2,4}$/;
				  if(patronFecha.test(fechanac)==false){
				  	alert("El formato de la fecha de nacimiento es erroneo.Debe ser DD/MM/AAAA .");
				  	return false;
				  }
				  if(patronFecha.test(fechain)==false){
				  	alert("El formato de la fecha de ingreso es erroneo.Debe ser DD/MM/AAAA .");
				  	return false;
				  }
				  if((patronFecha.test(fechafs)==false) && (fechafs!="")){
				  	alert("El formato de la fecha de fin de sanción es erroneo.Debe ser DD/MM/AAAA .");
				  	return false;
				  }
				  var correo document.getElementsByName("correo")[0].value;
				  var patronCorreo = /[\w-\.]{3,}@([\w-]{2,}\.)*([\w-]{2,}\.)[\w-]{2,4}/;
				  if(patronCorreo.test(correo)==false){
				  	alert("No es una dirección de correo electónico válida.");
				  	return false;
				  }
				}
		</script>
	</head>
	<body>
		<?php 
			$con = conectar();
			if(empty($_REQUEST['numero'])){
				$socio = consultarUnSocio($con, $_GET['cod']);
		?>
		<div id="texto"><p>Modifique los datos: </p></div>
		<form id="datos" method="post" onsubmit="return procesar()">
			<div id="envoltura">
				<div id="contenido">
					<div id="grupo1">
			<label>Numero de socio:</label><div id="numero"><input name="numero" type="text" value="<?php echo $socio['NUMEROSOCIO']; ?>" /></div>
			<label>Nombre completo:</label><div id="nombre"><input name="nombre" type="text" value="<?php echo $socio['NOMBRE']; ?>" /></div>
			<label>Sexo:</label><div id="sexo"><div id="masculino"><input name="sexo" type="radio" value="masculino" <?php if($socio['SEXO'] == 'masculino')echo "checked=''";	?> />Masculino</div>
			<div id="femenino"><input name="sexo" type="radio" value="femenino" <?php if($socio['SEXO'] == 'femenino')echo "checked=''";	?> />Femenino</div></div>
					</div>
					<div id="grupo2">
			<label>Edad:</label><div id="edad"><input name="edad" type="text" value="<?php echo $socio['EDAD']; ?>" /></div>
			<label>Tel&eacute;fono:</label><div id="telefono"><input name="telefono" type="text" value="<?php echo $socio['TELEFONO']; ?>" /></div>
			<label>Correo electr&oacute;nico:</label><div id="correo"><input name="correo" type="text" value="<?php echo $socio['CORREO']; ?>" /></div>
			<label>Socio VIP:</label><div id="vip"><input name="vip" type="checkbox" <?php if($socio['VIP'] == 'Y')echo "checked=''";?> /></div>
					</div>
					<div id="grupo3">
			<label>Direcci&oacute;n:</label><div id="direccion"><input name="direccion" type="text" value="<?php echo $socio['DIRECCION']; ?>" /></div>	
			<label id="fnac">Fecha de nacimiento:</label><div id="fechaNacimiento"><input name="fechanac" type="text" value="<?php echo $socio['FECHANACIMIENTO']; ?>" /></div>
			<label>Fecha de ingreso como socio:</label><div id="fechaIngreso"><input name="fechain" type="text" value="<?php echo $socio['FECHAINGRESO']; ?>" /></div>
			<label>Fecha de fin de sancion (opcional):</label><div id="fechaFinSancion"><input name="fechafs" type="text" <?php 
			if($socio['FECHAFINSANCION']!=NULL){
				$fecha = $socio['FECHAFINSANCION'];
				echo "value='$fecha'"; 
			}?> /></div>
			</div>
			</div>
			</div>
			<div id="botones">
			<div id="limpiar"><input type="reset" value="Limpiar" /></div>
			<div id="crear"><input type="submit" value="Modificar" /></div>
			</div>
		</form>
		<?php
			}else{
				$numero = (integer)$_REQUEST['numero'];
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
				modificarSocio($con, $numero, $nombre, $sexo, $edad, $telefono, $correo, $dir, $vip, $fechaIn, $finSan, $fnaci);
				desconectar($con);
				if(isset($numero)){
					header("Location: modificar.php?cod=$numero");
				}else{
					header("Location: ../error.php");
					exit;
				}
			}
		?>
	</body>
</html>
