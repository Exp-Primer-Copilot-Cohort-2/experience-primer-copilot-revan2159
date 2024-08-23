# buatkan program yang bisa menghitung jumlah kata dalam sebuah kalimat
# contoh:
# input: "aku adalah anak gembala"
# output: 4

def hitung_kata(kalimat):
    return len(kalimat.split())

kalimat = "aku adalah anak gembala"
print(hitung_kata(kalimat))

