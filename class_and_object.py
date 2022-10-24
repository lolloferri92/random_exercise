#definition of main class student
class student:
    def __init__(self,name,lastname,course):
        print("oggetto studente creato\n")
        self.name=name
        self.lastname=lastname
        self.course=course
#for the student class is defined the name, the lastname and the course

    def get_name(self):
        print(self.name)
    def get_lastname(self):
        print(self.lastname)
    def get_course(self):
        print(self.course)
# getter method

    def personal_information(self,append=""):
        print("Scheda Studente\n Nome: " +self.name+"\n Cognome: " +self.lastname+"\n Corso Di Studi: "+self.course + append)
#this funcition is for print the general information of the student

studente_uno=student("pippo","sempronio","algebra")
studente_uno.get_name()
studente_uno.personal_information()

#this class is a son of student class
class laureandi(student):
    def __init__(self,name,lastname,course,date):
        super().__init__(name,lastname,course)
        self.date=date
        print("\noggetto laureando creato")

    def get_date(self):
        print("la data inserita è " + self.date)

    def personal_information(self):
        super().personal_information("\n la data di laurea é " +self.date)

input("cominciao")
studente_due=laureandi("carlo","caio","fisica","38")
studente_due.get_date()
studente_due.get_name()
studente_due.personal_information()
input("ti è piaciuto")



