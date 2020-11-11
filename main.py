class Kategoria:
  def __init__(self, sor):
    self.nev = sor[0]
    self.tulelokSzama = int(sor[1])
    self.eltuntekSzama = int(sor[2])

kategoriak = []

for sor in open("titanic.txt"):
  kategoriak.append(Kategoria(sor.split(';')))

#for k in kategoriak: print(k.nev)

#második feladat:
print(f"2. feladat: {len(kategoriak)} db")

#harmadik feladat:
sum = 0
for k in kategoriak:
  sum += k.tulelokSzama + k.eltuntekSzama
print(f"3. feladat: {sum} fő")

#ötödik feladat:
def otodik(keresett):
  print("5. feladat:")
  for k in kategoriak:
    if keresett in k.nev:
      print(f"\t{k.nev}: {k.tulelokSzama + k.eltuntekSzama} fő")

#negyedik feladat:
keresett = input("4. feladat: Kulcsszó: ")
i = 0
while i < len(kategoriak):
  if keresett in kategoriak[i].nev:
    print("\tVan találat!")
    otodik(keresett)
    break
  i += 1
else:
  print("\tNincs találat!")

#hatodik feladat:
print("6. feladat:")
for k in kategoriak:
  if k.eltuntekSzama > (k.eltuntekSzama + k.tulelokSzama) * 0.6:
    print(f"\t{k.nev}")

#hetedik feladat:
maxi = 0
for i in range(len(kategoriak)):
  if kategoriak[maxi].tulelokSzama < kategoriak[i].tulelokSzama:
    maxi = i

print(f"7. feladat: {kategoriak[maxi].nev}")