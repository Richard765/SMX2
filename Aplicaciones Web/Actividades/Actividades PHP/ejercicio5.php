<?php
for ($num = 1; $num <= 100; $num++) {
if ($num % 15 == 0) {
echo "Baja del carro", "<br>";
}

elseif ($num % 5 == 0) {
echo "Esto no", "<br>";
}

elseif ($num % 3 == 0) {
echo "Esto si", "<br>";
}

else {
echo $num, "<br>";
}
}
?>

