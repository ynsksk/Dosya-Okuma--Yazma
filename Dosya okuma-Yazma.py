	#'r'==>"okuma"
	#'w'==>"yazmaya yarar fakat dosya yoksa dosya olu�turur
dosya varsa olan dosyay� siler"
	#'a'==>"yazmaya yarar dosya dosya var ise d�zenleme yapar"
	#'x'==>"yazmaya yarar dosya yoksa hata verir dosya var ise
d�zenleme yapar"
	#'r+'==>"okuma ve yazmaya yarar dosya var olmas� gerekir"
	#'w+'==>"okuma ve yazmaya yarar dosya var ise siler"
	#'a+'==>"okuma ve yazmaya yarar"
	#'x+'==>"okuma ve yazmaya yarar dosya varsa hata verir"
		#�rnek 1
	#Burda dosya yoksa a�ar var ise siler ve "merhaba yunus" yazar
	#with kullanmam�z�n amac� dosyay� kapatmay� unutursan
	python kendili�inden kapat�r
with open("yunus.txt","w") as dosya:
	dosya.write("merhaba yunus")
		#�rnek 2 
	#dosyan�n ba��na veri girmeye yarar
with open("yunus.txt","r+") as dosya:
    data=dosya.read()
    dosya.seek(0)#dosyan�n 0.index ine seek yard�m�yla ula�abiliyoruz
    data="nas�ls�n\n" + data #veriyi ba�a yazmak i�in son verilerle toplanmal�
    dosya.write(data)
		#�rnek 3
	#dosyan�n ortas�na veri girme
with open("yunus.txt","r+") as dosya:
    data=dosya.readlines()
    dosya.seek(0)
    data.insert(1,"nerelerdesin hi� g�remedim seni\n")
#insert ile ka��nc� index e veri yazac���n�z� g�sterir
    dosya.writelines(data)
	