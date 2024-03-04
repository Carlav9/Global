compra = float(input())
descuento = 0
descuentototal = 0

# Lectura de datos
if compra < 500:
    print(compra)

elif compra >= 500 and compra <= 1000:
    descuento = compra * 0.05
    descuentototal = compra - descuento
    print(descuentototal)

elif compra > 1001 and compra <= 7000:
    descuento = compra * 0.11
    descuentototal = compra - descuento
    print(descuentototal)

elif compra >= 7001 and compra <= 15000:
    descuento = compra * 0.18
    descuentototal = compra - descuento
    print(descuentototal)

elif compra > 15000:
    descuento = compra * 0.25
    descuentototal = compra - descuento
    print(descuentototal)