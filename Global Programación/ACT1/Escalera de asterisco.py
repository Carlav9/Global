n = int(input())
letra = '#'
for i in range(1, n + 1):
    for j in range(i):
        print(letra, end='')
    print()