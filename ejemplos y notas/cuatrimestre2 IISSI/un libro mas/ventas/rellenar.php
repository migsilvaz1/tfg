<?php
	if(empty($_GET['codigo']) || !isset($_GET['total'])){
		header("Location: ../error.php");
		exit;
	}
	include '../BDConexion.php';
	include 'gestionVentas.php';
	include '../productos/gestionProductos.php'
?>
<html>
	<head>
		<title>Producto nuevo en venta</title>
		<LINK REL=StyleSheet HREF="rellenar.css" TYPE="text/css" MEDIA=screen>
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
				  var codProd = document.getElementsByName("codProd")[0].value;
				  var cantidad = document.getElementsByName("cantidad")[0].value;
					if(isNaN(codProd)) {
						alert("El código del producto debe ser un número entero.");
						return false;
					}
					if(isNaN(cantidad)) {
						alert("El número de unidades debe ser un número entero.");
						return false;
					}
				}
		</script>
	</head>
	<body>
	<?php
			$total = $_GET['total'];
			if(empty($_REQUEST['codProd'])){
		?>
			<div id="texto"><p>Inserte los datos del producto: </p></div>
			<form id="datosProducto" method="post" onsubmit="return procesar()">
				<div id="envoltura">
					<div id="contenido">
						<div id="grupo1">
				<label>C&oacute;digo del producto:</label><div id="cod"><input name="codProd" type="text" /> </div>
				<label>N&uacute;mero de unidades:</label><div id="cantidad"><input name="cantidad" type="text" /></div>
				<div id="total">Total acumulado: <?php echo $total ?> €</div>
				</div>
				</div>
				</div>
				<div id="botones">
				<div id="seguir"><input type="submit" value="Aceptar y Continuar" /></div>
				<div id="salir"><input name="cond" type="submit" value="Terminar" /></div>
				</div>
			</form>
		<?php
			}else{
				$con = conectar();
				$codVen = $_GET['codigo'];
				$cantidad = $_REQUEST['cantidad'];
				$codProd = 	$_REQUEST['codProd'];
				$venta = consultarVenta($con, $codVen);
				insertarEnVenta($con, $codVen, $cantidad, $codProd,$venta['FECHAVENTA']);
				$producto = consultaProdCod($con, $codProd);
				$totalProd = $cantidad * $producto['PRECIO'];
				$total=$total + $totalProd;
				actualizarTotal($con, $codVen, $total);
				if(!isset($_REQUEST['cond'])){
					header("Location: rellenar.php?codigo=$codVen&total=$total");
				}else{
					echo "<div id='texto'>El total de la venta es $total €.</div>";
					echo "<a href='modificar.php?cod=$codVen'><button><img src='../img/next.png' alt='Seguir' /></button></a>";
				}
			}
	?>
	</body>
</html>
