<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
"http://www.w3.org/TR/html4/strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<LINK REL=StyleSheet HREF="bienvenida.css" TYPE="text/css" MEDIA=screen>
		<title>principal</title>
		<meta name="author" content="usuario" />
		<!-- Date: 2012-07-24 -->
	</head>
	<body>
		<div id="texto">Bienvenido a la aplicaci&oacute;n de "Un Libro M&aacute;s".</div>
		<?php
			$texto1 = "<div id='texto'><p>Los libros son amigos que nunca decepcionan- <strong>Thomas Carlyle</strong></p></div>";
			$texto2 = "<div id='texto'><p>Un libro es como un jardín que se lleva en el bolsillo- <strong>Proverbio árabe</strong></p></div>";
			$texto3 = "<div id='texto'><p>Hay un libro abierto siempre para todos los ojos: la naturaleza- <strong>Jean Jacques Rousseau </strong></p></div>";
			$texto4 = "<div id='texto'><p>Mis libros siempre están a mi disposición, nunca están ocupados- <strong>Marco Tulio Cicerón </strong></p></div>";
			$texto5 = "<div id='texto'><p>El recuerdo que deja un libro a veces es más importante que el libro en sí- <strong>Adolfo Bioy Casares </strong></p></div>";
			$texto6 = "<div id='texto'><p>Un libro abierto es un cerebro que habla; cerrado, un amigo que espera; olvidado, un alma que perdona; destruído, un corazón que llora- <strong>Proverbio hindú.</strong></p></div>";
			$texto7 = "<div id='texto'><p>La lectura de un buen libro es un diálogo incesante en que el libro habla y el alma contesta- <strong>André Maurois </strong></p></div>";
			$texto8 = "<div id='texto'><p>Para viajar lejos, no hay mejor nave que un libro- Emily Dickinson </p></div>";
			$texto9 = "<div id='texto'><p>Un libro, como un viaje, se comienza con inquietud y se termina con melancolía- <strong>José Vasconcelos </strong></p></div>";
			$texto0 = "<div id='texto'><p>Algunos libros son probados, otros devorados, poquísimos masticados y digeridos- <strong>Sir Francis Bacon </strong></p></div>";
			mt_srand (time());
			$numero_aleatorio = mt_rand(0,9); 
			switch ($numero_aleatorio) {
				case 1: echo "$texto1";
					
					break;
				case 2: echo "$texto2";
					
					break;
				case 3: echo "$texto3";
					
					break;
				case 4: echo "$texto4";
					
					break;
				case 5: echo "$texto5";
					
					break;
				case 6: echo "$texto6";
					
					break;
				case 7: echo "$texto7";
					
					break;
				case 8: echo "$texto8";
					
					break;
				case 9: echo "$texto9";
					
					break;
				case 0: echo "$texto0";
					
					break;
				default: echo "$texto0";
					
					break;
			}
		?>
	</body>
</html>