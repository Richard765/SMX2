<?php
echo "Ejercicio 1";
$precio=283;
$descuento= 15;
$resultado= $precio - ($precio * $descuento) / 100;
echo "<br>";
echo $resultado; 

echo "<br>";

$precio2=653;
$iva=21;
$resultado2= $precio2 + ($precio2 * $iva) / 100;
echo "<br>";
echo $resultado2; 

echo "<br>";
echo "<br>";
echo "Ejercicio 2";
$descuento2= 5;
$resultadonofinal= $precio2 - ($precio2 * $descuento2) / 100;
$resultado3= $resultadonofinal + ($resultadonofinal * $iva) /100;
echo "<br>";
echo $resultado3;
echo "<br>";
echo "<br>";
$interes= 5;
$tiempo= 3;
$interessimple1= ($precio2 * $interes * $tiempo) / 100;
$interessimple2= ($precio2 * $interes * ($tiempo * 4)) / 100;
$precio3=$precio;
$precio4=$precio;
echo "$interessimple1<br>";
echo $interessimple2;
?>