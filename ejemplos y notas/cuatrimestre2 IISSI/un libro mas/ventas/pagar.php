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
		<title>Pagar Reserva</title>
		<LINK REL=StyleSheet HREF="pagar.css" TYPE="text/css" MEDIA=screen>
	</head>
	<body>
		<?php
			$con = conectar();
			$codigo = $_GET['cod'];
			pagarReserva($con, $codigo);
			desconectar($con);
		?>
		<div id="texto"><p>Se a pagado la reserva <?php echo $codigo; ?></p></div>
	</body>
</html>