# Deklarasi array untuk menyimpan nilai
nilai_siswa = []

# Meminta input nilai dari pengguna
for i in range(5):
    nilai = float(input(f"masukan nilai siswa ke-{i+1}: "))
    nilai_siswa.append(nilai)

# menghtung total nilai
total_nilai = sum(nilai_siswa)

# menghitung rata-rata
rata_rata = total_nilai / len(nilai_siswa)

# ,enampilkan hasil rata-rata
print(f"Rata-rata nlai siswa adalah: {rata_rata}")