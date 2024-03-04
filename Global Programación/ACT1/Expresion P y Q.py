def verificar_expresion(p, q):
  if p**3 + q**4 - 2*p**2 < 680:
    print(p)
    print(q)

try:
  p, q = map(int, input("").split())
  verificar_expresion(p, q)
except ValueError:
  print("")