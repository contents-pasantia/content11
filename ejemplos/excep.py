def palindrome(word):
  return word == word[::-1]

# print(palindrome(1))
# print(palindrome(''))

"""
try:
  print(palindrome(1))
except TypeError:
  print("Solo se aceptan cadenas")
"""

#---race
def palindrome_race(word):
  try:
    if len(word) == 0:
      raise ValueError (" No se puede ingresar una cadena vacia")
    return word == word[::-1]
  except ValueError as ve:
    print(ve)
    return False

try:
  print(palindrome_race('radar'))
except TypeError:
  print("solo se puede ingresar strings")
finally:
  print('fin del programa')