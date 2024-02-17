# creamos la función para invertir las mayúsculas
def invert_case(cadena):
    if type(cadena) is not str:  # nos aseguramenos de que la cadena sea un str
        estado = -16
        return (estado, None)  # imprimimos el código de error único y None
    elif cadena == "":  # verifica que no sea un str vacío
        estado = -48
        return (estado, None)
    elif cadena.isalpha() is False:  # ve que solo contenga letras del abc
        estado = -32
        return (estado, None)
    else:  # comienza proceso de inversión
        estado = 0
        lista = []  # crea una lista para guardar las letras invertidas
        for i in range(len(cadena)):
            if cadena[i].islower():  # verifica si la letra es minúscula
                lista.append(cadena[i].upper())
            else:
                lista.append(cadena[i].lower())
        cadena_final = "".join(lista)  # une las letras invertidas
        return (estado, cadena_final)


def numero_primo(numero):
    if type(numero) is int:  # verifica que sea entero
        if (numero <= 100):  # verifica que sea menor a 100
            lista_primos = []  # hace una lista con los primos
            cont = 0
            for i in range(2, numero+1):
                for j in range(2, int(i/2)+1):
                    if i % j == 0:
                        cont += 1
                if cont == 0:
                    lista_primos.append(i)  # une los primos
                cont = 0
            estado = 0
            return (estado, lista_primos)
        else:
            estado = -80
            return (estado, None)
    else:
        estado = -64
        return (estado, None)
