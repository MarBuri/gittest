"""clovek1 = ["Petr","Novák","Olomouc",779 00,True]
clovek2 = ["Pavel","Malý","Prostějov",775 44,True]
clovek3 = ["Jan","Velký","Přerov",False]

zamestnanci = [clovek1,clovek2,clovek3]

for clovek in zamestnanci
    print(clovek[1])
"""

#key - value pair --> slovník

#zamestnanec1 = {"name": "John","age":30,"city":"NY"}

#print(zamestnanec1)


"""zamestnanec2 = {
    "name": "Marry",
    "age": 27,
    "city": "Paris",
}"""

#print(zamestnanec2)

#založení slovníků
muj_novy_slovnik = {}
#založení množiny
moje_mnozina = set()
print(muj_novy_slovnik)
muj_novy_slovnik["jmeno"] = "Lukas"
print(muj_novy_slovnik)
muj_novy_slovnik["ridicak"] = True
muj_novy_slovnik["hobby"] = ("fotbal", "hry", "zahálka", "spánek")
muj_novy_slovnik["vek"] = 22
muj_novy_slovnik["jmeno"] = "Matej"
print(muj_novy_slovnik)

print(muj_novy_slovnik["jmeno"])
print(muj_novy_slovnik["hobby"][0])

#ZÁKLADNÍ METODY

print(muj_novy_slovnik.keys())
print(muj_novy_slovnik.values())
print(muj_novy_slovnik.items())

student = {
    "name": "John",
    "age": 25,
    "courses": ["Math","Compsi"]
}

for value in student.values():
    print(value)