def clasificar_caracter(caracter):
  if caracter in 'AEIOU':
    return 'V'
  elif caracter == 'Y':
    return 'S'
  else:
    return 'C'

def main():
  count = 0
  resultados = []
  caracteres = input().split()
  for caracter in caracteres:
    if caracter.isupper():
      resultados.append(clasificar_caracter(caracter))
      count += 1
      if count == 10:
        break
  print(' '.join(resultados))

main()