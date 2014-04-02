<?php
	if(empty($_GET['cod'])){
		header("Location: ../error.php");
		exit;
	}
	include '../BDConexion.php';
	include 'gestionVentas.php';
?>
<html>
	<head>
		<title>Elminar Venta</title>
		<LINK REL=StyleSheet HREF="eliminar.css" TYPE="text/css" MEDIA=screen>
	</head>
	<body>
		<?php
			$con = conectar();
			$codigo = $_GET['cod'];
			$lineas = consultarLineasDeVenta($con, $codigo);
			for($n=0; $n<sizeof($lineas); $n++){
				$actual = $lineas[$n];
				eliminarDeVenta($con, $codigo, $actual['CODIGOPRODUCTO']);
			}
			eliminarVenta($con, $codigo);
			desconectar($con);
		?>
		<div id="texto"><p>Se a eliminado la venta <?php echo $codigo; ?></p></div>
	</body>
</html>