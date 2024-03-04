def clasficacion(L):
  if L <= 3:
    return "BEBE"
  elif L <= 14:
    return "NINO"
  elif L <= 18:
    return "JOVEN"
  elif L <= 65:
    return "ADULTO"
  else:
    return "ADULTO 3RA"

L = int(input())
print(clasficacion(L))