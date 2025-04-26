# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
print("Salom! Bu oddiy kalkulyator.")

# 1. Foydalanuvchidan ikkita son olish
son1 = float(input("Birinchi sonni kiriting: "))
amal = input("Amalni kiriting (+, -, *, /): ")
son2 = float(input("Ikkinchi sonni kiriting: "))

# 2. Hisoblash
if amal == "+":
    natija = son1 + son2
elif amal == "-":
    natija = son1 - son2
elif amal == "*":
    natija = son1 * son2
elif amal == "/":
    if son2 != 0:
        natija = son1 / son2
    else:
        natija = "0 ga bo‘lish mumkin emas!"
else:
    natija = "Noto‘g‘ri amal!"

# 3. Natijani chiqarish
print("Natija:", natija)






  
        
        
        


    