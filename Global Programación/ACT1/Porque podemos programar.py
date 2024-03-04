def calcular_y(x):
  y = (x + x**2) / (5*x + 3)
  y = y * (y + x) / (y + 2*x)
  return y

y = float(input())
result = calcular_y(y)
print(round(result, 6))