# Alıştırma 4: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest -v

import pytest

from alistirma import indirim_orani, sepet_toplami, en_pahali_urun


def test_sepet_toplami():
    sepet = [
        {"urun": "çay", "fiyat": 20, "adet": 2},
        {"urun": "simit", "fiyat": 15, "adet": 3},
        {"urun": "tost", "fiyat": 60, "adet": 1},
    ]
    assert sepet_toplami(sepet) == 145

@pytest.mark.parametrize("tutar, beklenen", [
    (0, 0),     
    (99, 0),     
    (100, 5),     
    (499, 5),
    (500, 10),   
    (999, 10),
    (1000, 15),  
    (1500, 15)
])
def test_indirim_orani(tutar, beklenen):
    assert indirim_orani(tutar) == beklenen

def test_indirim_orani_negatif():
  
    with pytest.raises(ValueError):
        indirim_orani(-10)

def test_sepet_toplami_bos():
    
    assert sepet_toplami([]) == 0

def test_sepet_toplami():
    sepet = [
        {"urun": "çay", "fiyat": 20, "adet": 2},   
        {"urun": "simit", "fiyat": 15, "adet": 3},
        {"urun": "tost", "fiyat": 60, "adet": 1},
    ]
    assert sepet_toplami(sepet) == 145

@pytest.mark.parametrize("hatali_adet", [0, -2])
def test_sepet_toplami_gecersiz_adet(hatali_adet):
    
    sepet = [{"urun": "çay", "fiyat": 20, "adet": hatali_adet}]
    with pytest.raises(ValueError):
        sepet_toplami(sepet)

def test_en_pahali_urun_bos():
    assert en_pahali_urun([]) is None

def test_en_pahali_urun_normal():
    sepet = [
        {"urun": "su", "fiyat": 5, "adet": 1},
        {"urun": "çay", "fiyat": 20, "adet": 1},
        {"urun": "kahve", "fiyat": 20, "adet": 1}, 
        {"urun": "pasta", "fiyat": 15, "adet": 1}
    ]
   
    assert en_pahali_urun(sepet) == "çay"
