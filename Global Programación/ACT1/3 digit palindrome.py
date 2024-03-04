def es_palindromo(numero):
  str_numero = str(numero).zfill(3)
  if str_numero[0] == str_numero[-1]:
    return True
  else:
    return False

numero = int(input())
print(es_palindromo(numero))