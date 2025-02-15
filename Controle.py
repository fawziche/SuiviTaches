from BDD import *
from Utilitaires import *



class Ctrl_EtatProjet(BDD_EtatProjet):
    def __init__(self):
        try:
            super().__init__()

        except Exception as err:
            raise Exception(err.args[0])


    def ajouterEtat(self, arEtatProjet):
        try:
            if arEtatProjet.etat is None or arEtatProjet.etat == "":
                raise Exception ("Ctrl - Etat - ajout : l'état n'est pas renseigné !")
            else:
                tmp_id = super().lireEtatProjetviaEtat(arEtatProjet).id 
                if tmp_id > 0:
                    raise Exception ("Ctrl - Etat - ajout : cet état existe déjà (id = " + str(tmp_id) + ") !")
                else:                
                    arEtatProjet.etat = arEtatProjet.etat.upper()
                    super().ajouterEtat(arEtatProjet)
        
        except Exception as err:
            raise Exception(err.args[0])
    

    def majEtat(self, arEtatProjet):
        try:
            if arEtatProjet.etat is None or arEtatProjet.etat == "":
                raise Exception ("Ctrl - etat - maj : l'état n'est pas renseigné pour l'ID = " + arEtatProjet.id + " !")
            else:
                arEtatProjet.etat = arEtatProjet.etat.upper()
                super().majEtat(arEtatProjet)
        
        except Exception as err:
            raise Exception(err.args[0])
    



class Ctrl_TypeProjet(BDD_TypeProjet):
    def __init__(self):
        try:
            super().__init__()

        except Exception as err:
            raise Exception(err.args[0])
        

    def ajouterType(self, arTypeProjet):
        try:
            if arTypeProjet.type is None or arTypeProjet.type == "":
                raise Exception ("Ctrl - type - ajout : le type n'est pas renseigné !")
            else:
                tmp_id = super().lireTypeProjetviaType(arTypeProjet).id 
                if tmp_id > 0:
                    raise Exception ("Ctrl - type - ajout : ce type existe déjà (id = " + str(tmp_id) + ") !")
                else:   
                    arTypeProjet.type = arTypeProjet.type.upper()
                    super().ajouterType(arTypeProjet)

        except Exception as err:
            raise Exception(err.args[0])


    def majType(self, arTypeProjet):
        try:
            if arTypeProjet.type is None or arTypeProjet.type == "":
                raise Exception ("Ctrl - type - maj : le type n'est pas renseigné pour l'ID = " + arTypeProjet.id + "' !")
            else:
                arTypeProjet.type = arTypeProjet.type.upper()
                super().majType(arTypeProjet)

        except Exception as err:
            raise Exception(err.args[0])
        



class Ctrl_Projet(BDD_Projet):
    def __init__(self):
        try:
            super().__init__()

        except Exception as err:
            raise Exception(err.args[0])
        

    def ajouterProjet(self, arProjet):
        try:
            if arProjet.nom is None or arProjet.nom == "":
                raise Exception ("Ctrl - projet - ajout : le nom du projet n'est pas renseigné !")
            elif not Utilitaires.estUnFloat(arProjet.charge):  
                raise Exception(f"Ctrl - projet - ajout : La charge '{arProjet.charge}' n'est pas numérique pour l'ID = " + str(arProjet.id) + "' !")
            elif not Utilitaires.estUnFloat(arProjet.tempsPasse):
                raise Exception(f"Ctrl - projet - ajout : Le temps passé '{arProjet.tempsPasse}' n'est pas numérique pour l'ID = " + str(arProjet.id) + "' !")
            else:
                super().ajouterProjet(arProjet)

        except Exception as err:
            raise Exception(err.args[0])


    def majProjet(self, arProjet):
        try:
            if arProjet.nom is None or arProjet.nom == "":
                raise Exception ("Ctrl - projet - maj : le projet n'est pas renseigné pour l'ID = " + str(arProjet.id) + "' !")
            elif not Utilitaires.estUnFloat(arProjet.charge):
                raise Exception(f"Ctrl - projet - maj : La charge '{arProjet.charge}' n'est pas numérique pour l'ID = " + str(arProjet.id) + "' !")
            elif not Utilitaires.estUnFloat(arProjet.tempsPasse):
                raise Exception(f"Ctrl - projet - maj : Le temps passé '{arProjet.tempsPasse}' n'est pas numérique pour l'ID = " + str(arProjet.id) + "' !")
            else:
                super().majProjet(arProjet)

        except Exception as err:
            raise Exception(err.args[0])




class Ctrl_Tache(BDD_Tache):
    def __init__(self):
        try:
            super().__init__()

        except Exception as err:
            raise Exception(err.args[0])
        

    def ajouterTache(self, arTache):
        try:
            if arTache.date is None:
                raise Exception ("Ctrl - tache - ajout : la date n'est pas renseignée !")
            elif not Utilitaires.estUnFloat(arTache.tempsPasse):  
                raise Exception(f"Ctrl - tache - ajout : Le temps passé '{arTache.tempsPasse}' n'est pas numérique !")
            elif not Utilitaires.estUnFloat(arTache.tempsPrevu):
                raise Exception(f"Ctrl - tache - ajout : Le temps prévu '{arTache.tempsPrevu}' n'est pas numérique !")
            else:
                super().ajouterTache(arTache)

        except Exception as err:
            raise Exception(err.args[0])


    def majTache(self, arTache):
        try:
            if arTache.date is None:
                raise Exception ("Ctrl - tache - maj : la date n'est pas renseignée pour l'ID = " + str(arTache.id) + "' !")
            elif not Utilitaires.estUnFloat(arTache.tempsPasse):
                raise Exception(f"Ctrl - tache - maj : Le temps passé '{arTache.tempsPasse}' n'est pas numérique pour l'ID = " + str(arTache.id) + "' !")
            elif not Utilitaires.estUnFloat(arTache.tempsPrevu):
                raise Exception(f"Ctrl - tache - maj : Le temps prévu '{arTache.tempsPrevu}' n'est pas numérique pour l'ID = " + str(arTache.id) + "' !")
            else:
                super().majTache(arTache)

        except Exception as err:
            raise Exception(err.args[0])