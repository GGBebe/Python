lessonCount = 0
while lessonCount <= 0 or lessonCount >10:
    lessonCount = int(input("Ders sayısını giriniz: "))

#passedLessons = 0
#failedLessons = 0

passedLessons_rev = []
failedLessons_rev = []
passedLessonsExams = []
passedLessonsFinals = []
failedLessonsExams = []
failedLessonsFinals = []

for i in range(lessonCount):
    lessonExam = float(input(f"{i+1}. ders için vize notunu giriniz: "))
    if lessonExam > 100:
        print("100'den aşağı bir sayı giriniz!")
    else:
        lessonFinal = float(input(f"{i+1}. ders için final notunu giriniz: "))
        if lessonFinal > 100:
            print("100'den aşağı bir sayı giriniz!")
        else:
            lessonAverage = (lessonExam*.4) + (lessonFinal*.6)
            if lessonAverage >= 50:
                passedLessons_rev.append(lessonAverage)
                passedLessonsExams.append(lessonExam)
                passedLessonsFinals.append(lessonFinal)
                #passedLessons += 1
            else:
                failedLessons_rev.append(lessonAverage)
                failedLessonsExams.append(lessonExam)
                failedLessonsFinals.append(lessonFinal)
                #failedLessons += 1

#print(f"{passedLessons} adet dersten geçtiniz. {failedLessons} adet dersten kaldınız.")
print(f"{passedLessons_rev} ortalama notları ile {len(passedLessons_rev)} dersten geçtiniz. {failedLessons_rev} ortalama notları ile {len(failedLessons_rev)} dersten kaldınız.")
print(f"Geçtiğiniz derslerin vize notları: {passedLessonsExams}, Geçtiğiniz derslerin final notları: {passedLessonsFinals}.\nKaldığınız derslerin vize notları: {failedLessonsExams}, kaldığınız derslerin final notları: {failedLessonsFinals}.")

