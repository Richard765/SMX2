<?php
$nom = $_GET['nom'];
$edat = $_GET['edat'];
$ara = date('Y');
$fechafinal = 2050 - $ara;
$edatfinal = $fechafinal + $edat;
echo $nom, " tendra " , $edatfinal, " en el año 2050."; 

$fechaactual = strtotime ('Y-m-d');
$fecha2050 = strtotime ('2050-01-01');
$diasrestantes = floor
?>
