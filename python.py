class Student:
    def __init__(self, jmeno, vek, predmety=None, znamky=None):
        self.jmeno = jmeno
        self.vek = vek
        self.predmety = predmety if predmety else []
        self.znamky = znamky if znamky else []

    def pridej_predmet(self, predmet):
        self.predmety.append(predmet)

    def ziskej_prumer(self):
        if not self.znamky:
            return 0
        return sum(self.znamky) / len(self.znamky)

    def pridej_znamku(self, znamka):
        self.znamky.append(znamka)

    def informace(self):
        print(f"Jméno: {self.jmeno}, Věk: {self.vek}, Předměty: {self.predmety}, Průměr: {self.ziskej_prumer()}")

class Teacher:
    def __init__(self, jmeno, vek, predmet, studenti=None):
        self.jmeno = jmeno
        self.vek = vek
        self.predmet = predmet
        self.studenti = studenti if studenti else []

    def pridat_studenta(self, student):
        self.studenti.append(student)

    def odebrat_studenta(self, student):
        self.studenti.remove(student)

    def informace(self):
        print(f"Jméno: {self.jmeno}, Věk: {self.vek}, Předmět: {self.predmet}, Studenti: {len(self.studenti)}")

student1 = Student("Jaroslav Melichar", 18)
student1.pridej_predmet("PRC")
student1.pridej_znamku(1)
student1.pridej_znamku(3)
student1.informace()


student2 = Student("Filip Dubček", 19)
student2.pridej_predmet("PRC")
student2.pridej_znamku(1)
student2.pridej_znamku(5)
student2.informace()

teacher1 = Teacher("Karolína Marešová", 25, "PRC,AG")
teacher1.pridat_studenta(student1)
teacher1.pridat_studenta(student2)

teacher2 = Teacher("Martin Kokeš", 29, "WP,SES")
teacher2.pridat_studenta(student1)
teacher2.pridat_studenta(student2)

print("\nInformace o učiteli:")
teacher1.informace()
teacher2.informace()
