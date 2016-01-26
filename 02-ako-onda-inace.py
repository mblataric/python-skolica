# Ovdje ćemo vježbati logičke operatore
# Što su logički operatori? To su pitanja "Ako je nešto, onda napravi ovo inače napravi ono".
# Primjerice, Ako je broj veći od 10, onda ispiši "Broj je veći od 10", inače ispiši "Broj nije veći od deset"
# U Pythonu, ali i mnogim drugim jezicima, logički operatori se odazivaju na imena IF ... ELSE
# Pa evo prvo nekoliko primjera.

# U varijablu (ladicu) broj unijet ćemo neki broj.
broj = int(input("Unesi neki broj: "))

# Sada ćemo provjeriti nekoliko raspona u kojem se broj nalazi.

rezultat = ""

if broj < 0:
    rezultat = "Broj je negativan."
else:
    rezultat = "Broj je pozitivan"

print(rezultat)

# Primjeti kako je linija poslije if i poslije else UVUČENA.
# To je JAKO bitno jer to označava da se te linije izvršavaju samo ako je uvjet u IF-u zadovoljen
# Odnosno, ako nije zadovoljen, onda se izvršava kod uvučen ispod ELSE
# Sljedeći primjer će pokazati kako može biti više linija ispod IF i ELSE - jedino je važno da budu uvijek jednako uvučeni

# Ovdje također ima primjer kako se broj pretvara u tekst pomoću str()
# Kako smo kod učitavanja broj morali koristiti int() da bi tekst pretvorili u broj, tako sada ovdje broj moramo
# pretvoriti u tekst pomoću str() kako bi ga mogli naljepiti u ostatak rečenice

print("\n**** Jednostavni uvjet ***")
if broj < 0:
    rezultat = "Broj " + str(broj) + " je negativan"
    print(rezultat)
else:
    rezultat = "Broj " + str(broj) + " je pozitivan"
    print(rezultat)


# IF-ovi se mogu i spajati. Recimo, Ako je broj manji od 0 onda napravi ovo, inače, ako je manji od 10 napravi nešto drugo,
# a inače napravi nešto treće.
# Za to se koristi komanda IF ... ELIF ... ELSE

print("\n**** Program s dobrim uvjetima ***")

if broj < 0:
    print("Broj je negativan")

elif broj < 10:
    print("Broj je pozitivan, ali je manji od 10")

elif broj < 100:
    print("Broj je pozitivan, ali je manji od 100")

else:
    print("Broj je pozitivan i veći je od 100")

# Primjeti da je redosljed uvjeta jako bitan. Ako bi uvjete napisali naopako i broj bi bio manji od 100, svi uvjeti bi bili zadovoljeni
# Za primjer, napisat ćemo isti uvjet, ali obrnuto da vidiš kako je redosljed bitan, odnosno kako treba razmisliti kako će se uvjeti postaviti
# Ukoliko upišemo negativan broj, program će ispisati prvi uvjet (jer je manji od 100), ali to nije ono što smo htjeli
#   pa možemo reći da ovaj program ima grešku (ili bug) jer ima loše postavljen uvjet

print("\n**** Program s lošim uvjetima ***")

if broj < 100:
    print("Broj je pozitivan, ali je manji od 100")

elif broj < 10:
    print("Broj je pozitivan, ali je manji od 10")

elif broj < 0:
    print("Broj je negativan")

# U svaki IF se može staviti i više uvjeta. Primjer:

print ("\n**** Više uvjeta u svakom IF-u ***")

if broj < 0:
    print("Broj je negativan")

elif broj > 0 and broj <= 10:
    print ("Broj je između 0 i 10")

elif broj > 10 and broj <= 100:
    print ("Broj je između 10 i 100")

elif broj > 100:
    print ("Broj je veći od 100")

# ZADATAK 1
# Iz prethodnog sata uzmi program koji računa kubikažu i kvadraturu tvoje i mamine i tatine sobe
# Spremi kvadrature i kubikaže u posebne varijable (posebno za tvoju, a posebno za njihovu sobu)
# Provjeri čija soba ima veću kvadraturu. Ako ima tvoja ispiši "Ou yeah, imam veću sobu!"
# Ako je njihova veća, ispiši "No, normalno da su si tata i mama zeli vekšu sobu!"
# Onda provjeri kubikažu. Ako je tvoja veća, ispiši "Dišem punim plućima!"
# Ako je njihova kubikaža veća, ispiši "Kašlj, kašlj, idem disat u susjednu sobu gdje ima više zraka"

# ZADATAK 2
# Upiši dva broj i spremi ih u varijable
# Ako je prvi broj veći, oduzmi ih i ispiši "Prvi broj je veći, a zbroj je ", prviBroj + drugiBroj
# Ako je drugi broj veći, zbroji ih i ispiši "Drugi broj je veći, a razlika je " drugiBroj - prviBroj
# Ako su brojevi jednaki, pomnoži ih, "Brojevi su jednaki - kvadrat broja ", prviBroj, "jednako je" prviBroj * drugiBroj


# ZADATAK 3
# Pitaj "Koliko imaš godina" i spremi u varijablu
# Ako je upisani broj:
#   - manji od 0, ispiši "Ne glupiraj se, nitko nema manje od nula godina"
#   - veći od nula, a manji ili jednak 2, ispiši "Oooo, pa ti si još beba"
#   - veći od 2, ali manji ili jednak 5, ispiši "Pelene, vrtić, vrtić, pelene - tu si negdje!"
#   - veći od 5, ali manji ili jednak od 10, ispiši "No, ideš u školu. I kaj sad, misliš da si faca?!"
#   - veći od 10, ali manji od 15, ispiši "Dobro, malo si narasao - sad misliš da si velika faca?!"
#   - veći od 15, ali manji od 20, ispiši "Ne pravi se važan, bolje gledaj kud hodaš!"
#   - veći od 20, ali manji od 30, ispiši "Odi si nađi posao već jednom!"
#   - veći od 30, ali manji od 80, ispiši "Sorry, sa starcima ne razgovaram"
#   - veći od 80, ali manji od 90, ispiši "Kaaaj, ti si još žiiiv, kaaak?!"
#   - veći od 100, ispiši "Oh ne, trebam doktora. Mislim da razgovaram s mrtvacima!"