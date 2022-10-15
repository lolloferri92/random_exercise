class studente:
    def _init_(self,nome,cognome,corso_di_studi):
        self.nome=nome
        self.cognome=cognome
        self.corso_di_studi=corso_di_studi

    def scheda_personale(self):
        return f"Scheda Studente\n Nome:{self.nome}\n Cognome:{self.cognome}\n Corso Di Studi:{self.corso_di_studi}"

studente_uno=studente("pippo","sempronio","algebra")
print(studente_uno.scheda_personale())



