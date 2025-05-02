def esPalindromo(cadena):
    # Utilizaremos esta variable para almacenar nuestra cadena sin espacios
    cadena_form = ""
    # Recorremos la cadena, si el caraccter es alfabetico lo ponemos en minñuscula, si es espacio lo saltamos
    # en otro caso devolvemos falso ya que no es un palíndromo.
    for c in cadena:
        if c.isalpha():
            cadena_form = cadena_form + c.lower()
        elif c == " ":
            pass
        else:
            return False
    principio = 0  # Posición del primer carácter de la cadena
    final = len(cadena_form) - 1  # Posición del último carácter de la cadena
    # Vamos comparando los caracteres en estas dos posiciones mientras no se crucen.
    # En el momento que encontremos dos caracteres distintos podemos dejar de comparar ya
    # que la frase no es palíndromo. Si se cruzan los dos pivotes es que la frase es palíndromo.
    # Suponemos que una cadena vacía es un palíndromo.
    while final > principio:
        if cadena_form[principio] != cadena_form[final]:
            return False
        final -= 1
        principio += 1
    return True


# En caso de que este script se utilice como programa principal solicitamos los datos al usuario.
if __name__ == "__main__":
    cadena = input("Introduzca la cadena a estudiar:")
    if esPalindromo(cadena):
        print("La cadena es un palíndromo.")
    else:
        print("La cadena no es un palindromo.")
