<?php
	function conectar()
	{
		$con = oci_connect('trabajo', 'trabajo', 'localhost/XE');
		if (!$con) {
    		$e = oci_error();
    		trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
		}
		return $con;
	}
	
	function desconectar($con){
		oci_close($con);
	}
?>
