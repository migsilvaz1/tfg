<?php
	include '../BDConexion.php';
	include 'gestionSocios.php';
?>
<html>
	<head>
		<title>Administrar Socios</title>
		<LINK REL=StyleSheet HREF="administrar.css" TYPE="text/css" MEDIA=screen>
		<script type="text/javascript">
			function procesar () {
			  var numero = document.getElementsByName("numero")[0].value;
			  if((numero !="") && (isNaN(numero))){
			  	alert("Introduzca un numero.");
			  	return false;
			  }
			}
		</script>
	</head>
	<body>
		<?php if(!isset($_REQUEST['numero'])){
			?><div id="texto">Introduzca el n&uacute;mero de socio para realizar la busqueda. Dejelo en blanco para buscar todos los socios.</div>
			<form id="consulta" method="post" onsubmit="return procesar()">
				<div id="envoltura">
					<div id="contenido">
						<div id="grupo1">
				<label>N&uacute;mero:</label><div id="numero"><input name="numero" type="text" /></div>
						</div>
					</div>
				</div>
				<input type="submit" id="buscar" value="Buscar" />
			</form><?php
		}else{
			$con = conectar();
			if(empty($_REQUEST['numero'])){
				$lista = consultarTodosSocios($con);
				echo "<p id='texto'>Resultados: </p>";
				echo "<table id='tabla'>
				<tr><td>N&uacute;mero</td>
				<td>Nombre</td>
				<td>Acci&oacute;n</td></tr>";
				for($n=0; $n<sizeof($lista); $n++){
					$socio = $lista[$n];
					$numero = $socio['NUMEROSOCIO'];
					$nombre = $socio['NOMBRE'];
					echo "<tr><td>$numero</td>\n";
					echo "<td>$nombre</td>\n";
					echo "<td>
							<a href='modificar.php?cod=$numero'><button><img src='../img/page_edit.png' alt='Modificar' /></button></a>
							<a href='eliminar.php?cod=$numero'><button><img src='../img/delete.png' alt='Eliminar' /></button></a>
						</td></tr>";
				}
				echo "</table>";
			}else{
				$socio = consultarUnSocio($con, $_REQUEST['numero']);
				echo "<p id='texto'>Resultados: </p>";
				echo "<table id='tabla'>
				<tr><td>N&uacute;mero</td>
				<td>Nombre</td>
				<td>Acci&oacute;n</td></tr>";
				$numero = $socio['NUMEROSOCIO'];
				$nombre = $socio['NOMBRE'];
				echo "<tr><td>$numero</td>\n";
				echo "<td>$nombre</td>\n";
				echo "<td><a href='modificar.php?cod=$numero'><button><img src='../img/page_edit.png' alt='Modificar' /></button></a>
							<a href='eliminar.php?cod=$numero'><button><img src='../img/delete.png' alt='Eliminar' /></button></a></td></tr>\n";
				echo "</table>";
			}
			desconectar($con);
		}
		?>
	</body>
</html>
