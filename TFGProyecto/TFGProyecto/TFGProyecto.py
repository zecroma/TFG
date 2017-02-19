import BilinearMaps
import LSSS

ciclo1= BilinearMaps.BilinearMaps.cyclic(11)
ciclo2 = BilinearMaps.BilinearMaps.cyclic(7)

print("Ciclo 1: ")
print(ciclo1)

print("\n")

print("Ciclo 2: ")
print(ciclo2)

print("\n")

print("G x G -> Gt1: ")
print(BilinearMaps.BilinearMaps.e(ciclo1, ciclo1))

print("\n")

print("G x G -> Gt2: ")
print(BilinearMaps.BilinearMaps.e(ciclo2, ciclo2))

print("\n")

print("Propiedad bilineal: ")
print(BilinearMaps.BilinearMaps.bilinear(ciclo1))

print("\n")

print("Propiedad no degenerativa: ")
print(BilinearMaps.BilinearMaps.nonDegenerate(ciclo1))

print("\n")

print("Access structure: ")
print(LSSS.LSSS.accessStructure(ciclo2))
