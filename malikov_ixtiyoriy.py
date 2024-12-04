# -*- coding: utf-8 -*-
"""Malikov ixtiyoriy

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15AY1VHHlFIL81nFW6jHvWdP4LRiTmirZ
"""

def Malikov_investor(belgi):
    if belgi == "Bitcoin":
        return "96 689.12$"
    elif belgi == "Ethereum":
        return "3 858.20$"
    elif belgi == "Binance Coin":
        return "763.96$"
    elif belgi == "Bitcoin Cash":
        return "572.17$"
    elif belgi == "Toncoin":
        return "7.12$"
    elif belgi == "Solana":
        return "236.23$"
    elif belgi == "AVAX":
        return "56.23$"
    elif belgi == "Cosmos":
        return "10.46$"
    elif belgi == "Filecoin":
        return "8.24$"
    elif belgi == "Cardano":
        return "1.20$"
    elif belgi == "EOS":
        return "1.41$"
    elif belgi == "Arbitrum":
        return "1.17$"
        #Crypto valyutalarda kurs o'ynab turadi.
    else:
        return "https://bank.uz/uz/crypto-currency saytiga murojaat qiling"

belgi = input("Crypto valyuta nomini kiriting: ")
natija = Malikov_investor(belgi)
print(natija)

pip install opencv-python

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("photo_2024-10-16_22-58-07.jpg")
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("WIN_20240502_11_15_27_Pro.jpg")
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

import matplotlib.pyplot as plt
import numpy as np

days = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
prices = [25000, 25500, 26000, 27000, 26500, 27500, 28000]  # USD qiymatlar

plt.figure(figsize=(10, 5))
plt.plot(days, prices, marker='o', color='red', linestyle='-', label='Bitcoin kursi')
plt.title("Bitcoin kursi (haftalik)")
plt.xlabel("Kunlar")
plt.ylabel("Narx (USD)")
plt.grid(True)
plt.legend()
plt.show()