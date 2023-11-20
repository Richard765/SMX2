#!/bin/bash
# prova pel càlcul
# de la lletra del DNI  a través
# de bashscript.
clear
#
# Emplenam una llista (array) amb els valors de les 23 posicions de les lletres
#
lletra=(T R W A G M Y F P D X B N J Z S Q V H L C K E)
#
# Crees una funció per a comptar la longitud de la cadena introduïda per l' usuari
function longitud() {
long=$(echo $1 | wc -m)
}
# Comptam tants elements hi ha al nostre array i l'emmagatzemam
total=${#lletra[*]}
# Inicialitzam la variable del control del bucle
control='0'
# Mentres que no indiquem el contrari, se executarà el bucle...
while [ $control -eq 0 ] ;
do
# Ara sol·licitam el DNI sense la lletra del NIF
read -p "Introdueixi els seu núm de DNI SENSE la lletra: " dni
longitud $dni
if [ $long -ne 9 ];
then
echo "La longitud del número introduït no és correcta."
echo "Si la xifra introduïda és inferior a 8 xifres, posa un zero a l'esquerra."
echo "Si és superior, fes-t'ho mirar..."
control='0'
else
# Dividim el nostre DNI pel total d'elements de l'array
divi=`expr $dni \/ $total`
# Multiplicam el resultat un altre pic pel total d'elements
multi=`expr $divi \* $total`
# Restam al nostre DNI el resultat de l'anterior operació
resta=`expr $dni - $multi`
# Y així obtenim la lletra, que ens ajudarà a calcular la posició de l'array
echo " _____________________________________________________"
echo ""
echo " La lletra que correspon al teu DNI és ${lletra[$resta]} "
sleep 1
echo ""
echo " El teu NIF és $dni-${lletra[$resta]}"
echo "______________________________________________________"
echo
control='1'
fi
done
