<?php
	include '../BDConexion.php';
	include 'gestionVentas.php';
?>
<html>
	<head>
		<title>Nueva Venta</title>
		<LINK REL=StyleSheet HREF="nuevo.css" TYPE="text/css" MEDIA=screen>
		<script type="text/javascript">
			function check() {
				var patronFecha = /^\d{1,2}\/\d{1,2}\/\d{2,4}$/;
				var codigo = document.getElementById("incodigo").value;
				var socio = document.getElementById("insocio").value;
				var fecha = document.getElementById("infecha").value;
                if(codigo == "" || fecha == ""){
				  	alert("Solo el número de socio puede estar en blanco.");
				  	return false;
				}
				var aRadios = document.getElementsByName("pagado");
				var activo = false;
                for( var contador=0; contador < aRadios.length; contador++ ){
                    if(aRadios[contador].checked == true)activo = true;
                }
                if(!activo){
                	alert("Seleccione una opción de pago.");
                 	return false;
                }
				if(isNaN(codigo)) {
					alert("El número de venta debe ser un número entero.");
					return false;
				}
				if(socio != "" && isNaN((socio)) {
					alert("El número de socio debe ser un número entero.");
					return false;
				}
				if(patronFecha.test(fecha) == false) {
					alert("El formato de la fecha es erroneo. Debe ser DD/MM/AAAA.");
					return false;
				}
			}
		</script>
	</head>
	<body>
	<?php 
		if(!isset($_REQUEST['codVen'])){
	?>
			<div id="texto"><p>El formulario permite el registro de ventas y reservas. Una reserva es una venta que no se ha pagado: </p></div>
			<form id="datosVenta" method="post" onsubmit="return check()">
				<div id="envoltura">
					<div id="contenido">
						<div id="grupo1">
				<label>C&oacute;digo:</label><div id="codigo"><input id="incodigo" name="codVen" type="text" /></div>
				<label>Socio (en blanco si no es socio):</label><div id="socio"><input id="insocio" name="numSoc" type="text" /></div>
				<label>Fecha:</label><div id="fecha"><input id="infecha" name="fecha" type="text" /></div>
				<label>¿Pagado?:</label><div id="pagado"><div id="si"><input name="pagado" type="radio" value="Y" />Si</div><div id="no"><input name="pagado" type="radio" value="N" />No</div></div>
						</div>
					</div>
				</div>
				<div id="botones">
				<div id="limpiar"><input type="reset" value="Limpiar" /></div>
				<div id="continuar"><input type="submit" value="Continuar" /></div>
				</div>
			</form>
	<?php
		}else{
			$con = conectar();
			$codVen = (integer)$_REQUEST['codVen'];
			if(empty($_REQUEST['numSoc'])){
				$numSoc = NULL;
			}else{
				$numSoc = $_REQUEST['numSoc'];
			}
			$fecha = $_REQUEST['fecha'];
			$pagado = $_REQUEST['pagado'];
			if(empty($codVen) || empty($fecha) || empty($pagado)){
				desconectar($con);
				header("Location: ../error.php");
				exit;
			}
			crearVenta($con, $codVen, $numSoc, $fecha, $pagado);
			desconectar($con);
			$total = 0.0;
			header("Location: rellenar.php?codigo=$codVen&total=$total");
		}
	?>
	</body>
</html>
