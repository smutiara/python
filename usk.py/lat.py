#fungsi ascending
def urutasc(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                simpan=a[j]
                a[j]=a[j+1]
                a[j+1]=simpan
    print(a)

#fungsi Descending
def urutdesc(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]<a[j+1]:
                simpan=a[j]
                a[j]=a[j+1]
                a[j+1]=simpan
    print(a)
    
while True:
    print("=================================")
    print("Program Mengurutkan Data")
    print("Menggunakan metode bubble short")
    print("=================================")

    angka1 = int(input("Masukkan angka 1 : "))
    angka2 = int(input("Masukkan angka 2 : "))
    angka3 = int(input("Masukkan angka 3 : "))
    angka4 = int(input("Masukkan angka 4 : "))
    angka5 = int(input("Masukkan angka 5 : "))

    print("Silahkan pilih pengurutan : ")
    print("1. Ascending")
    print("2. Descending")

    bil = [angka1, angka2, angka3, angka4, angka5]
    print("==============================: ")
    pilih = input("Metode yang dipilih : ")
    print("Data sebelum diurutkan : ")
    print(bil)
    print('- Nilai Maksimal : ', max(bil))
    print('- Nilai Minimal : ', min(bil))
    print('- Nilai Rerata : ', sum(bil) / len(bil))
    print("Data sesudah diurutkan : ")
    if pilih == "1":
        urutasc(bil)
    elif pilih == "2":
        urutdesc(bil)
    else:
        print("Pilihan tidak ada")
    print("==============================: ")
    # Input pengulangan
    menu=input("Kembali ke menu awal (Y/N)?")

    #pilihan pengulangan, Ya atau No
    if menu=="N" or menu=="n":
        print("Selesai, Terimakasih!")
        break
    elif menu!="Y" and menu!="y":
        print("Pilihan tidak ada!")
        break

