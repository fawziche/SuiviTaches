from PyQt5.QtWidgets import QWidget, QFormLayout, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QCheckBox, QComboBox
from Controle import *


# #########################       ETAT       ####################################################
class vue_GestionEtat(QWidget):
    def __init__(self):
        #Initialisation du Widget
        QWidget.__init__(self)

        #Initialisation du Layout
        layout = QFormLayout()   
        
        #Ajout d'un champs pour les erreur
        self.chpsErreur = QLabel ("")
        layout.addRow(self.chpsErreur)

        #Ajout d'un champs d'info
        self.chpsInfo = QLabel ("Veuillez apporter vos mises à jour :")
        layout.addRow(self.chpsInfo)

        #Tableau
        self.table = QTableWidget()
        self.remplirTableau()
        layout.addRow(self.table)

        #Ajout du bouton "Maj"
        btn = QPushButton("Mise à jour")
        btn.clicked.connect(self.maj)
        layout.addWidget(btn)

        #Ajout du layout au widget
        self.setLayout(layout)


    def maj(self):
        ctrl_EtatProjet = Ctrl_EtatProjet()
        unEtatProjet = EtatProjet()
        msgInfo = ""
        self.chpsErreur.setText("")
        self.table.selectColumn(0)   # pour prendre en compte une maj meme si on a oublié d'enlever le mode édit sur une cellule
        cbxMaj = QCheckBox()
        cbxDel = QCheckBox()

        try:
            # Update ou delete
            for row in range(self.table.rowCount()-1):
                cbxMaj = self.table.cellWidget(row, 0)
                cbxDel = self.table.cellWidget(row, 1)
                unEtatProjet.id = self.table.item(row, 2).text()
                unEtatProjet.etat = self.table.item(row, 3).text().strip()
                
                if cbxMaj.isChecked or cbxDel.isChecked: 
                    if cbxDel.isChecked():
                        ctrl_EtatProjet.deleteEtat(unEtatProjet)
                    elif cbxMaj.isChecked():
                        ctrl_EtatProjet.majEtat(unEtatProjet)


            # Insert
            tmp = self.table.item(len(self.data),3)
            if tmp == None:
                print("rien à ajouter")
            else:
                unEtatProjet.etat = tmp.text().strip()
                if (unEtatProjet.etat != ""):
                    ctrl_EtatProjet.ajouterEtat(unEtatProjet)
            
            # Cloture de la BDD
            ctrl_EtatProjet.cloreBDD()
            
            if msgInfo != "":
                self.chpsInfo.setText(f"Maj de la BDD faite : {msgInfo}")

            # Actualisation du tableau
            self.remplirTableau()

        
        except Exception as err:
            self.chpsErreur.setText(f"Erreur : {err.args[0]}")


    def remplirTableau(self):
        try:
            ctrl_EtatProjet = Ctrl_EtatProjet()
            self.data = ctrl_EtatProjet.lireEtats()    # on recherche les données à rentrer dans le tableau

            self.table.clear()  # on efface tout
            self.table.setColumnCount(4)
            self.table.setHorizontalHeaderLabels(["Maj", "Del", "ID", "Etat"])
            self.table.setColumnWidth(0, 40)
            self.table.setColumnWidth(1, 40)
            self.table.setColumnWidth(2, 100)
            self.table.setColumnWidth(3, 400)
            self.table.setRowCount(len(self.data)+1)   # fixe le nombre de ligne du tableau

            i = 0
            for elt in self.data:
                cbxMaj = QCheckBox()
                #cbxMaj.setChecked(True)
                self.table.setCellWidget(i, 0, cbxMaj)
                cbxDel = QCheckBox()
                self.table.setCellWidget(i, 1, cbxDel)

                self.table.setItem(i, 2, QTableWidgetItem(str(elt[0])))
                self.table.setItem(i, 3, QTableWidgetItem(elt[1]))
                i += 1
            self.table.setItem(i, 2, QTableWidgetItem(">>Ajouter>>"))
            
            ctrl_EtatProjet.cloreBDD()
        
        except Exception as err:
            self.chpsErreur.setText(f"Erreur : {err.args[0]}")


# #########################       TYPE       ####################################################
class vue_GestionType(QWidget):
    def __init__(self):
        #Initialisation de la fenetre
        QWidget.__init__(self)

        #Initialisation du Layout
        layout = QFormLayout()   
        
        #Ajout d'un champs pour les erreur
        self.chpsErreur = QLabel ("")
        layout.addRow(self.chpsErreur)

        #Ajout d'un champs d'info
        self.chpsInfo = QLabel ("Veuillez apporter vos mises à jour :")
        layout.addRow(self.chpsInfo)

        #Tableau
        self.table = QTableWidget()
        self.remplirTableau()
        layout.addRow(self.table)

        #Ajout du bouton "Maj"
        btn = QPushButton("Mise à jour")
        btn.clicked.connect(self.maj)
        layout.addWidget(btn)

        #Ajout du layout à la fenetre
        self.setLayout(layout)


    def maj(self):
        ctrl_TypeProjet = Ctrl_TypeProjet()
        unTypeProjet = TypeProjet()
        msgInfo = ""
        self.chpsErreur.setText("")
        self.table.selectColumn(0)   # pour prendre en compte une maj meme si on a oublié d'enlever le mode édit sur une cellule
        cbxMaj = QCheckBox()
        cbxDel = QCheckBox()

        try:
            # Update ou delete
            for row in range(self.table.rowCount()-1):
                cbxMaj = self.table.cellWidget(row, 0)
                cbxDel = self.table.cellWidget(row, 1)
                unTypeProjet.id = self.table.item(row, 2).text()
                unTypeProjet.type = self.table.item(row, 3).text().strip()
                
                if cbxMaj.isChecked or cbxDel.isChecked: 
                    if cbxDel.isChecked():
                        ctrl_TypeProjet.deleteType(unTypeProjet)
                    elif cbxMaj.isChecked():
                        ctrl_TypeProjet.majType(unTypeProjet)


            # Insert
            tmp = self.table.item(len(self.data),3)
            if tmp == None:
                print("rien à ajouter")
            else:
                unTypeProjet.type = tmp.text().strip()
                if (unTypeProjet.type != ""):
                    ctrl_TypeProjet.ajouterType(unTypeProjet)
            
            # Cloture de la BDD
            ctrl_TypeProjet.cloreBDD()
            
            if msgInfo != "":
                self.chpsInfo.setText(f"Maj de la BDD faite : {msgInfo}")

            # Actualisation du tableau
            self.remplirTableau()
        
        except Exception as err:
            self.chpsErreur.setText(f"Erreur : {err.args[0]}")


    def remplirTableau(self):
        try:
            ctrl_TypeProjet = Ctrl_TypeProjet()
            self.data = ctrl_TypeProjet.lireTypes() 

            self.table.clear()  # on efface tout
            self.table.setColumnCount(4)
            self.table.setHorizontalHeaderLabels(["Maj", "Del", "ID", "Etat"])
            self.table.setColumnWidth(0, 40)
            self.table.setColumnWidth(1, 40)
            self.table.setColumnWidth(2, 100)
            self.table.setColumnWidth(3, 400)
            self.table.setRowCount(len(self.data)+1)   # fixe le nombre de ligne du tableau

            i = 0
            for elt in self.data:
                cbxMaj = QCheckBox()
                #cbxMaj.setChecked(True)
                self.table.setCellWidget(i, 0, cbxMaj)
                cbxDel = QCheckBox()
                self.table.setCellWidget(i, 1, cbxDel)

                self.table.setItem(i, 2, QTableWidgetItem(str(elt[0])))
                self.table.setItem(i, 3, QTableWidgetItem(elt[1]))
                i += 1
            self.table.setItem(i, 2, QTableWidgetItem(">>Ajouter>>"))

            ctrl_TypeProjet.cloreBDD()

        except Exception as err:
            self.chpsErreur.setText(f"Erreur : {err.args[0]}")


# #########################       PROJET       ####################################################
class vue_GestionProjet(QWidget):
    def __init__(self):
        #Initialisation de la fenetre
        QWidget.__init__(self)

        #Initialisation du Layout
        layout = QFormLayout()   
        
        #Ajout d'un champs pour les erreur
        self.chpsErreur = QLabel ("")
        layout.addRow(self.chpsErreur)

        #Ajout d'un champs d'info
        self.chpsInfo = QLabel ("Veuillez apporter vos mises à jour :")
        layout.addRow(self.chpsInfo)

        #Tableau
        self.table = QTableWidget()
        self.remplirTableau()
        layout.addRow(self.table)

        #Ajout du bouton "Maj"
        btn = QPushButton("Mise à jour")
        btn.clicked.connect(self.maj)
        layout.addWidget(btn)

        #Ajout du layout à la fenetre
        self.setLayout(layout)


    def maj(self):
        ctrl_Projet = Ctrl_Projet()
        unProjet = Projet()
        msgInfo = ""
        self.chpsErreur.setText("")
        self.table.selectColumn(0)   # pour prendre en compte une maj meme si on a oublié d'enlever le mode édit sur une cellule
        cbxMaj = QCheckBox()
        cbxDel = QCheckBox()
        cmbType = QComboBox()
        cmbEtat = QComboBox()

        try:
            # Update ou delete
            for row in range(self.table.rowCount()-1):
                cbxMaj = self.table.cellWidget(row, 0)
                cbxDel = self.table.cellWidget(row, 1)
                
                if cbxMaj.isChecked or cbxDel.isChecked: 
                    # ID
                    unProjet.id = self.table.item(row, 2).text()
                    # Nom
                    unProjet.nom = self.table.item(row, 3).text().strip()
                    # Type
                    cmbType = self.table.cellWidget(row, 4)
                    unProjet.type_id = cmbType.itemData(cmbType.currentIndex())
                    # Etat
                    cmbEtat = self.table.cellWidget(row, 5)
                    unProjet.etat_id = cmbEtat.itemData(cmbEtat.currentIndex())
                    # Charge
                    unProjet.charge = self.table.item(row, 6).text().strip()
                    # Temps passe
                    unProjet.tempsPasse = self.table.item(row, 7).text().strip()
                    # Descriptif
                    unProjet.descriptif = self.table.item(row, 8).text().strip()
                    # Remarque
                    unProjet.remarque = self.table.item(row, 9).text().strip()

                    if cbxDel.isChecked():
                        ctrl_Projet.deleteProjet(unProjet)
                    elif cbxMaj.isChecked():
                        ctrl_Projet.majProjet(unProjet)

            # Insert
            row = len(self.data)
            if self.table.item(row, 3) == None:
                print("rien à ajouter")
            else:
                # Nom
                unProjet.nom = self.table.item(row, 3).text().strip()
                # Type
                cmbType = self.table.cellWidget(row, 4)
                unProjet.type_id = cmbType.itemData(cmbType.currentIndex())
                # Etat
                cmbEtat = self.table.cellWidget(row, 5)
                unProjet.etat_id = cmbEtat.itemData(cmbEtat.currentIndex())
                # Charge
                unProjet.charge = self.table.item(row, 6).text().strip()
                # Temps passe
                unProjet.tempsPasse = self.table.item(row, 7).text().strip()
                # Descriptif
                unProjet.descriptif = self.table.item(row, 8).text().strip()
                # Remarque
                unProjet.remarque = self.table.item(row, 9).text().strip()
              
                if (unProjet.nom != ""):
                    ctrl_Projet.ajouterProjet(unProjet)
            

            # Cloture de la BDD
            ctrl_Projet.cloreBDD()
            
            if msgInfo != "":
                self.chpsInfo.setText(f"Maj de la BDD faite : {msgInfo}")

            # Actualisation du tableau
            self.remplirTableau()
        
        except Exception as err:
            self.chpsErreur.setText(f"Erreur : {err.args[0]}")


    def remplirTableau(self):
        try:
            ctrl_Projet = Ctrl_Projet()
            self.data = ctrl_Projet.lireProjets()
            self.data_types = (Ctrl_TypeProjet()).lireTypes()
            self.data_etats = (Ctrl_EtatProjet()).lireEtats()
            
            # Initialisation de la structure de la table
            self.table.clear()  # on efface tout
            self.table.setColumnCount(10)
            self.table.setHorizontalHeaderLabels(["Maj", "Del", "ID", "Nom", "Type", "Etat", "Charge (j)", "Temps passé (j)", "Descriptif", "Remarque"])
            self.table.setColumnWidth(0, 40)
            self.table.setColumnWidth(1, 40)
            self.table.setColumnWidth(2, 100)    # ID
            self.table.setColumnWidth(3, 350)    # Nom
            self.table.setColumnWidth(4, 150)    # Type
            self.table.setColumnWidth(5, 100)    # Etat
            self.table.setColumnWidth(6, 75)     # Charge
            self.table.setColumnWidth(7, 75)     # Temps passé
            self.table.setColumnWidth(8, 500)    # Descriptif
            self.table.setColumnWidth(9, 500)    # Remarque
            self.table.setRowCount(len(self.data)+1)   # fixe le nombre de ligne du tableau

            # Alimentation du tableau
            i = 0
            for elt in self.data:
                # check box de maj
                cbxMaj = QCheckBox()
                self.table.setCellWidget(i, 0, cbxMaj)

                # check box de suppression
                cbxDel = QCheckBox()
                self.table.setCellWidget(i, 1, cbxDel)

                # ID
                self.table.setItem(i, 2, QTableWidgetItem(str(elt[0])))
                
                # Nom
                self.table.setItem(i, 3, QTableWidgetItem(elt[1]))

                # Type
                cmbType = QComboBox()
                for eltType in self.data_types:
                    cmbType.addItem(eltType[1], eltType[0])
                cmbType.setCurrentIndex(cmbType.findData(elt[2]))
                self.table.setCellWidget(i, 4, cmbType)

                # Etat
                cmbEtat = QComboBox()
                for eltEtat in self.data_etats:
                    cmbEtat.addItem(eltEtat[1], eltEtat[0])
                cmbEtat.setCurrentIndex(cmbEtat.findData(elt[3]))
                self.table.setCellWidget(i, 5, cmbEtat)

                # Charge                
                self.table.setItem(i, 6, QTableWidgetItem(str(elt[4])))

                # Temps passé
                self.table.setItem(i, 7, QTableWidgetItem(str(elt[5])))

                # Descriptif
                self.table.setItem(i, 8, QTableWidgetItem(elt[6]))
                
                # Remarque
                self.table.setItem(i, 9, QTableWidgetItem(elt[7]))

                i += 1

            # On prépare la ligne pour "ajout"
            self.table.setItem(i, 2, QTableWidgetItem(">>Ajouter>>"))
            cmbType = QComboBox()
            for eltType in self.data_types:
                cmbType.addItem(eltType[1], eltType[0])
            self.table.setCellWidget(i, 4, cmbType)
            cmbEtat = QComboBox()
            for eltEtat in self.data_etats:
                cmbEtat.addItem(eltEtat[1], eltEtat[0])
            self.table.setCellWidget(i, 5, cmbEtat)

            # On redimensionne automatiquement les cellules en fonction de leur contenu            
            self.table.resizeRowsToContents()
            self.table.resizeColumnsToContents()

            # On clot l'accès à la BDD
            ctrl_Projet.cloreBDD()

        except Exception as err:
            self.chpsErreur.setText(f"Erreur : {err.args[0]}")
