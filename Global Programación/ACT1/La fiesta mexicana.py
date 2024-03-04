def calcular_comida(N, M):
  try:
    diferencia = N - M
    if diferencia < 0:
      print(f"{diferencia}\nLO SIENTO NO ALCANZA LA COMIDA")
    elif diferencia > 0:
      print(f"{diferencia}\nTIENE UN TUPPER PARA LLEVAR?")
    else:
      print(f"{diferencia}\nESTAMOS COMPLETOS")
  except ValueError:
    print("Error")

try:
  N = int(input())
  M = int(input())
  calcular_comida(N, M)
except ValueError:
  print("Error")