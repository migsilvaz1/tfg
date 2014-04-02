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
		<title>Modificar Producto</title>
		<LINK REL=StyleSheet HREF="modificar.css" TYPE="text/css" MEDIA=screen>
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
				  var precio = document.getElementsByName("precio")[0].value;
				  if(isNaN(precio)){
				  	alert("El precio debe ser un número real.");
				  	return false;
				  }
				  var popularidad = document.getElementsByName("popularidad")[0].value;
				  if(isNaN(popularidad)){
				  	alert("La popularidad debe ser un número entero.");
				  	return false;
				  }
				  var edad = document.getElementsByName("edadRec")[0].value;
				  if(isNaN(edad)){
				  	alert("La edad recomendada debe ser un número entero.");
				  	return false;
				  }
				  var stock = document.getElementsByName("stock")[0].value;
				  if(isNaN(stock)){
				  	alert("El stock debe ser un número entero.");
				  	return false;
				  }
				}
		</script>
	</head>
	<body>
		<?php 
			$con = conectar();
			$producto = consultaProdCod($con, $_GET['codp']);
			if(empty($_REQUEST['codProd'])){
		?>
		<div id="texto">Actualice los campos necesarios. Recuerde que no pueden quedar campos vacios.</div>
		<form id="datosGenericos" method="post" onsubmit="return procesar()">
			<div id="envoltura">
				<div id="contenido">
					<div id="grupo1">
			<label>C&oacute;digo:</label><div id="codigo"><input name="codProd" type="text" value="<?php echo $producto['CODIGOPRODUCTO']; ?>" /></div>
			<label>Nombre:</label><div id="nombre"><input name="nombre" type="text" value="<?php echo $producto['NOMBRE']; ?>" /></div>
			<label>Precio:</label><div id="precio"><input name="precio" type="text" value="<?php echo $producto['PRECIO']; ?>" /></div>
			<label>Popularidad:</label><div id="popularidad"><input name="popularidad" type="text" value="<?php echo $producto['POPULARIDAD']; ?>" /></div>
					</div>
					<div id="grupo2">
			<label>Edad recomendada:</label><div id="edad"><input name="edadRec" type="text" value="<?php echo $producto['EDADRECOMENDADA']; ?>" /></div>
			<label>Personaje protagonista:</label><div id="personaje"><input name="personaje" type="text" value="<?php echo $producto['PERSONAJE']; ?>" /></div>
			<label>Colecci&oacute;n:</label><div id="coleccion"><input name="coleccion" type="text" value="<?php echo $producto['COLECCION']; ?>" /></div>
			<label>Stock:</label><div id="stock"><input name="stock" type="text" value="<?php echo $producto['STOCK']; ?>" /></div>
					</div>
					<div id="grupo3">
			<?php
				if(isset($producto['ID_IMPRESO'])){
			?>
			<label>Editorial:</label><div id="editorial"><input name="editorial" type="text"  value="<?php echo $producto['EDITORIAL']; ?>"/></div>
			<label>Precio de alquiler:</label><div id="precioAlq"><input name="precAlq" type="text" value="<?php echo $producto['PRECIOALQUILER']; ?>" /></div>
			<label>Autor:</label><div id="autor"><input name="autor" type="text" value="<?php echo $producto['AUTOR']; ?>" /></div>
			<?php
					if(isset($producto['ID_COMIC'])){
			?>
			<label>Tipo:</label><div id="tcomic"><select id="tipocomic" name="tipoC">
				<option value="grapa" <?php if($producto['TIPOCOMIC']=="grapa")echo "selected=''"; ?>>Grapa</option>
				<option value="tomo" <?php if($producto['TIPOCOMIC']=="tomo")echo "selected=''"; ?>>Tomo</option>
			</select></div>
			<label>G&eacute;nero:</label><div id="gcomic"><select id="generocomic" name="generoC">
				<option value="manga" <?php if($producto['GENEROCOMIC']=="manga")echo "selected=''"; ?>>Manga</option>
				<option value="viñetas" <?php if($producto['GENEROCOMIC']=="vinetas")echo "selected=''"; ?>>Viñetas</option>
				<option value="heroico" <?php if($producto['GENEROCOMIC']=="heroico")echo "selected=''"; ?>>Heroico</option>
			</select></div>
			<?php		
					}
					if(isset($producto['id_libro'])){
			?>
			<label>Tipo:</label><div id="tlibro"><select id="tipolibro" name="tipoL">
				<option value="bolsillo" <?php if($producto['TIPOLIBRO']=="bolsillo")echo "selected=''"; ?>>Bolsillo</option>
				<option value="tapaDura" <?php if($producto['TIPOCLIBRO']=="tapaDura")echo "selected=''"; ?>>Tapa Dura</option>
				<option value="tapaBlanda" <?php if($producto['TIPOLIBRO']=="tapaBlanda")echo "selected=''"; ?>>Tapa Blanda</option>
			</select></div>
			<label>G&eacute;nero:</label><div id="glibro"><select id="GENEROLIBRO" name="generoL">
				<option value="aventura" <?php if($producto['GENEROLIBRO']=="aventura")echo "selected=''"; ?>>Aventura</option>
				<option value="cienciaFiccion" <?php if($producto['GENEROLIBRO']=="cienciaFiccion")echo "selected=''"; ?>>Ciencia Ficci&oacute;</option>
				<option value="clasicos" <?php if($producto['GENEROLIBRO']=="clasicos")echo "selected=''"; ?>>Cl&aacute;sicos</option>
				<option value="cuentos" <?php if($producto['GENEROLIBRO']=="cuentos")echo "selected=''"; ?>>Cuentos</option>
				<option value="ensayos" <?php if($producto['GENEROLIBRO']=="ensayos")echo "selected=''"; ?>>Ensayos</option>
				<option value="novelaNarrativa" <?php if($producto['GENEROLIBRO']=="novelaNarrativa")echo "selected=''"; ?>>Novela Narrativa</option>
				<option value="novelaPolicial" <?php if($producto['GENEROLIBRO']=="novelaPolicial")echo "selected=''"; ?>>Novela Policial</option>
				<option value="novelaHistorica" <?php if($producto['GENEROLIBRO']=="novelaHistorica")echo "selected=''"; ?>>Novela Hist&oacute;rica</option>
				<option value="poesia" <?php if($producto['GENEROLIBRO']=="poesia")echo "selected=''"; ?>>Poes&iacute;a</option>
				<option value="teatro" <?php if($producto['GENEROLIBRO']=="teatro")echo "selected=''"; ?>>Teatro</option>
				<option value="tecnicos" <?php if($producto['GENEROLIBRO']=="tecnicos")echo "selected=''"; ?>>T&eacute;cnicos</option>
				<option value="infantil" <?php if($producto['GENEROLIBRO']=="infantil")echo "selected=''"; ?>>Infantil</option>
			</select></div>
			<?php	
					}
				}
				if(isset($producto['ID_MERCHANDISING'])){
			?>
			<label>Marca:</label><div id="marca"><input name="marca" type="text" value="<?php echo $producto['MARCA']; ?>" /></div>
			<?php
				}
			?>
			</div>
			</div>
			</div>
			<div id="modificar"><input type="submit" value="Modificar" /></div>
			</form>
			<?php
			}else{
				$codProd = (integer)$_REQUEST['codProd'];
				$nom = $_REQUEST['nombre'];
				$precio = (integer)$_REQUEST['precio'];
				$popu = (integer)$_REQUEST['popularidad'];
				$edRec = (integer)$_REQUEST['edadRec'];
				$personaje = $_REQUEST['personaje'];
				$coleccion = $_REQUEST['coleccion'];
				$stock = (integer)$_REQUEST['stock'];
				if(isset($producto['ID_IMPRESO'])){
					$editorial = $_REQUEST['editorial'];
					$precAlq = (float)$_REQUEST['precAlq'];
					$autor = $_REQUEST['autor'];
					if(isset($producto['ID_COMIC'])){
						$tipoComic = $_REQUEST['tipoC'];
						$generoComic = $_REQUEST['generoC'];
						modificarComic($con, $tipoComic, $generoComic, $editorial, $precAlq, $autor, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock);
					}
					if(isset($producto['ID_LIBRO'])){
						$tipoLibro = $_REQUEST['tipoL'];
						$generoLibro = $_REQUEST['generoL'];
						modificarLibro($con, $tipoLibro, $generoLibro, $editorial, $precAlq, $autor, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock);
					}
				}
				if(isset($producto['ID_MERCHANDISING'])){
					$marca = $_REQUEST['marca'];
					modificarMerchandising($con, $marca, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock);
				}
				desconectar($con);
				header("Location: modificar.php?codp=$codProd");
			}
			?>
	</body>
</html>