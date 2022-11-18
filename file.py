file = open("sample.txt", "r")
#farklı dizinde bir dosya olsa önünde yolu belirtilmeli. 
# w = write manasına geliyor. 
# a = append (ekleme yapıyor)
# \n alt satır
# r = readable
# "r+" "a+b" etc.
#! birden fazla girilebilir mi. Ayrı dosyalar mı açılmalı.

#file.writelines("\ndeneme 123")
print(file.read())

file.close()

#! bir şirket çalışanların verilerini tutan dosya oluşturulacak
#! kullanıcıdan çalışan sayısı alınacak
#! çalışan sayısı kadar isim, soyisim, maaş bilgisi alınacak
#!dosyadaki her satıra "Ad Soyad - Maaş" kalıbında çalışan bilgisi eklenecek.
#! Programın sonunda bu dosyadan bilgileri satır satır okuyup lisleyecek kod yazılacak.
#? kaç kişi ise ona göre isim soy isim maaş bilgisi isteyecek ve alt satıra geçecek. 
#! eklenen çalışanlar mevcut çalışanları silmeyecek üzerine yazılacak (append)
#! hata yakalama işlemleri unutulmamalı. maaş için kullanıcı ASD girebilir.. 