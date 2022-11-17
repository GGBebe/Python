lessonCount = 0
while lessonCount <= 0 or lessonCount >10:
    lessonCount = int(input("Ders sayısını giriniz: "))

passedLessons = 0
failedLessons = 0

for i in range(lessonCount):
    lessonExam = float(input(f"{i+1}. ders için vize notunu giriniz: "))
    lessonFinal = float(input(f"{i+1}. ders için vize notunu giriniz: "))
    lessonAverage = (lessonExam*.4) + (lessonFinal*.6)
    if lessonAverage >= 50:
        passedLessons += 1
    else:
        failedLessons += 1

print(f"{passedLessons} adet dersten geçtiniz. {failedLessons} adet dersten kaldınız.")


