<?php
    function insertarSocio($con, $nombre, $sexo, $edad, $telefono, $correo, $dir, $vip, $fechaIn, $finSan, $fnaci){
    	$stmt = oci_parse($con, 'SELECT sec_nso.NEXTVAL FROM dual');
		oci_execute($stmt);
		$row = oci_fetch_row($stmt);
		$numSoc = $row[0];
		oci_free_statement($stmt);
    	$stmt = oci_parse($con,'INSERT INTO socios (numeroSocio, nombre, sexo, edad, telefono, correo, direccion, vip, fechaIngreso, fechaFinSancion, fechaNacimiento) VALUES (:id, :nom, :sexo, :edad, :telefono, :correo, :dir, :vip, :fechaIn, :finSan, :fnaci)');
		oci_bind_by_name($stmt, ':id', $numSoc);
		oci_bind_by_name($stmt,':nom', $nombre);
		oci_bind_by_name($stmt,':sexo', $sexo);
		oci_bind_by_name($stmt,':edad', $edad);
		oci_bind_by_name($stmt,':telefono', $telefono);
		oci_bind_by_name($stmt,':correo', $correo);
		oci_bind_by_name($stmt,':fechaIn', $fechaIn);
		oci_bind_by_name($stmt,':dir', $dir);
		oci_bind_by_name($stmt,':vip', $vip);
		oci_bind_by_name($stmt,':finSan', $finSan);
		oci_bind_by_name($stmt,':fnaci', $fnaci);
		oci_execute($stmt);
		oci_free_statement($stmt);
		return $numSoc;
    }
	function modificarSocio($con, $numero, $nombre, $sexo, $edad, $telefono, $correo, $dir, $vip, $fechaIn, $finSan, $fnaci){
		$stmt = oci_parse($con,'UPDATE socios SET nombre = :nom, sexo = :sexo, edad =:edad, telefono = :telefono, correo = :correo, direccion = :dir, vip = :vip, fechaIngreso = :fechaIn, fechaFinSancion = :finsan, fechaNacimiento = :fnaci WHERE numeroSocio = :numero');
		oci_bind_by_name($stmt,':numero', $numero);
		oci_bind_by_name($stmt,':nom', $nombre);
		oci_bind_by_name($stmt,':sexo', $sexo);
		oci_bind_by_name($stmt,':edad', $edad);
		oci_bind_by_name($stmt,':telefono', $telefono);
		oci_bind_by_name($stmt,':correo', $correo);
		oci_bind_by_name($stmt,':fechaIn', $fechaIn);
		oci_bind_by_name($stmt,':dir', $dir);
		oci_bind_by_name($stmt,':vip', $vip);
		oci_bind_by_name($stmt,':finSan', $finSan);
		oci_bind_by_name($stmt,':fnaci', $fnaci);
		oci_execute($stmt);
		oci_free_statement($stmt);
	}
	function eliminarSocio($con, $numero){
		$stmt = oci_parse($con,'DELETE FROM socios WHERE numeroSocio = :numero');
		oci_bind_by_name($stmt,':numero', $numero);
		oci_execute($stmt);
		oci_free_statement($stmt);
	}
	function consultarUnSocio($con, $numero){
		$stmt = oci_parse($con,'SELECT * FROM socios WHERE numeroSocio = :numero');
		oci_bind_by_name($stmt,':numero', $numero);
		oci_execute($stmt);
		$result = oci_fetch_array($stmt);
		oci_free_statement($stmt);
		return $result;
	}
	function consultarTodosSocios($con){
		$stmt = oci_parse($con,'SELECT * FROM socios ORDER BY numeroSocio');
		oci_execute($stmt);
		oci_fetch_all($stmt, $lista, null, null, OCI_FETCHSTATEMENT_BY_ROW);
		oci_free_statement($stmt);
		return $lista;
	}
?>