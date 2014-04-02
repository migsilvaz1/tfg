<?php
	include '../BDConexion.php';
	include 'gestionProductos.php';
?>
<html>
	<head>
		<title>Crear Nuevo Producto</title>
		<LINK REL=StyleSheet HREF="nuevo.css" TYPE="text/css" MEDIA=screen>
		<script type="text/javascript">
				
				function comprobarSeleccionado(){
                 var aRadios = document.getElementsByName("tipo");
                 var activo = false;
 
                 for( var contador=0; contador < aRadios.length; contador++ ){
                     if(aRadios[contador].checked == true)activo = true;
                 }
 
                 if(!activo){
                 	alert("Seleccione una opción.")
                 	return false;
                 }
               }
             	
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
			if(!isset($_REQUEST['tipo'])){
		?>
		<div id="intro"><p>Seleccione el tipo de producto que desea crear:</p></div>
			<form id="seleccion" method="get" onsubmit="return comprobarSeleccionado()">
				<input name="tipo" id="tipoComic" type="radio" value="comic" /> Comic
				<input name="tipo" id="tipoLibro" type="radio" value="libro" /> Libro
				<input name="tipo" id="tipoMerch" type="radio" value="merchandising" /> Merchandising
				<input type="submit" id="aceptar" value="Aceptar" />
			</form>
		<?php }else{
				if(!isset($_REQUEST['codProd'])){
			?>
		<div id="texto"><p>Rellene los datos para crear el nuevo producto: </p></div>
		<form id="datosGenericos" method="post" onsubmit="return procesar()">
			<div id="envoltura">
				<div id="contenido">
					<div id="grupo1">
			<label>C&oacute;digo:</label><div id="codigo"><input name="codProd" type="text" /></div>
			<label>Nombre:</label><div id="nombre"><input name="nombre" type="text" /></div>
			<label>Precio:</label><div id="precio"><input name="precio" type="text" /></div>
			<label>Popularidad:</label><div id="popularidad"><input name="popularidad" type="text" value="0"/></div>
					</div>
					<div id="grupo2">
			<label>Edad recomendada:</label><div id="edad"><input name="edadRec" type="text" /></div>
			<label>Personaje protagonista:</label><div id="personaje"><input name="personaje" type="text" /></div>
			<label>Colecci&oacute;n:</label><div id="coleccion"><input name="coleccion" type="text" /></div>
			<label>Stock:</label><div id="stock"><input name="stock" type="text" /></div>
					</div>
					<div id="grupo3">
			<?php
			if($_REQUEST['tipo']=="comic" || $_REQUEST['tipo']=="libro"){ 
			?>
			<label>Editorial:</label><div id="editorial"><input name="editorial" type="text" /></div>
			<label>Precio de alquiler:</label><div id="precioAlq"><input name="precAlq" type="text" /></div>
			<label>Autor:</label><div id="autor"><input name="autor" type="text" /></div>
			<?php 	
				if($_REQUEST['tipo']=="comic"){
			?>
			<label>Tipo:</label><div id="tcomic"><select name="tipoC">
				<option value="grapa">Grapa</option>
				<option value="tomo">Tomo</option>
			</select></div>
			<label>G&eacute;nero:</label><div id="gcomic"><select name="generoC">
				<option value="manga">Manga</option>
				<option value="vinetas">Viñetas</option>
				<option value="heroico">Heroico</option>
			</select></div>
			<?php
				}else{ 
			?>
			<label>Tipo:</label><div id="tlibro"><select name="tipoL">
				<option value="bolsillo">Bolsillo</option>
				<option value="tapaDura">Tapa Dura</option>
				<option value="tapaBlanda">Tapa Blanda</option>
			</select></div>
			<label>G&eacute;nero:</label><div id="glibro"><select name="generoL">
				<option value="aventura">Aventura</option>
				<option value="cienciaFiccion">Ciencia Ficci&oacute;n</option>
				<option value="clasicos">Cl&aacute;sicos</option>
				<option value="cuentos">Cuentos</option>
				<option value="ensayos">Ensayos</option>
				<option value="novelaNarrativa">Novela Narrativa</option>
				<option value="novelaPolicial">Novela Policial</option>
				<option value="novelaHistorica">Novela Hist&oacute;rica</option>
				<option value="poesia">Poes&iacute;a</option>
				<option value="teatro">Teatro</option>
				<option value="tecnicos">T&eacute;cnicos</option>
				<option value="infantil">Infantil</option>
			</select></div>
			<?php 	
				}
			}else{ 
			?>
			<label>Marca:</label><div id="marca"><input name="marca" type="text" /></div>
			<?php
			}
			?>
			</div>
			</div>
			</div>
			<div id="botones">
			<div id="limpiar"><input type="reset" value="Limpiar" /></div>
			<div id="crear"><input type="submit" value="Crear" /></div>
			</div>
			
			</form>
			<?php
			}else{
				$con = conectar();
				$codProd = (integer)$_REQUEST['codProd'];
				$nom = $_REQUEST['nombre'];
				$precio = (integer) $_REQUEST['precio'];
				$popu = (integer)$_REQUEST['popularidad'];
				$edRec = (integer)$_REQUEST['edadRec'];
				$personaje = $_REQUEST['personaje'];
				$coleccion = $_REQUEST['coleccion'];
				$stock = (integer)$_REQUEST['stock'];
				if($_REQUEST['tipo']=="comic" || $_REQUEST['tipo']=="libro"){
					$editorial = $_REQUEST['editorial'];
					$precAlq = (float)$_REQUEST['precAlq'];
					$autor = $_REQUEST['autor'];
					if($_REQUEST['tipo'] == "comic"){
						$tipoComic = $_REQUEST['tipoC'];
						$generoComic = $_REQUEST['generoC'];
						insertarComic($con, $tipoComic, $generoComic, $editorial, $precAlq, $autor, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock);
					}else{
						$tipoLibro = $_REQUEST['tipoL'];
						$generoLibro = $_REQUEST['generoL'];
						insertarLibro($con, $tipoLibro, $generoLibro, $editorial, $precAlq, $autor, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock);
					}
				}else{
					$marca = $_REQUEST['marca'];
					insertarMerchandising($con, $marca, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock);
				}
				desconectar($con);
			?>
			<div id="textofin"><p>El producto se ha creado correctamente.</p></div>
			<?php
			}
			}
			?>
	</body>
</html>
