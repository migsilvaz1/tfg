<?php
	if(empty($_GET['cod'])){
		header("Location: ../error.php");
		exit;
	}
	include '../BDConexion.php';
	include 'gestionEventos.php';
?>
<html>
	<head>
		<title>Elminar Evento</title>
		<LINK REL=StyleSheet HREF="eliminar.css" TYPE="text/css" MEDIA=screen>
	</head>
	<body>
		<?php
			$con = conectar();
			$id = $_GET['cod'];
			eliminarEvento($con, $id);
			desconectar($con);
		?>
		<div id="texto">Se a eliminado el evento.</div>
	</body>
</html>