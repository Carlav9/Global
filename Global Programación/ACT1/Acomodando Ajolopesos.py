def ordenar_monedas(monedas):
  monedas_validas = [0.50, 1, 2, 5, 10]
  monedas_ordenadas = sorted([moneda for moneda in monedas if moneda in monedas_validas], reverse=True)
  return ' '.join(format(moneda, '.2f') if moneda == 0.50 else str(int(moneda)) for moneda in monedas_ordenadas)

n = int(input(""))
monedas = [float(input("")) for _ in range(n)]

formato_monedas = []
for moneda in monedas:
  if moneda.is_integer():
    formato_monedas.append(int(moneda))
  else:
    formato_monedas.append(round(moneda, 2))

print(ordenar_monedas(formato_monedas))