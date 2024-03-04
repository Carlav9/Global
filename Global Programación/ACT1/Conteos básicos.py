def contar_de_a_b(a, b):
  for i in range(a, b+1):
    print(i)

a, b = map(int, input().split())
contar_de_a_b(a, b)