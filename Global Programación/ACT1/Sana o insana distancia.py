import math

def estado_distancia(xa, ya, xb, yb):
  distancia = math.sqrt((xb - xa)**2 + (yb - ya)**2)
  if distancia >= 150:
    return "sana"
  else:
    return "insana"

xa, ya, xb, yb = map(int, input("").split())
print(estado_distancia(xa, ya, xb, yb))