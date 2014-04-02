<?php
	include '../BDConexion.php';
	include 'gestionVentas.php';
?>
<html>
	<head>
		<title>Administrar Venta</title>
		<LINK REL=StyleSheet HREF="administrar.css" TYPE="text/css" MEDIA=screen>
		<script type="text/javascript">
			function procesar () {
			 var codVen = document.getElementsByName("codVen")[0].value;
			 var numSoc = document.getElementsByName("numSoc")[0].value;
			 if((codVen =="") && (numSoc == "")){
			 	alert("Introduzca algún dato para realizar la búsqueda.");
			 	return false;
			 }
			 if((codVen != "")&&(isNaN(codVen))){
			 	alert("El número de venta debe ser un número entero.");
			 	return false;
			 }
			 if((numSoc != "")&&(isNaN(numSoc))){
			 	alert("El número de socio debe ser un número entero.");
			 	return false;
			 }
			}
		</script>
	</head>
	<body>
		<?php
			if(!isset($_REQUEST['codVen']) && !isset($_REQUEST['numSoc']) && !isset($_REQUEST['nsoc'])){
		?>
			<div id="texto"><p>Introduzca los datos para la busqueda:</p></div>
			<form id="datos" method="post" onsubmit="return procesar()">
				<div id="envoltura">
					<div id="contenido">
						<div id="grupo1">
				<label>N&uacute;mero de venta:</label><div id="codigo"><input name="codVen" type="text" /></div>
				<label>N&uacute;mero de socio:</label><div id="socio"><input name="numSoc" type="text" /></div>
						</div>
					</div>
				</div>
				<div id="buscar"><input type="submit" value="Buscar Venta" /></div>
			</form>
		<?php
			}else{
				$con = conectar();
				if(!empty($_REQUEST['codVen'])){
					$venta = consultarVenta($con, $_REQUEST['codVen']);
					if(empty($venta)){
						echo "No se ha encontrado ninguna venta con ese c&oacute;digo.";
					}else{
					$nventa = $venta['CODIGOVENTA'];
					$fecha = $venta['FECHAVENTA'];
					$total = $venta['TOTAL'];
					$pagado = $venta['PAGADO'];
					echo "<p id='texto'>Resultados: </p>";
					echo "<table id='tabla'>
					<tr><td>Venta</td>
					<td>Fecha</td>
					<td>Total</td>
					<td>Tipo</td>
					<td>Acci&oacute;n</td></tr>";
					echo "<tr><td>$nventa</td>\n";
					echo "<td>$fecha</td>\n";
					echo "<td>$total</td>\n";
					if($pagado == 'Y'){
						echo "<td>Venta</td>\n";
					}else{
						echo "<td>Reserva</td>\n";
					}
					echo "<td>
							<a href='modificar.php?cod=$nventa'><button><img src='../img/page_edit.png' alt='Modificar' /></button></a>
							<a href='eliminar.php?cod=$nventa'><button><img src='../img/delete.png' alt='Eliminar' /></button></a>
						</td></tr>";
					echo "</table>";
					}
					}
				if(!empty($_REQUEST['numSoc'])){
					$lista = consultarVentasSocio($con, $_REQUEST['numSoc']);
					if(empty($lista)){
						echo "No se ha encontrado ninguna venta de ese socio.";
					}else{
					echo "<p id='texto'>Resultados: </p>";
					echo "<table id='tabla'>
					<tr><td>Venta</td>
					<td>Fecha</td>
					<td>Total</td>
					<td>Tipo</td>
					<td>Acci&oacute;n</td></tr>";
					for($n=0; $n<sizeof($lista); $n++){
						$venta = $lista[$n];
						$nventa = $venta['CODIGOVENTA'];
						$fecha = $venta['FECHAVENTA'];
						$total = $venta['TOTAL'];
						$pagado = $venta['PAGADO'];
						echo "<tr><td>$nventa</td>\n";
						echo "<td>$fecha</td>\n";
						echo "<td>$total</td>\n";
						if($pagado == 'Y'){
						echo "<td>Venta</td>\n";
					}else{
						echo "<td>Reserva</td>\n";
					}
						echo "<td>
							<a href='modificar.php?cod=$nventa'><button><img src='../img/page_edit.png' alt='Modificar' /></button></a>
							<a href='eliminar.php?cod=$nventa'><button><img src='../img/delete.png' alt='Eliminar' /></button></a>
						</td></tr>";
					}
					echo "</table>";
					}
				}
				desconectar($con);
			}
		?>
	</body>
</html>
