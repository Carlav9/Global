n = int(input())
tot = 0.0
notas = (float(x) for x in input().split())
for nota in notas:
  tot += nota
prom = tot / n
est = "Aprobado" if prom >= 7 else "Reprobado"
print(est)