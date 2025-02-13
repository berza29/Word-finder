# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:39:01 2025

@author: Lenovo
"""

import re

def kelime_bul(dosya_yolu, kelimeler):
    try:
   
        with open(dosya_yolu, "r", encoding="utf-8") as dosya:
            icerik = dosya.read().lower()  

        kelime_sayaci = {kelime: 0 for kelime in kelimeler}

        # Her kelimenin dosyada kaç kez geçtiğini hesapla
        for kelime in kelimeler:
            kelime_sayaci[kelime] = len(re.findall(rf'\b{kelime}\b', icerik))

        return kelime_sayaci

    except FileNotFoundError:
        print("Hata: Dosya bulunamadı.")
        return None


dosya_yolu = "6.0 AYŞBUL.pdf"  # Buraya dosya adını girin
kelimeler = ["python", "veri", "algoritma"]  # Aranacak kelimeler

sonuclar = kelime_bul(dosya_yolu, kelimeler)

if sonuclar:
    for kelime, sayi in sonuclar.items():
        print(f"'{kelime}' kelimesi {sayi} kez geçti.")

