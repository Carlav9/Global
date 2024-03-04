def convertir_fecha(fecha):
  dia, mes, year = fecha.split('/')
  year = int(year)
  if year >= 74:
    year += 1900
  else:
    year += 2000
  return f"{dia}/{mes}/{year}"

fechas = []
counter = 0

while counter < 4:
  fecha = input()
  if fecha == "salir":
    break
  fecha_convertida = convertir_fecha(fecha)
  fechas.append(fecha_convertida)
  counter += 1

for fecha_convertida in fechas:
  print(fecha_convertida)