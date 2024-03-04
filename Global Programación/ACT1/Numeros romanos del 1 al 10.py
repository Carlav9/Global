def into_roman(num):
    roman_map = {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII',
        9: 'IX',
        10: 'X'
    }
    res = ""
    if num >= 1 and num <= 10:
        for i, r in roman_map.items():
            if num == i:
                res = r
                break
    else:
        res = "El número debe ser >= 1 y <= 10"
    return res

try:
    num = int(input(""))
    print(into_roman(num))
except ValueError:
    print("Error, ingrese un número válido")
except EOFError:
    print("valor invalido")