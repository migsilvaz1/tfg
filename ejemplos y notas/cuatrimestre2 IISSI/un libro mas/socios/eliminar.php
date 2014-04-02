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
		<title>Elminar Socio</title>
		<LINK REL=StyleSheet HREF="eliminar.css" TYPE="text/css" MEDIA=screen>
	</head>
	<body>
		<?php
			$con = conectar();
			$codigo = $_GET['cod'];
			eliminarSocio($con, $codigo);
			desconectar($con);
		?>
		<div id="textofin"><p>Se a eliminado el socio <?php echo $codigo; ?></p></div>
	</body>
</html>