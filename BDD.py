import mysql.connector 
from modeleBDD import *



class BDD_EtatProjet():
    # On ouvre la connexion
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost",user="root",password="Saadia04", database="suiviTaches")
        except Exception as err:
            raise Exception(err.args[0])

    def cloreBDD(self):
        try:
            self.conn.close()
        except Exception as err:
            raise Exception(err.args[0])

    def ajouterEtat(self, arEtatProjet):
        try:
            cursor = self.conn.cursor()
            
            requete = """INSERT INTO tEtatProjet (etat) VALUES (%s)"""
            cursor.execute(requete, (arEtatProjet.etat,))
            self.conn.commit()

            # on loggue
            print("Etat ajouté : " + arEtatProjet.etat)

        except Exception as err:
            raise Exception("BDD - Etat - Ajout : " + err.args[0])


    def majEtat(self, arEtatProjet):
        try:
            cursor = self.conn.cursor()
            
            requete = """UPDATE tEtatProjet SET etat = (%s) WHERE id = (%s)"""
            cursor.execute(requete, (arEtatProjet.etat,arEtatProjet.id))
            self.conn.commit()

            print(f"etat maj -> {arEtatProjet.id} : {arEtatProjet.etat}")

        except Exception as err:
            raise Exception("BDD - Etat - maj : " + err.args[0])


    def deleteEtat(self, arEtatProjet):
        try:
            cursor = self.conn.cursor()
            
            requete = """DELETE FROM tEtatProjet WHERE id = (%s)"""
            cursor.execute(requete, (arEtatProjet.id,))
            self.conn.commit()

            print(f"etat delete -> {arEtatProjet.id}")

        except Exception as err:
            raise Exception("BDD - Etat - delete : " + err.args[0])


    def lireEtats(self):
        try:
            data = []

            cursor = self.conn.cursor()

            cursor.execute("""SELECT id, etat FROM tEtatProjet""")
            rows = cursor.fetchall()
            for row in rows:
                data.append((row[0], row[1]))

            return data
    
        except Exception as err:
            raise Exception("BDD - Etat - lireEtats : " + err.args[0])
    

    def lireEtatProjetviaEtat(self, arEtatProjet):
        try:
            unEtatProjet = EtatProjet()

            cursor = self.conn.cursor()
            requete = """SELECT id, etat FROM tEtatProjet WHERE etat = (%s)"""
            cursor.execute(requete, (arEtatProjet.etat,))
            rows = cursor.fetchall()
            for row in rows:
                unEtatProjet.id = int(row[0])
                unEtatProjet.etat = row[1]

            return unEtatProjet
    
        except Exception as err:
            raise Exception("BDD - Etat - lireEtat : " + err.args[0])


class BDD_TypeProjet():
    # On ouvre la connexsion
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost",user="root",password="Saadia04", database="suiviTaches")

        except Exception as err:
            raise Exception("BDD - Type - open : " + err.args[0])
        

    def cloreBDD(self):
        try:
            self.conn.close()

        except Exception as err:
            raise Exception("BDD - Type - Close : " + err.args[0])


    def ajouterType(self, arTypeProjet):
        try:
            cursor = self.conn.cursor()
            
            requete = """INSERT INTO tTypeProjet (Type) VALUES (%s)"""
            cursor.execute(requete, (arTypeProjet.type,))
            self.conn.commit()

            print(f"Type ajouté : {arTypeProjet.type}")

        except Exception as err:
            raise Exception("BDD - Type - ajout : " + err.args[0])


    def majType(self, arTypeProjet):
        try:
            cursor = self.conn.cursor()
            
            requete = """UPDATE tTypeProjet SET Type = (%s) WHERE id = (%s)"""
            cursor.execute(requete, (arTypeProjet.type,arTypeProjet.id))
            self.conn.commit()

            print(f"etat maj -> {arTypeProjet.id} : {arTypeProjet.type}")

        except Exception as err:
            raise Exception("BDD - Type - maj : " + err.args[0])
        

    def deleteType(self, arTypeProjet):
        try:
            cursor = self.conn.cursor()
            
            requete = """DELETE FROM tTypeProjet WHERE id = (%s)"""
            cursor.execute(requete, (arTypeProjet.id,))
            self.conn.commit()

            print(f"type delete -> {arTypeProjet.id}")

        except Exception as err:
            raise Exception("BDD - Type - delete : " + err.args[0])


    def lireTypes(self):
        try:
            data = []

            cursor = self.conn.cursor()

            cursor.execute("""SELECT id, Type FROM tTypeProjet""")
            rows = cursor.fetchall()
            for row in rows:
                data.append((row[0], row[1]))

            return data
        
        except Exception as err:
            raise Exception("BDD - Type - lireTypes : " + err.args[0])
    

    def lireTypeProjetviaType(self, arTypeProjet):
        try:
            unTypeProjet = TypeProjet()

            cursor = self.conn.cursor()
            requete = """SELECT id, Type FROM tTypeProjet WHERE type = (%s)"""
            cursor.execute(requete, (arTypeProjet.type,))
            rows = cursor.fetchall()
            for row in rows:
                unTypeProjet.id = int(row[0])
                unTypeProjet.type = row[1]

            return unTypeProjet
        
        except Exception as err:
            raise Exception("BDD - Type - lireType : " + err.args[0])

        

class BDD_Projet():
    # On ouvre la connexion
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost",user="root",password="Saadia04", database="suiviTaches")

        except Exception as err:
            raise Exception("BDD - Projet - Open : " + err.args[0])


    def cloreBDD(self):
        try:
            self.conn.close()

        except Exception as err:
            raise Exception("BDD - Projet - Close : " + err.args[0])
        

    def ajouterProjet(self, arProjet):
        try:
            cursor = self.conn.cursor()
            
            requete = """
                INSERT INTO tProjets (nom, type_id, etat_id, charge, tempsPasse, descriptif, remarque) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            data = (arProjet.nom, arProjet.type_id, arProjet.etat_id, arProjet.charge, arProjet.tempsPasse, arProjet.descriptif, arProjet.remarque)
            cursor.execute(requete, data)
            self.conn.commit()

            print(f"Projet ajouté : {data}")
            
        except Exception as err:
            raise Exception("BDD - Projet - ajout : " + err.args[0])
        

    def majProjet(self, arProjet):
        try:
            cursor = self.conn.cursor()
            
            requete = """
                UPDATE tProjets SET nom = (%s), type_id = (%s), etat_id = (%s), charge = (%s), tempsPasse = (%s), descriptif = (%s), remarque = (%s)
                WHERE id = (%s) """
            data = (arProjet.nom, arProjet.type_id, arProjet.etat_id, arProjet.charge, arProjet.tempsPasse, arProjet.descriptif, arProjet.remarque, arProjet.id)
            cursor.execute(requete, data)
            self.conn.commit()

            print(f"Projet maj : {data}")

        except Exception as err:
            raise Exception("BDD - Projet - maj : " + err.args[0])


    def deleteProjet(self, arProjet):
        try:
            cursor = self.conn.cursor()
            
            requete = """DELETE FROM tProjets WHERE id = (%s)"""
            cursor.execute(requete, (arProjet.id,))
            self.conn.commit()

            print(f"projet delete -> {arProjet.id}")

        except Exception as err:
            raise Exception("BDD - Projet - delete : " + err.args[0])
        

    def lireProjets(self):
        try:
            data = []

            cursor = self.conn.cursor()

            cursor.execute("""SELECT id, nom, type_id, etat_id, charge, tempsPasse, descriptif, remarque FROM tProjets""")
            rows = cursor.fetchall()
            for row in rows:
                data.append((row))

            return data
        
        except Exception as err:
            raise Exception("BDD - Projet - lireProjets : " + err.args[0])
        

    def lireProjet(self, arProjet):
        try:
            unProjet = arProjet

            cursor = self.conn.cursor()
            requete = """SELECT nom, type_id, etat_id, charge, tempsPasse, descriptif, remarque FROM tProjets WHERE id = (%s)"""
            cursor.execute(requete, (arProjet.id,))
            row = cursor.fetchone()

            unProjet.nom = row[0]
            unProjet.type_id = int(row[1])
            unProjet.etat_id = int(row[2])
            unProjet.charge = int(row[3])
            unProjet.tempsPasse = int(row[4])
            unProjet.descriptif = row[5]
            unProjet.remarque = row[6]
            print(unProjet)

            return unProjet
        
        except Exception as err:
            raise Exception("BDD - Projet - lireProjet : " + err.args[0])
        
