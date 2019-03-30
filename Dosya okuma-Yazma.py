	#'r'==>"okuma"
	#'w'==>"yazmaya yarar fakat dosya yoksa dosya oluþturur
dosya varsa olan dosyayý siler"
	#'a'==>"yazmaya yarar dosya dosya var ise düzenleme yapar"
	#'x'==>"yazmaya yarar dosya yoksa hata verir dosya var ise
düzenleme yapar"
	#'r+'==>"okuma ve yazmaya yarar dosya var olmasý gerekir"
	#'w+'==>"okuma ve yazmaya yarar dosya var ise siler"
	#'a+'==>"okuma ve yazmaya yarar"
	#'x+'==>"okuma ve yazmaya yarar dosya varsa hata verir"
		#örnek 1
	#Burda dosya yoksa açar var ise siler ve "merhaba yunus" yazar
	#with kullanmamýzýn amacý dosyayý kapatmayý unutursan
	python kendiliðinden kapatýr
with open("yunus.txt","w") as dosya:
	dosya.write("merhaba yunus")
		#örnek 2 
	#dosyanýn baþýna veri girmeye yarar
with open("yunus.txt","r+") as dosya:
    data=dosya.read()
    dosya.seek(0)#dosyanýn 0.index ine seek yardýmýyla ulaþabiliyoruz
    data="nasýlsýn\n" + data #veriyi baþa yazmak için son verilerle toplanmalý
    dosya.write(data)
		#örnek 3
	#dosyanýn ortasýna veri girme
with open("yunus.txt","r+") as dosya:
    data=dosya.readlines()
    dosya.seek(0)
    data.insert(1,"nerelerdesin hiç göremedim seni\n")
#insert ile kaçýncý index e veri yazacýðýnýzý gösterir
    dosya.writelines(data)
	