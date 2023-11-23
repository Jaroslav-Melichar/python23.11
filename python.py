class Student:
    def __init__(self, jmeno, prijmeni, hodnoceni, predmet=None):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.hodnoceni = hodnoceni
        self.predmet = predmet if predmet else []

    def info(self):
        print(f"Jméno: {self.jmeno}, příjmení: {self.prijmeni}, hodnocení: {self.hodnoceni}, předmět: {self.predmet}")

    def znamka(self):
        if self.hodnoceni > 90:
            print("Výborně")
        elif self.hodnoceni > 70:
            print("Dobře")
        elif self.hodnoceni > 50:
            print("Prospěl")
        else:
            print("Neprospěl")

    def add_predmet(self, predmet):
        self.predmet.append(predmet)

class Teacher:
    def __init__(self, jmeno, predmet):
        self.jmeno = jmeno
        self.predmet = predmet

    def add_hodnoceni(self, student, hodnoceni):
        student.hodnoceni.append(hodnoceni)

student1 = Student("Jan", "Novák", 80)
student1.info()
student1.znamka()
student1.add_predmet("Math")
student1.info() 