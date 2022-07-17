# sintaxis lambda argumentos: expresion

def palindromo_func(cadena):
    return cadena == cadena[::-1]

palindromo = lambda cadena: cadena == cadena[::-1]

print(palindromo('radar'))
print(palindromo('ana'))
print(palindromo('casa'))

print(palindromo_func('radar'))