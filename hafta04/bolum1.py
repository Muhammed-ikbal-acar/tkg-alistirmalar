# 1. Vize-final sonucu
def vize_final_sonuc(vize, final):
    ortalama = vize * 0.4 + final * 0.6
    if ortalama >= 50 and final >= 50:
        return "Geçti"
    else:
        return "Kaldı"

# 2. Asal sayı mı?
def asal_mi(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# 3. Palindrom mu?
def palindrom_mu(metin):
    temizlenmis = metin.lower().replace(" ", "")
    return temizlenmis == temizlenmis[::-1]

# 4. En uzun kelime
def en_uzun_kelime(cumle):
    if not cumle:
        return ""
    kelimeler = cumle.split()
    en_uzun = kelimeler[0]
    for kelime in kelimeler:
        if len(kelime) > len(en_uzun):
            en_uzun = kelime
    return en_uzun

# 5. En düşük not (HATALIYDI -> DÜZELTİLDİ: Başlangıç değeri düzeltildi)
def en_dusuk_not(notlar):
    if len(notlar) == 0:
        return None
    en_dusuk = notlar[0]  # Hata buradaydı: 0 yerine listedeki ilk eleman olmalı
    for n in notlar:
        if n < en_dusuk:
            en_dusuk = n
    return en_dusuk

# 6. 1'den n'ye kadar toplam (HATALIYDI -> DÜZELTİLDİ: range bitiş değeri düzeltildi)
def toplam(n):
    sonuc = 0
    for i in range(1, n + 1):  # Hata buradaydı: 'n' dahil olması için 'n + 1' yapıldı
        sonuc = sonuc + i
    return sonuc
