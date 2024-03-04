def son_adyacentes(a, b):
  if abs(a - b) == 1 or (a == 1 and b == 100) or (a == 100 and b == 1) or (a == 100 and b == 2) or (a == 2 and b == 100):
    return "SI"
  else:
    return "NO"

T = int(input())
for _ in range(T):
  a, b = map(int, input().split())
  print(son_adyacentes(a, b))