import pytest
from bolum2 import sifre_gucu, otopark_ucreti, yuzde_degisim

def test_sifre_gucu_bos_hata():
    with pytest.raises(ValueError):
        sifre_gucu("")

def test_sifre_gucu_zayif():
    assert sifre_gucu("1234567") == "zayıf"

def test_sifre_gucu_orta():
    assert sifre_gucu("12345678") == "orta"
    assert sifre_gucu("12345678901") == "orta"

def test_sifre_gucu_guclu():
    assert sifre_gucu("123456789012") == "güçlü"
    assert sifre_gucu("cokguclubirsifre") == "güçlü"

def test_otopark_ucreti_negatif_hata():
    with pytest.raises(ValueError):
        otopark_ucreti(-5)

def test_otopark_ucreti_ucretsiz():
    assert otopark_ucreti(0) == 0
    assert otopark_ucreti(15) == 0

def test_otopark_ucreti_20tl():
    assert otopark_ucreti(16) == 20
    assert otopark_ucreti(60) == 20

def test_otopark_ucreti_40tl():
    assert otopark_ucreti(61) == 40
    assert otopark_ucreti(180) == 40

def test_otopark_ucreti_60tl():
    assert otopark_ucreti(181) == 60
    assert otopark_ucreti(500) == 60

def test_yuzde_degisim_sifir_hata():
    with pytest.raises(ValueError):
        yuzde_degisim(0, 100)

def test_yuzde_degisim_hesaplamalar():
    assert yuzde_degisim(200, 250) == pytest.approx(25.0)
    assert yuzde_degisim(200, 150) == pytest.approx(-25.0)
    assert yuzde_degisim(100, 100) == pytest.approx(0.0)
