<?php
    function insertarProducto($con,$codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock){
		$stmt = oci_parse($con,'INSERT INTO productos (codigoProducto, nombre, precio, popularidad, edadRecomendada, personaje, coleccion, stock) VALUES (:codProd, :nom, :precio, :popu, :edRec, :personaje, :coleccion, :stock)');
		oci_bind_by_name($stmt,':codProd', $codProd);
		oci_bind_by_name($stmt,':nom', $nom);
		oci_bind_by_name($stmt,':precio', $precio);
		oci_bind_by_name($stmt,':popu', $popu);
		oci_bind_by_name($stmt,':edRec', $edRec);
		oci_bind_by_name($stmt,':personaje', $personaje);
		oci_bind_by_name($stmt,':coleccion', $coleccion);
		oci_bind_by_name($stmt,':stock', $stock);
		oci_execute($stmt);
		oci_free_statement($stmt);
    }
	function insertarImpreso($con, $editorial, $precAlq, $autor, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock){
		insertarProducto($con, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock);
		$stmt = oci_parse($con, 'SELECT sec_ids.NEXTVAL FROM dual');
		oci_execute($stmt);
		$cadena = oci_fetch_array($stmt);
		$id = $cadena[0];
		oci_free_statement($stmt);
		$stmt = oci_parse($con,'INSERT INTO impresos (id_impreso, editorial, precioAlquiler, autor, codigoProducto) VALUES (:id, :editorial, :precAlq, :autor, :codProd)');
		oci_bind_by_name($stmt,':id',$id);
		oci_bind_by_name($stmt,':editorial', $editorial);
		oci_bind_by_name($stmt,':precAlq', $precAlq);
		oci_bind_by_name($stmt,':autor', $autor);
		oci_bind_by_name($stmt,':codProd', $codProd);
		oci_execute($stmt);
		oci_free_statement($stmt);
		return $id;
	}
    function insertarComic($con, $tipoComic, $generoComic, $editorial, $precAlq, $autor, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock){
    	$idImpreso = insertarImpreso($con, $editorial, $precAlq, $autor, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock);
		if($idImpreso!=NULL){
			$stmt = oci_parse($con, 'SELECT sec_ids.NEXTVAL FROM dual');
			oci_execute($stmt);
			$cadena = oci_fetch_array($stmt);
			$id = $cadena[0];
			oci_free_statement($stmt);
			$stmt = oci_parse($con,'INSERT INTO comics (id_comic, tipoComic, generoComic, id_impreso) VALUES (:id, :tipoComic, :generoComic, :idImpreso)');
			oci_bind_by_name($stmt,':id',$id);
			oci_bind_by_name($stmt,':tipoComic', $tipoComic);
			oci_bind_by_name($stmt,':generoComic', $generoComic);
			oci_bind_by_name($stmt,':idImpreso', $idImpreso);
			oci_execute($stmt);
			oci_free_statement($stmt);
		}
	}
	
	function insertarLibro($con, $tipoLibro, $generoLibro, $editorial, $precAlq, $autor, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock){
    	$idImpreso = insertarImpreso($con, $editorial, $precAlq, $autor, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock);
		if($idImpreso!=NULL){
			$stmt = oci_parse($con, 'SELECT sec_ids.NEXTVAL FROM dual');
			oci_execute($stmt);
			$cadena = oci_fetch_array($stmt);
			$id = $cadena[0];
			oci_free_statement($stmt);
			$stmt = oci_parse($con,'INSERT INTO libros (id_libro, tipoLibro, generoLibro, id_impreso) VALUES (:id, :tipoLibro, :generoLibro, :idImpreso)');
			oci_bind_by_name($stmt,':id',$id);
			oci_bind_by_name($stmt,':tipoLibro', $tipoLibro);
			oci_bind_by_name($stmt,':generoLibro', $generoLibro);
			oci_bind_by_name($stmt,':idImpreso', $idImpreso);
			oci_execute($stmt);
			oci_free_statement($stmt);
		}
	}
	
	function insertarMerchandising($con, $marca, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock){
		$stmt = oci_parse($con, 'SELECT sec_ids.NEXTVAL FROM dual');
		oci_execute($stmt);
		$cadena = oci_fetch_array($stmt);
		$id = $cadena[0];
		oci_free_statement($stmt);
		insertarProducto($con, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock);
		$stmt = oci_parse($con,'INSERT INTO merchandising (id_merchandising, marca, codigoProducto) VALUES (:id, :marca, :codProd)');
		oci_bind_by_name($stmt,':id',$id);
		oci_bind_by_name($stmt,':marca', $marca);
		oci_bind_by_name($stmt,':codProd', $codProd);
		oci_execute($stmt);
		oci_free_statement($stmt);
	}
	function consultaProdCod($con, $codigo){
		$res = NULL;
		$stmt = oci_parse($con,'SELECT * FROM productos WHERE codigoProducto = :codigo');
		oci_bind_by_name($stmt,':codigo', $codigo);
		oci_execute($stmt);
		$rproducto = oci_fetch_array($stmt);
		oci_free_statement($stmt);
		$stmt = oci_parse($con,'SELECT * FROM impresos JOIN comics ON impresos.id_impreso = comics.id_impreso WHERE codigoProducto = :codigo');
		oci_bind_by_name($stmt,':codigo', $codigo);
		oci_execute($stmt);
		$rcomic = oci_fetch_array($stmt);
		oci_free_statement($stmt);
		if($rcomic == FALSE){
			$stmt = oci_parse($con,'SELECT * FROM impresos JOIN libros ON impresos.id_impreso = libros.id_impreso WHERE codigoProducto = :codigo');
			oci_bind_by_name($stmt,':codigo', $codigo);
			oci_execute($stmt);
			$rlibro = oci_fetch_array($stmt);
			oci_free_statement($stmt);
			if($rlibro == FALSE){
				$stmt = oci_parse($con,'SELECT * FROM merchandising WHERE codigoProducto = :codigo');
				oci_bind_by_name($stmt,':codigo', $codigo);
				oci_execute($stmt);
				$rmer = oci_fetch_array($stmt);
				oci_free_statement($stmt);
				if($rmer == FALSE){
					$res = FALSE;
				}else{
					$res = array_merge($rproducto, $rmer);
				}
			}else{
				$res = array_merge($rproducto, $rlibro);
			}
		}else{
			$res = array_merge($rproducto, $rcomic);
		}
		return $res;
	}
	function buscarRapNombre($con, $nombre){
		$lista = array();
		$stmt = oci_parse($con,'SELECT * FROM productos WHERE nombre LIKE :nombre ORDER BY codigoProducto');
		$nombre = "%".$nombre."%";
		oci_bind_by_name($stmt,':nombre', $nombre);
		oci_execute($stmt);
		$check = oci_fetch_all($stmt, $lista, null, null, OCI_FETCHSTATEMENT_BY_ROW);
		if($check == FALSE)return $check;
		oci_free_statement($stmt);
		return $lista;
	}
	function buscarTodos($con){
		$lista = array();
		$stmt = oci_parse($con,'SELECT * FROM productos ORDER BY codigoProducto');
		oci_execute($stmt);
		$check = oci_fetch_all($stmt, $lista, null, null, OCI_FETCHSTATEMENT_BY_ROW);
		if($check == FALSE)return $check;
		oci_free_statement($stmt);
		return $lista;
	}
	function modificarProducto($con, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock){
    	$stmt = oci_parse($con,'UPDATE productos SET nombre = :nom, precio = :precio, popularidad = :popu, edadRecomendada = :edRec, personaje = :personaje, coleccion = :coleccion, stock = :stock WHERE  codigoProducto = :codProd');
		oci_bind_by_name($stmt,':codProd', $codProd);
		oci_bind_by_name($stmt,':nom', $nom);
		oci_bind_by_name($stmt,':precio', $precio);
		oci_bind_by_name($stmt,':popu', $popu);
		oci_bind_by_name($stmt,':edRec', $edRec);
		oci_bind_by_name($stmt,':personaje', $personaje);
		oci_bind_by_name($stmt,':coleccion', $coleccion);
		oci_bind_by_name($stmt,':stock', $stock);
		oci_execute($stmt);
		oci_free_statement($stmt);
	}
	function modificarImpreso($con, $editorial, $precAlq, $autor, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock){
		modificarProducto($con, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock);
		$stmt = oci_parse($con,'UPDATE impresos SET editorial = :editorial, precioAlquiler = :precAlq, autor = :autor WHERE codigoProducto = :codProd');
		oci_bind_by_name($stmt,':editorial', $editorial);
		oci_bind_by_name($stmt,':precAlq', $precAlq);
		oci_bind_by_name($stmt,':autor', $autor);
		oci_bind_by_name($stmt,':codProd', $codProd);
		oci_execute($stmt);
		oci_free_statement($stmt);
		$stmt = oci_parse($con,'SELECT * FROM impresos WHERE codigoProducto = :codProd');
		oci_bind_by_name($stmt,':codProd', $codProd);
		oci_execute($stmt);
		$impreso = oci_fetch_array($stmt);
		oci_free_statement($stmt);
		return $impreso['ID_IMPRESO'];
	}
    function modificarComic($con, $tipoComic, $generoComic, $editorial, $precAlq, $autor, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock){
    	$idImpreso = modificarImpreso($con, $editorial, $precAlq, $autor, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock);
		$stmt = oci_parse($con,'UPDATE comics SET tipoComic = :tipoComic, generoComic = :generoComic WHERE id_impreso = :idImpreso');
		oci_bind_by_name($stmt,':tipoComic', $tipoComic);
		oci_bind_by_name($stmt,':generoComic', $generoComic);
		oci_bind_by_name($stmt,':idImpreso', $idImpreso);
		oci_execute($stmt);
		oci_free_statement($stmt);	
    }
	
	function modificarLibro($con, $tipoLibro, $generoLibro, $editorial, $precAlq, $autor, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock){
		$idImpreso = modificarImpreso($con, $editorial, $precAlq, $autor, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock);
		$stmt = oci_parse($con,'UPDATE libros SET tipoLibro = :tipoLibro, generoLibro = :generoLibro WHERE id_impreso = :idImpreso');
		oci_bind_by_name($stmt,':tipoLibro', $tipoLibro);
		oci_bind_by_name($stmt,':generoLibro', $generoLibro);
		oci_bind_by_name($stmt,':idImpreso', $idImpreso);
		oci_execute($stmt);
		oci_free_statement($stmt);
	}
	
	function modificarMerchandising($con, $marca, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock){
		modificarProducto($con, $codProd, $nom, $precio, $popu, $edRec, $personaje, $coleccion, $stock);
		$stmt = oci_parse($con,'UPDATE merchandising SET marca = :marca WHERE codigoProducto = :codProd');
		oci_bind_by_name($stmt,':marca', $marca);
		oci_bind_by_name($stmt,':codProd', $codProd);
		oci_execute($stmt);
		oci_free_statement($stmt);
	}
	function eliminarProducto($con, $codigo){
		$producto = consultaProdCod($con, $codigo);
		if(isset($producto['ID_COMIC'])){
			$stmt = oci_parse($con,'DELETE FROM comics WHERE id_impreso = :id');
			oci_bind_by_name($stmt,':id', $producto['ID_IMPRESO']);
			oci_execute($stmt);
			oci_free_statement($stmt);
			$stmt = oci_parse($con,'DELETE FROM impresos WHERE codigoProducto = :codProd');
			oci_bind_by_name($stmt,':codProd', $producto['CODIGOPRODUCTO']);
			oci_execute($stmt);
			oci_free_statement($stmt);
			$stmt = oci_parse($con,'DELETE FROM productos WHERE codigoProducto = :codProd');
			oci_bind_by_name($stmt,':codProd', $producto['CODIGOPRODUCTO']);
			oci_execute($stmt);
			oci_free_statement($stmt);
		}
		if(isset($producto['ID_LIBRO'])){
			$stmt = oci_parse($con,'DELETE FROM libros WHERE id_impreso = :id');
			oci_bind_by_name($stmt,':id', $producto['ID_IMPRESO']);
			oci_execute($stmt);
			oci_free_statement($stmt);
			$stmt = oci_parse($con,'DELETE FROM impresos WHERE codigoProducto = :codProd');
			oci_bind_by_name($stmt,':codProd', $producto['CODIGOPRODUCTO']);
			oci_execute($stmt);
			oci_free_statement($stmt);
			$stmt = oci_parse($con,'DELETE FROM productos WHERE codigoProducto = :codProd');
			oci_bind_by_name($stmt,':codProd', $producto['CODIGOPRODUCTO']);
			oci_execute($stmt);
			oci_free_statement($stmt);
		}
		if(isset($producto['ID_MERCHANDISING'])){
			$stmt = oci_parse($con,'DELETE FROM merchandising WHERE codigoProducto = :codProd');
			oci_bind_by_name($stmt,':codProd', $producto['CODIGOPRODUCTO']);
			oci_execute($stmt);
			oci_free_statement($stmt);
			$stmt = oci_parse($con,'DELETE FROM productos WHERE codigoProducto = :codProd');
			oci_bind_by_name($stmt,':codProd', $producto['CODIGOPRODUCTO']);
			oci_execute($stmt);
			oci_free_statement($stmt);
		}
	}
?>