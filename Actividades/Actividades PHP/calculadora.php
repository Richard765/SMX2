<!DOCTYPE html>
<html>
<head>
    <style>
        .estilo {
            text-align: center;
            margin-top: 400px;
            font-size: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="estilo">
<?php
$op1 = $_GET['op1'];
$op2 = $_GET['op2'];
$operacion = $_GET['operacion'];

if (is_numeric($op1) && is_numeric($op2)) {
switch ($operacion) { 

case "suma":
$suma = $op1 + $op2;
echo $suma;
break;

case "resta":
$resta = $op1 - $op2;
echo $resta;
break;

case "multiplicacion":
$multiplicacion = $op1 * $op2;
echo $multiplicacion;
break;

case "division":
if ($op2 == 0) {
 echo "No se puede dividir entre 0";
} else {
$division = $op1 / $op2;
echo $division;
}
break;

default:
echo "Algo has hecho mal";
break;
}
} else {
 echo "No se puede colocar letras/simbolos en una " ,$operacion;
}
?>
    </div>
</body>
</html>
