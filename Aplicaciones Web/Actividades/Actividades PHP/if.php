<?php
$edad = $_GET["edad"];

if ($edad <= -1)
{
echo "Los numeros negativos no cuentan";
}

elseif ($edad <= 3)
{
echo "Es un infante";
}

elseif ($edad <= 17)
{
echo "Es un niño";
}

elseif ($edad <= 64)
{
echo "Es un adulto";
}

elseif ($edad >= 65)
{
echo "Es un señor";
}
?>
