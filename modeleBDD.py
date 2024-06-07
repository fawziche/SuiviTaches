import datetime

class EtatProjet:
    def __init__(self):
        self.id = 0
        self.etat = ""


class TypeProjet:
    def __init__(self):
        self.id = 0
        self.type = ""


class Projet:
    def __init__(self):
        self.id = 0
        self.nom = ""
        self.type_id = 0
        self.etat_id = 0
        self.charge = 0.00
        self.tempsPasse = 0.00
        self.descriptif = ""
        self.remarque = ""


class Taches:
    def __init__(self):
        self.id = 0
        self.date = datetime.date.today()
        self.projet_id = 0
        self.tempsPasse = 0
        self.tempsPrevu = 0
        self.description = ""
