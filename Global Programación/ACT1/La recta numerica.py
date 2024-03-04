def posicion_en_recta_numerica(a, b):
  diferencia = a - b
  if diferencia < 0:
    return 'Izquierda'
  elif diferencia > 0:
    return 'Derecha'
  else:
    return 'Centro'

a, b = map(int, input().split())
print(posicion_en_recta_numerica(a, b))