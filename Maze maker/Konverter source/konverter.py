failinimi = input ("Sisesta lähtefaili nimi: ")
uusfail= input ("Siseta väljundfaili nimi: ")
fail = open (failinimi, encoding = "UTF-8" )
andmed = fail.read()
fail.close()
andmed = andmed.replace("\t", "")[:-1]


fail = open (uusfail, "w", encoding = "UTF-8")
fail.write(andmed)
fail.close()