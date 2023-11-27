arr = ["Macia", "Juan", "Jose", "Ernesto"]

var_a_encontrar = input("¿Que nombre estas buscando? ")

def busqueda_while(arr, var_a_encontrar):
    encontrado = False
    busqueda = 0
    while busqueda < len(arr) and not encontrado:
        if arr[busqueda] == var_a_encontrar:
            encontrado = True
        else:
            busqueda += 1
    return encontrado

def busqueda_for(arr, var_a_encontrar):
    for busqueda in arr:
        if busqueda == var_a_encontrar:
            return True
    return False

def recorrido_while(arr):
    recorrido = 0
    while recorrido < len(arr):
        print(arr[recorrido])
        recorrido += 1

def recorrido_for(arr):
    for recorrido in arr:
        print(recorrido)

print("---Busqueda while---")
print(busqueda_while(arr, var_a_encontrar))

print("---Busqueda for---")
print(busqueda_for(arr, var_a_encontrar))

print("---Recorrido while---")
recorrido_while(arr)

print("---Recorrido for---")
recorrido_for(arr)