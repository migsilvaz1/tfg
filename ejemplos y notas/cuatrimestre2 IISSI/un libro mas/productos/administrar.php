<?php
	include '../BDConexion.php';
	include 'gestionProductos.php';
?>
<html>
	<head>
		<title>Administrar Productos</title>
		<LINK REL=StyleSheet HREF="administrar.css" TYPE="text/css" MEDIA=screen>
		<script type="text/javascript">
				
				function comprobarDatos(){
                 var ctrlCodProd = document.getElementsByName("codProd");
                 var codigo = ctrlCodProd[0].value;
                 var ctrlNombre = document.getElementsByName("nombre");
                 var nombre = ctrlNombre[0].value;
                 if(codigo !="" && nombre !=""){
                 	alert("Solo puede rellenar una opcion.");
                 	return false;
                 }
               }
		</script>
	</head>
	<body>
		<?php
			if(!isset($_REQUEST['codProd']) || !isset($_REQUEST['nombre'])){
		?>
		<div id="intro"><p>Introduzca datos para usar uno de los criterios de b&uacute;squeda. Dejar en blanco para obtener un listado de todos los productos: </p></div>
		<form id="consulta" method="get" onsubmit="return comprobarDatos()">
			<div id="envoltura">
				<div id="contenido">
					<div id="grupo1">
			<label>Buscar por el c&oacute;digo del producto:</label><div id="codigo"><input name="codProd" type="text" /></div>
			<label>Buscar por el nombre del producto:</label><div id="nombre"><input name="nombre" type="text" /></div>
					</div>
				</div>
			</div>
			<input type="submit" id="buscar" value="Buscar" />
		</form>
		<?php
			}else{
				$con = conectar();
				if(!empty($_REQUEST['codProd'])){
					$codigo = $_REQUEST['codProd'];
					$producto = consultaProdCod($con, $codigo);
					$codigo = $producto['CODIGOPRODUCTO'];
					$nombre = $producto['NOMBRE'];
					$precio = $producto['PRECIO'];
					$stock = $producto['STOCK'];
					echo "<p id=\"texto\">Resultados: </p>";
					echo "<table id=\"tabla\">
			<tr>
				<td>C&oacute;digo</td>
				<td>Nombre</td>
				<td>Precio</td>
				<td>Stock</td>
				<td>Acci&oacute;n</td>
			</tr>
			<tr>
				<td>$codigo</td>
				<td>$nombre</td>
				<td>$precio</td>
				<td>$stock</td>";
				echo "<td>
							<a href='modificar.php?codp=$codigo'><button><img src='../img/page_edit.png' alt='Modificar' /></button></a>
							<a href='eliminar.php?codp=$codigo'><button><img src='../img/delete.png' alt='Eliminar' /></button></a>
						</td></tr>";
				echo"</table>";
				}
				if(!empty($_REQUEST['nombre'])){
					$nombre = $_REQUEST['nombre'];
					$productos = buscarRapNombre($con, $nombre);
					if($productos == FALSE){
						echo "No se han encontrado resultados.";
					}else{
					echo "<p id=\"texto\">Resultados: </p>";
					echo "<table id=\"tabla\">
			<tr>
				<td>C&oacute;digo</td>
				<td>Nombre</td>
				<td>Precio</td>
				<td>Stock</td>
				<td>Acci&oacute;n</td>
			</tr>";
					for($n=0; $n < sizeof($productos); $n++){
						$producto = $productos[$n];
						$codigo = $producto['CODIGOPRODUCTO'];
						$nombre = $producto['NOMBRE'];
						$precio = $producto['PRECIO'];
						$stock = $producto['STOCK'];
						echo "<tr><td>$codigo</td>";
						echo "<td>$nombre</td>";
						echo "<td>$precio</td>";
						echo "<td>$stock</td>";
						echo "<td>
							<a href='modificar.php?codp=$codigo'><button><img src='../img/page_edit.png' alt='Modificar' /></button></a>
							<a href='eliminar.php?codp=$codigo'><button><img src='../img/delete.png' alt='Eliminar' /></button></a>
						</td></tr>";
					}
					echo "</table>";
					}
				}
				if(empty($_REQUEST['nombre']) && empty($_REQUEST['codProd'])){
					$productos = buscarTodos($con);
					if($productos == FALSE){
						echo "No se han encontrado resultados.";
					}else{
					echo "<p id=\"texto\">Resultados: </p>";
					echo "<table id=\"tabla\">
			<tr>
				<td>C&oacute;digo</td>
				<td>Nombre</td>
				<td>Precio</td>
				<td>Stock</td>
				<td>Acci&oacute;n</td>
			</tr>";
					for($n=0; $n < sizeof($productos); $n++){
						$producto = $productos[$n];
						$codigo = $producto['CODIGOPRODUCTO'];
						$nombre = $producto['NOMBRE'];
						$precio = $producto['PRECIO'];
						$stock = $producto['STOCK'];
						echo "<tr><td>$codigo</td>";
						echo "<td>$nombre</td>";
						echo "<td>$precio</td>";
						echo "<td>$stock</td>";
						echo "<td>
							<a href='modificar.php?codp=$codigo'><button><img src='../img/page_edit.png' alt='Modificar' /></button></a>
							<a href='eliminar.php?codp=$codigo'><button><img src='../img/delete.png' alt='Eliminar' /></button></a>
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
