"""
==============================
Nama        : Ayu R
NIM         : A11.2019.11654
Kelompok    : A11.4118
Tanggal     : 19-10-2019
==============================
"""
biner = input("masukkan nilai biner :")
panjang = len(biner)
pangkat = 0
desimal = 0
while panjang > 0 :
    panjang -= 1
    string = biner[panjang]
    if string == 1 or string == "1" :
        nilai = 2 ** pangkat
    else :
        nilai = 0
    pangkat += 1
    desimal += nilai
print("nilai desimal dari biner", biner, "adalah", desimal)