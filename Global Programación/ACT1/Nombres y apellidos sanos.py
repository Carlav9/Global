def reorganizar_nombre(nombre):
  partes = nombre.split()
  if len(partes) not in [2, 3, 4]:
    return '*'
  if len(partes) == 2:
    return ' '.join(partes[::-1])
  elif len(partes) == 3:
    return ' '.join([partes[-1]] + partes[:-1])
  elif len(partes) == 4:
    return ' '.join(partes[2:] + partes[:2])

while True:
  try:
    nombre = input()
    if len(nombre) > 40:
      print("Por favor ingrese un nombre con no más de 40 caracteres")
    else:
      print(reorganizar_nombre(nombre))
  except EOFError:
    break