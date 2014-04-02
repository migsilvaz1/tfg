<?php
   function crearVenta($con, $codVen, $numSoc, $fecha, $pagado){
   	$stmt = oci_parse($con,'INSERT INTO ventas (codigoVenta, numeroSocio, fechaVenta, total, pagado) VALUES (:codVen, :numSoc, :fecha, 0.0, :pagado)');
	oci_bind_by_name($stmt,':codVen', $codVen);
	oci_bind_by_name($stmt,':numSoc', $numSoc);
	oci_bind_by_name($stmt,':fecha', $fecha);
	oci_bind_by_name($stmt,':pagado', $pagado);
	oci_execute($stmt);
	oci_free_statement($stmt);
   }
   function modificarVenta($con, $codVen, $numSoc, $fecha){
   	$stmt = oci_parse($con,'UPDATE ventas SET numeroSocio = :numSoc, fechaVenta = :fecha WHERE codigoVenta = :codVen');
	oci_bind_by_name($stmt,':fecha', $fecha);
	oci_bind_by_name($stmt,':numSoc', $numSoc);
	oci_bind_by_name($stmt,':codVen', $codVen);
	oci_execute($stmt);
	oci_free_statement($stmt);
   }
   function actualizarTotal($con, $codVen, $tot){
   	$stmt = oci_parse($con,'UPDATE ventas SET total = :tot WHERE codigoVenta = :codVen');
	oci_bind_by_name($stmt,':codVen', $codVen);
	oci_bind_by_name($stmt,':tot', $tot);
	oci_execute($stmt);
	oci_free_statement($stmt);
   }
   function eliminarVenta($con, $codVen){
   	$stmt = oci_parse($con,'DELETE FROM ventas WHERE codigoVenta = :codVen');
	oci_bind_by_name($stmt,':codVen', $codVen);
	oci_execute($stmt);
	oci_free_statement($stmt);
	}
   function insertarEnVenta($con, $codVen, $cantidad, $codProd, $fecha){
   	$stmt = oci_parse($con,'INSERT INTO lineasVentas (codigoVenta, cantidad, codigoProducto, fechaVenta) VALUES (:codVen, :cantidad, :codProd, :fecha)');
	oci_bind_by_name($stmt,':codProd', $codProd);
	oci_bind_by_name($stmt,':cantidad', $cantidad);
	oci_bind_by_name($stmt,':codVen', $codVen);
	oci_bind_by_name($stmt,':fecha', $fecha);
	oci_execute($stmt);
	oci_free_statement($stmt);
	$producto = consultaProdCod($con, $codProd);
	$nstock = $producto['STOCK'] - $cantidad;
	$stmt = oci_parse($con,'UPDATE productos SET stock = :nstock WHERE codigoProducto = :codProd');
	oci_bind_by_name($stmt,':nstock', $nstock);
	oci_bind_by_name($stmt,':codProd', $codProd);
	oci_execute($stmt);
	oci_free_statement($stmt);
	}
   function eliminarDeVenta($con, $codVen, $codProd, $cantidad){
   	$stmt = oci_parse($con,'DELETE FROM lineasVentas WHERE codigoVenta = :codVen AND codigoProducto = :codProd');
	oci_bind_by_name($stmt,':codVen', $codVen);
	oci_bind_by_name($stmt,':codProd', $codProd);
	oci_execute($stmt);
	oci_free_statement($stmt);
	$producto = consultaProdCod($con, $codProd);
	$nstock = $producto['STOCK'] + $cantidad;
	$stmt = oci_parse($con,'UPDATE productos SET stock = :nstock WHERE codigoProducto = :codProd');
	oci_bind_by_name($stmt,':nstock', $nstock);
	oci_bind_by_name($stmt,':codProd', $codProd);
	oci_execute($stmt);
	oci_free_statement($stmt);
   }  
   function consultarVenta($con, $codVen){
   	$stmt = oci_parse($con,'SELECT * FROM ventas WHERE codigoVenta = :codVen');
	oci_bind_by_name($stmt,':codVen', $codVen);
	oci_execute($stmt);
	$venta = oci_fetch_array($stmt);
	oci_free_statement($stmt);
	return $venta;
   }
   function consultarTodasVentas($con){
   	$stmt = oci_parse($con,'SELECT * FROM ventas ORDER BY fechaVenta');
	oci_bind_by_name($stmt,':codVen', $codVen);
	oci_execute($stmt);
	oci_fetch_all($stmt, $lista, null, null, OCI_FETCHSTATEMENT_BY_ROW);
	oci_free_statement($stmt);
	return $lista;
   }
   function consultarVentasSocio($con, $numSoc){
   	$lista = array();
   	$stmt = oci_parse($con,'SELECT * FROM ventas WHERE numeroSocio = :numSoc');
	oci_bind_by_name($stmt,':numSoc', $numSoc);
	oci_execute($stmt);
	oci_fetch_all($stmt, $lista, null, null, OCI_FETCHSTATEMENT_BY_ROW);
	oci_free_statement($stmt);
	return $lista;
   }
   function consultarLineasDeVenta($con, $codVen){
   	$lista = array();
   	$stmt = oci_parse($con,'SELECT * FROM lineasVentas WHERE codigoVenta = :codVen');
	oci_bind_by_name($stmt,':codVen', $codVen);
	oci_execute($stmt);
	oci_fetch_all($stmt, $lista, null, null, OCI_FETCHSTATEMENT_BY_ROW);
	oci_free_statement($stmt);
	return $lista;
   }
	function modPagoReserva($con, $codVen, $pagado){
   	$stmt = oci_parse($con,'UPDATE ventas SET pagado = :pagado WHERE codigoVenta = :codVen');
	oci_bind_by_name($stmt,':codVen', $codVen);
	oci_bind_by_name($stmt,':pagado', $pagado);
   	oci_execute($stmt);
	oci_free_statement($stmt);
	}
?>