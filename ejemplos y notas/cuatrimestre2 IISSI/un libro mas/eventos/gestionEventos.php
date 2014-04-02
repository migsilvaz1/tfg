<?php
    function insertarEvento($con, $nom, $fecha, $dur, $preEnt, $dir, $hora, $aforo, $vip){
    	$stmt = oci_parse($con, 'SELECT sec_ids.NEXTVAL FROM dual');
		oci_execute($stmt);
		$row = oci_fetch_row($stmt);
		$id = $row[0];
    	$stmt = oci_parse($con,'INSERT INTO eventos (id_evento, nombre, fecha, duracion, precioEntrada, direccion, hora, aforo, sitiosVip) VALUES (:id, :nom, :fecha, :dur, :preEnt, :dir, :hora, :aforo, :vip)');
		oci_bind_by_name($stmt,':id', $id);
		oci_bind_by_name($stmt,':nom', $nom);
		oci_bind_by_name($stmt,':fecha', $fecha);
		oci_bind_by_name($stmt,':dur', $dur);
		oci_bind_by_name($stmt,':preEnt', $preEnt);
		oci_bind_by_name($stmt,':dir', $dir);
		oci_bind_by_name($stmt,':hora', $hora);
		oci_bind_by_name($stmt,':aforo', $aforo);
		oci_bind_by_name($stmt,':vip', $vip);
		oci_execute($stmt);
		oci_free_statement($stmt);
    }
	function modificarEvento($con, $id, $nom, $fecha, $dur, $preEnt, $dir, $hora, $aforo, $vip){
		$stmt = oci_parse($con,'UPDATE eventos SET nombre = :nom, fecha = :fecha, duracion = :dur, precioEntrada = :preEnt, direccion = :dir, hora = :hora, aforo = :aforo, sitiosVip = :vip WHERE id_evento = :id');
		oci_bind_by_name($stmt,':nom', $nom);
		oci_bind_by_name($stmt,':fecha', $fecha);
		oci_bind_by_name($stmt,':dur', $dur);
		oci_bind_by_name($stmt,':preEnt', $preEnt);
		oci_bind_by_name($stmt,':dir', $dir);
		oci_bind_by_name($stmt,':hora', $hora);
		oci_bind_by_name($stmt,':aforo', $aforo);
		oci_bind_by_name($stmt,':vip', $vip);
		oci_bind_by_name($stmt,':id', $id);
		oci_execute($stmt);
		oci_free_statement($stmt);
	}
	function eliminarEvento($con, $id){
		$stmt = oci_parse($con,'DELETE FROM eventos WHERE id_evento = :id');
		oci_bind_by_name($stmt,':id', $id);
		oci_execute($stmt);
		oci_free_statement($stmt);
	}
	function consultarEvento($con, $nom){
		$lista = array();
		$stmt = oci_parse($con,'SELECT * FROM eventos WHERE nombre LIKE :nombre ORDER BY fecha');
		$nombre = "%".$nom."%";
		oci_bind_by_name($stmt,':nombre', $nombre);
		oci_execute($stmt);
		$check = oci_fetch_all($stmt, $lista, null, null, OCI_FETCHSTATEMENT_BY_ROW);
		oci_free_statement($stmt);
		return $lista;
	}
	function consPorFecha($con, $fecha){
		$stmt = oci_parse($con,'SELECT * FROM eventos WHERE fecha = :fecha');
		oci_bind_by_name($stmt,':fecha', $fecha);
		oci_execute($stmt);
		oci_fetch_all($stmt, $lista, null, null, OCI_FETCHSTATEMENT_BY_ROW);
		oci_free_statement($stmt);
		return $lista;
	}
	function consPorCod($con, $cod){
		$stmt = oci_parse($con,'SELECT * FROM eventos WHERE id_evento = :codigo');
		oci_bind_by_name($stmt,':codigo', $cod);
		oci_execute($stmt);
		$result = oci_fetch_array($stmt);
		oci_free_statement($stmt);
		return $result;
	}
	function apuntarAEvento($con, $socio, $id){
		$stmt = oci_parse($con,'INSERT INTO relEveSoc (id_evento, numeroSocio) VALUES (:id, :socio)');
		oci_bind_by_name($stmt,':id',$id);
		oci_bind_by_name($stmt,':socio',$socio);
		oci_execute($stmt);
		oci_free_statement($stmt);
	}
	function quitarDeEvento($con, $socio, $id){
		$stmt = oci_parse($con,'DELETE FROM relEveSoc WHERE id_evento = :id AND numeroSocio = :numero');
		oci_bind_by_name($stmt,':id', $id);
		oci_bind_by_name($stmt,':numero', $socio);
		oci_execute($stmt);
		oci_free_statement($stmt);
	}
	function consultarSociosApuntados($con, $nom){
		$stmt = oci_parse($con,'SELECT * FROM eventos WHERE nombre = :nombre');
		oci_bind_by_name($stmt,':nombre', $nom);
		oci_execute($stmt);
		$evento = oci_fetch_array($stmt);
		$id = $evento['ID_EVENTO'];
		oci_free_statement($stmt);
		$lista = array();
		$stmt = oci_parse($con,'SELECT * FROM relEveSoc WHERE id_evento = :id');
		oci_bind_by_name($stmt,':id',$id);
		oci_execute($stmt);
		oci_fetch_all($stmt, $lista, null, null, OCI_FETCHSTATEMENT_BY_ROW);
		oci_free_statement($stmt);
		$sol = array();
		for($n=0;$n<sizeof($lista);$n++){
			$linea = $lista[$n];
			$numSoc =$linea['NUMEROSOCIO'];
			$stmt = oci_parse($con,'SELECT * FROM socios WHERE numeroSocio = :numero');
			oci_bind_by_name($stmt,':numero', $numSoc);
			oci_execute($stmt);
			$result = oci_fetch_array($stmt);
			oci_free_statement($stmt);
			array_push($sol,$result);
		}
		return $sol;
	}
?>