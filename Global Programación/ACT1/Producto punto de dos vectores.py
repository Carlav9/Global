def producto(n, a, b):
  return sum(a[i]*b[i] for i in range(n))

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(producto(n, a, b))