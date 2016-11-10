# -*- coding: utf-8 -*-

def get_kalimat():
    """Return string"""

    semarang_wiki = "Kota Semarang (Hanacaraka: ꦑꦸꦛꦯꦼꦩꦫꦁ) adalah ibukota Provinsi Jawa Tengah, Indonesia sekaligus kota metropolitan terbesar kelima di Indonesia sesudah Jakarta, Surabaya, Bandung, dan Medan."

    return semarang_wiki


def preprocess(kalimat):
    """Return list of kata"""

    kalimat = kalimat.lower()
    kalimat = kalimat.split()
    for idx, kata in enumerate(kalimat):
        kalimat[idx] = kata.strip("(:)")
    
    return kalimat


def frekuensi_kata(kalimat):
    frek = 0
    for kata in kalimat:
        frek += 1
    
    return frek

def main():
    semarang_wiki = get_kalimat()
    semarang = preprocess(semarang_wiki)
    frekuensi = frekuensi_kata(semarang)

    with open('freq.txt', 'w', encoding='utf8') as f:
        kalimat = "Kalimat : \n{0}\n".format(semarang_wiki)
        f.write(kalimat)
        frekuensi = "Frekuensi Kata : {0}".format(frekuensi)
        f.write(frekuensi)

if __name__ == '__main__':
    main()