def umumiy_sozlar(matn1, matn2):
    sozlar1 = set(matn1.split())
    sozlar2 = set(matn2.split())
    umumiy_sozlar = sozlar1 & sozlar2
    return umumiy_sozlar

matn1 = input("Birinchi matnni kiriting: ")
matn2 = input("Ikkinchi matnni kiriting: ")

umumiy_sozlar = umumiy_sozlar(matn1, matn2)
print("Umumiy so'zlarni quyidagilar: ", umumiy_sozlar)
