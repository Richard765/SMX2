<?php
    $uno = 0;
    $dos = 0;
    $tres = 0;
    $cuatro = 0;
    $cinco = 0;
    $seis = 0;
    $unop = 0;
    $dosp = 0;
    $tresp = 0;
    $cuatrop = 0;
    $cincop = 0;
    $seisp = 0;

    function tirar($tiradas_max){
        global $uno, $dos, $tres, $cuatro, $cinco, $seis; 
        $tiradas = 0;
        while ($tiradas < $tiradas_max){
            $valor = rand(1, 6);
            if ($valor == 1){
                $uno += 1;
            } elseif ($valor == 2){
                $dos += 1;
            } elseif ($valor == 3){
                $tres += 1;
            } elseif ($valor == 4){
                $cuatro += 1;
            } elseif ($valor == 5){
                $cinco += 1;
            } elseif ($valor == 6){
                $seis += 1;
            }
            $tiradas += 1;
        }
    }

    function probabilidad($tiradas_max){
        global $uno, $dos, $tres, $cuatro, $cinco, $seis;
        global $unop, $dosp, $tresp, $cuatrop, $cincop, $seisp; 
        $unop = number_format(($uno / $tiradas_max) * 100, 2);
        $dosp = number_format(($dos / $tiradas_max) * 100, 2);
        $tresp = number_format(($tres / $tiradas_max) * 100, 2);
        $cuatrop = number_format(($cuatro / $tiradas_max) * 100, 2);
        $cincop = number_format(($cinco / $tiradas_max) * 100, 2);
        $seisp = number_format(($seis / $tiradas_max) * 100, 2);
    }
    

    if (isset($_POST["tiradas"])) {
        $tiradas_max = intval($_POST["tiradas"]);
        tirar($tiradas_max);
        probabilidad($tiradas_max);
    }
?>

<!DOCTYPE html>
<head>
    <title>Ejercicio dado</title>
</head>
<body>
    <h1>Tirar dado</h1>
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
        ¿Cuantas veces quieres tirar el dado? 
        <input type="number" name="tiradas" min="1" required>
        <input type="submit" value="Tirar">
    </form>

    <?php
        echo "<h2>Resultados:</h2>";
        echo "Uno: $unop%, Dos: $dosp%, Tres: $tresp%, Cuatro: $cuatrop%, Cinco: $cincop%, Seis: $seisp%";
    ?>
</body>
</html>