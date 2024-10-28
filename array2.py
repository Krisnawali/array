matriks = []

print("masukan elemen untuk matriks 3x3:")
for i in range(3):
    baris =[]
    for j in range(3):
        nilai = int(input(f"masukan elemen baris (i+1), kolom {j+1}: "))
        baris.append(baris)
    matriks.append(baris)

transpose = []
for i in range(3):
    baris =[]
    for j in range(3):
        baris.append(matriks[j][i])
    transpose.append(baris)

print("\nHasil transpose matriks:")
for baris in transpose:
    print(baris)