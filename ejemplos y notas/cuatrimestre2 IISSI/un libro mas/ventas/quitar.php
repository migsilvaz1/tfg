<?php
	if(empty($_GET['cod']) || empty($_GET['prod'])){
		header("Location: ../error.php");
		exit;
	}
	include '../BDConexion.php';
	include 'gestionVentas.php';
	include '../productos/gestionProductos.php';
?>
<html>
	<head>
		<title>Eliminar de Venta</title>
		<LINK REL=StyleSheet HREF="quitar.css" TYPE="text/css" MEDIA=screen>
	</head>
	<body>
		<?php
			$con = conectar();
			$codVen = $_GET['cod'];
			$codProd = $_GET['prod'];
			$restar = 0.0;
			$cantidad = 0;
			$venta = consultarVenta($con, $codVen);
			$lineas = consultarLineasDeVenta($con, $codVen);
			for($n=0;$n<sizeof($lineas);$n++){
				$actual = $lineas[$n];
				if($actual['CODIGOPRODUCTO'] == $codProd){
					$cantidad = $cantidad + $actual['CANTIDAD'];
				}
			}
			$producto = consultaProdCod($con, $codProd);
			$restar = $venta['TOTAL'] -( $cantidad * $producto['PRECIO'] );
			actualizarTotal($con, $codVen, $restar);
			eliminarDeVenta($con, $codVen, $codProd, $cantidad);
			desconectar($con);
			echo "<div id='texto'>Se a eliminado el producto $codProd de la venta $codVen</div><div id='boton'><a href='modificar.php?cod=$codVen'><button><img src='../img/accept.png' alt='Aceptar' /></button></a></div>"; ?>
	</body>
</html>