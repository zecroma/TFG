import BilinearMaps

ciclo1= BilinearMaps.BilinearMaps.cyclic(11)
ciclo2 = BilinearMaps.BilinearMaps.cyclic(13)

print("Ciclo 1: ")
print(ciclo1)

print("\n")

print("G x G -> Gt: ")
print(BilinearMaps.BilinearMaps.e(ciclo1,11))