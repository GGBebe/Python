# 1. Kullanıcı gireceği ders sayısını dirmeli
lessonCount = 0
while lessonCount <= 0 or lessonCount >10:
    lessonCount = int(input("Ders sayısını giriniz: "))



# 2. Girilen ders satısı kadar 2 adet soru sorulmalı
# (1. ders için vize notu giriniz, 1. ders için final notu giriniz.)


passedLessons = 0
failedLessons = 0
#i = 0
#while i < lessonCount:
for i in range(lessonCount):
    lessonExam = float(input(f"{i+1}. ders için vize notunu giriniz: "))
    lessonFinal = float(input(f"{i+1}. ders için vize notunu giriniz: "))
    lessonAverage = (lessonExam*.4) + (lessonFinal*.6)
    if lessonAverage >= 50:
        passedLessons += 1
    else:
        failedLessons += 1
# i++
print(f"{passedLessons} adet dersten geçtiniz. {failedLessons} adet dersten kaldınız.")


