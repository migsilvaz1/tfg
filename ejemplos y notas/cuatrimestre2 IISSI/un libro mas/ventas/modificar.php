<?php
	if(empty($_GET['cod'])){
		header("Location: ../error.php");
		exit;
	}
	include '../BDConexion.php';
	include 'gestionVentas.php';
	include '../productos/gestionProductos.php'
?>
<html>
	<head>
		<title>Modificar Venta</title>
		<LINK REL=StyleSheet HREF="modificar.css" TYPE="text/css" MEDIA=screen>
		<script type="text/javascript">
			function procesar() {
				  var ctrl = new Array(document.getElementsByName("codVen")[0].value, document.getElementsByName("fecha")[0].value);
				  var check = false;
				  var elec = false;
				  for(var i=0; i<ctrl.length; i++){
				  	if(ctrl[i] =="")check = true;
				  }
				  var aRadios = document.getElementsByName("pagado");
                 for( var contador=0; contador < aRadios.length; contador++ ){
                     if(aRadios[contador].checked == true)elec = true;
                 }
				  if(check){
				  	alert("Solo el número de socio puede estar en blanco.");
				  	return false;
				  }
				  if(!elec){
				  	alert("Debe indicar si está pagada o no");
					return false;
					}
					var codVen = document.getElementsByName("codVen")[0].value;
					var numSoc = document.getElementsByName("numSoc")[0].value;
					if(isNaN(parseInt(codVen))) {
						alert("El número de venta debe ser un número entero.");
						return false;
					}
					if(isNaN(numSoc)) {
						alert("El número de socio debe ser un número entero.");
						return false;
					}
					var fecha = document.getElementsByName("fecha")[0].value;
					var patronFecha = /^\d{1,2}\/\d{1,2}\/\d{2,4}$/;
					if(patronFecha.test(fecha) == false) {
							alert("El formato de la fecha es erroneo.Debe ser DD/MM/AAAA .");
							return false;
					}
				}
		</script>
	</head>
	<body>
	<?php 
		$con = conectar();
		if(!isset($_REQUEST['ncodVen'])){
			$codVen = $_GET['cod'];
			$venta = consultarVenta($con, $codVen);
			$total = $venta['TOTAL'];
	?>
			<div id="texto1"><p>Datos de la venta o reserva: </p></div>
			<form id="datosVenta" method="post" onsubmit="return procesar()">
				<div id="envoltura">
					<div id="contenido">
						<div id="grupo1">
				<label>C&oacute;digo:</label><div id="codigo"><input name="ncodVen" type="text" value="<?php echo $venta['CODIGOVENTA']; ?>" /></div>
				<label>Socio (en blanco si no es socio):</label><div id="socio"><input name="numSoc" type="text"value="<?php echo $venta['NUMEROSOCIO']; ?>" /></div>
						</div>
						<div id="grupo2">
				<label>Fecha:</label><div id="fecha"><input name="fecha" type="text"value="<?php echo $venta['FECHAVENTA']; ?>" /></div>
				<label>Total:</label><div id="total"><input name="total" type="text"value="<?php echo $venta['TOTAL']; ?>" /></div>
						</div>
						<div id="grupo3">
				<label>¿Pagado?:</label><div id="pagado"><div id="si"><input name="pagado" type="radio" value="Y"<?php if($venta['PAGADO'] == 'Y')echo "checked=''";	?> />Si</div>
					<div id="no"><input name="pagado" type="radio" value="N"<?php if($venta['PAGADO'] == 'N')echo "checked=''";	?> />No</div></div>
				</div>
				</div>
				</div>
				<div id="botones">
				<div id="limpiar"><input type="reset" value="Limpiar" /></div>
				<div id="continuar"><input type="submit" value="Modificar" /></div>
				</div>
			</form>
			<div id="texto2">Desglose:</div>
	<?php
			$lineas = consultarLineasDeVenta($con, $codVen);
			if(empty($lineas)){
				echo "<div id='texto'>La venta esta vac&iacute;a. Añadir productos <a href='rellenar.php?codigo=$codVen&total=$total'><button><img src='../img/add.png' alt='Quitar' /></a></div>";
			}else{
			echo "<table id='tabla'>
					<tr><td>C&oacute;digo Producto</td>
					<td>Nombre</td>
					<td>Cantidad</td>
					<td>Acci&oacute;n</td></tr>";
					for($n=0; $n<sizeof($lineas); $n++){
						$articulo = $lineas[$n];
						$nprod = $articulo['CODIGOPRODUCTO'];
						$producto = consultaProdCod($con, $nprod);
						$nombre = $producto['NOMBRE'];
						$cantidad = $articulo['CANTIDAD'];
						echo "<tr><td>$nprod</td>\n";
						echo "<td>$nombre</td>\n";
						echo "<td>$cantidad</td>\n";
						echo "<td><a href='quitar.php?cod=$codVen&prod=$nprod'><button><img src='../img/delete.png' alt='Quitar' /></button></a></td></tr>";
					}
					echo "<tr><td>Añadir Productos</td><td></td><td></td><td><a href='rellenar.php?codigo=$codVen&total=$total'><button><img src='../img/add.png' alt='Quitar' /></a></td></tr>";
			echo "</table>";
			}
	?>
	<?php
		}else{
			$con = conectar();
			$codVen = $_REQUEST['ncodVen'];
			if(empty($_REQUEST['numSoc'])){
				$numSoc = NULL;
			}else{
				$numSoc = $_REQUEST['numSoc'];
			}
			$fecha = $_REQUEST['fecha'];
			$pagado = $_REQUEST['pagado'];
			if($venta['PAGADO'] != $pagado){
				modPagoReserva($con, $codVen, $pagado);
			}
			modificarVenta($con, $codVen, $numSoc, $fecha);
			desconectar($con);
			header("Location: modificar.php?cod=$codVen");
		}
	?>
	</body>
</html>
