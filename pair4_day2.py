vize = float(input("Vize Notunuzu Giriniz: "))
if vize > 100:
    print("100'den aşağı bir sayı giriniz!")
else:
    final = float(input("Final Notunuzu Giriniz: "))
    if final > 100:
        print("100'den aşağı bir sayı giriniz!")
    else:
        average = (vize*(.4))+(final*(.6))
        print(f"Ders ortalamanız: {average}")
        if average < 50 and average >= 0:
            print("FF aldınız!")
        elif average < 60 and average >=50:
            print("DD aldınız!")
        elif average < 70 and average >=60:
            print("CC aldınız!")
        elif average < 80 and average >=70:
            print("BB aldınız!")
        else:
            print("AA aldınız!")