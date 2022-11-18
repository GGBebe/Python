#number = 1/0
#print("Hello world")

#exception
#handled exception

try:
    examNote = float(input("Lütfen sınav notunuzu giriniz: "))
    print(examNote)
    #number = 1/0
except ValueError:
    print("ValueError DENEME")
except ZeroDivisionError:
    print("Hiç bir sayı 0'a bölünemez")
except:
    print("Doğru bir girdi girmediniz...")
finally: #!her türlü çalışacak olan blok
    print("Try except bloğu sona erdi..")


