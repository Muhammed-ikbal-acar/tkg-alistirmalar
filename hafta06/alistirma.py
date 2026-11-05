# Alıştırma 5: Bu dosyadaki kod ÇALIŞIYOR ama kötü yazılmış.
#
# Sizin işiniz kodu temizlemek:
#   - ruff check hiçbir sorun bulmamalı,
#   - ruff format dosyayı değiştirmemeli,
#   - test_alistirma.py'deki testlerin hepsi geçmeli.
# Fonksiyonların adlarını ve ne yaptıklarını değiştirmeyin; yalnızca nasıl
# yazıldıklarını değiştirin. Her fonksiyonun üstündeki açıklama, ne yapması
# gerektiğini (şartnameyi) anlatıyor.


# 1. Bilet fiyatı
# - Yaş negatifse ValueError fırlatır.
# - 6 yaşından küçükler ücretsizdir (0 TL).
# - Hafta içi bilet 100 TL, hafta sonu 150 TL.
# - Öğrencilere 30 TL indirim yapılır.
def bilet_fiyati(yas, ogrenci, hafta_sonu):
    if yas < 0:
        raise ValueError("yaş negatif olamaz")
    if yas < 6:
        return 0

    fiyat = 150 if hafta_sonu else 100
    
    if ogrenci:
        fiyat -= 30
        
    return fiyat


def not_ortalamasi(notlar):
    if not notlar:
        return None
    return sum(notlar) / len(notlar)


def ortalama_metni(notlar):
    ort = not_ortalamasi(notlar)
    if ort is None:
        return "not yok"
    return str(round(ort, 1))


def gecti_mi(puan):
    return puan >= 50


def sayiya_cevir(metin):
    try:
        return int(metin)
    except ValueError:
        return None


def katilimci_ekle(ad, liste=None):
    if liste is None:
        liste = []
    liste.append(ad)
    return liste
