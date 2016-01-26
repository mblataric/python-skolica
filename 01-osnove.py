# Ispis podatka na ekran

# Ako želimo ispisati tekst, stavimo navodnike
# print ("Ovo je ispis teksta.")

# Ako želimo ispisati broj, stavimo bez navodnika
# print (3)

# Razlika između navodnika i bez:
# print ("3 + 2")
# print (3453534 + 543534532)

# Možemo i kombinirati tekst i brojeve
# print ("3 + 2", "Tekst '3 + 2': ")
# print ("3 plus 2 = ", 3 + 2)



# UNOS PODATAKA
# Podatke unosimo s komandom input
# U ovom podatku, unos spremimo u varijablu a koju poslije toga ispišemo

# a = input("Upiši svoje ime: ")

# print ("Tvoje ime je: ", a)


# ZADATAK 1
# Složi program koji će pitati koliko imaš godina. Nakon upisa,
# ispiši "Ti imaš <upisane godine> godina".
# NAPOMENA: <upisane godine> zamijeni s podatkom koji je upisan

#b = input("Koliko ti imas godina: ")
#print("ti imas",b,"godina")

# ZADATAK 2
# Složi program koji će pitati za ime tate i mame
# Nakon unosa ispiši: Tvoji roditelji se zovu <ime tate> i <ime mame>
# NAPOMENA: <ime tate> i <ime mame> zamijeni s upisanim podacima

#tata = input("Kako ti se tata zove: ")
#mama = input("Kako ti se zove mama: ")
#print("Tvoji roditelji se zovu",tata,"i",mama)

prviBroj = int(input("upiši prvi broj: "))
drugiBroj = int(input("upiši drugi broj: "))

print(prviBroj, "+", drugiBroj, "=", prviBroj + drugiBroj)
print(prviBroj, "-", drugiBroj ,"=", prviBroj - drugiBroj)
print(prviBroj, "*", drugiBroj, "=", prviBroj * drugiBroj)
print(prviBroj, "/", drugiBroj, "=", prviBroj / drugiBroj)