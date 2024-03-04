def fraccion(n, m):
  a = n // m
  b = n % m
  if b != 0:
    return f"{a} {b}/{m}"
  else:
    return str(a)

n, m = map(int, input("").split())
print(fraccion(n, m))