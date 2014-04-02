<?php
	if(empty($_GET['codp'])){
		header("Location: ../error.php");
		exit;
	}
	include '../BDConexion.php';
	include 'gestionProductos.php';
?>
<html>
	<head>
		<title>Elminar Producto</title>
		<LINK REL=StyleSheet HREF="eliminar.css" TYPE="text/css" MEDIA=screen>
	</head>
	<body>
		<?php
			$con = conectar();
			$codigo = $_GET['codp'];
			eliminarProducto($con, $codigo);
			desconectar($con);
		?>
		<div id="texto"><p>Se a eliminado el producto <?php echo $codigo; ?></p></div>
	</body>
</html>
