from PyQt5.QtWidgets import QWidget, QFormLayout, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QCheckBox, QComboBox, QHBoxLayout, QLineEdit
from Controle import *
import datetime


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

        #Filtre
        self.layout_filter = QHBoxLayout()
        self.zoneFiltre()
        layout.addRow(self.layout_filter)

        #Ajout du bouton "Maj"
        btn = QPushButton("Mise à jour")
        btn.setStyleSheet("background-color: green")
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
                    if self.table.item(row, 8) == None:
                        unProjet.descriptif = ""
                    else:
                        unProjet.descriptif = self.table.item(row, 8).text().strip()
                    # Remarque
                    if self.table.item(row, 9) == None:
                        unProjet.remarque = ""
                    else:
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
                if self.table.item(row, 6) == None:
                    unProjet.charge = 0
                else:
                    unProjet.charge = self.table.item(row, 6).text().strip()
                # Temps passe
                if self.table.item(row, 7) == None:
                    unProjet.tempsPasse = 0
                else:
                    unProjet.tempsPasse = self.table.item(row, 7).text().strip()
                # Descriptif
                if self.table.item(row, 8) == None:
                    unProjet.descriptif = ""
                else:
                    unProjet.descriptif = self.table.item(row, 8).text().strip()
                # Remarque
                if self.table.item(row, 9) == None:
                    unProjet.remarque = ""
                else:
                    unProjet.remarque = self.table.item(row, 9).text().strip()
              
                if (unProjet.nom != ""):
                    ctrl_Projet.ajouterProjet(unProjet)
            

            # Cloture de la BDD
            ctrl_Projet.cloreBDD()
            
            if msgInfo != "":
                self.chpsInfo.setText(f"Maj de la BDD faite : {msgInfo}")

            # Actualisation du tableau
            self.remplirTableau()
            self.zoneFiltre()
        
        except Exception as err:
            self.chpsErreur.setText(f"Erreur : {err.args[0]}")


    def trierEtDoublon(self, column):        
        
        uneListe = []   # on récupère les valeurs de la colonne
        for j in range(self.table.rowCount() - 1):
            uneListe.append(self.table.item(j, column).text())

        items = set(uneListe)   # un set permet d'avoir des valeurs uniques

        uniqueItems = list(items)     # on le convertit en liste pour pouvoir le trier
        numeric_sort = lambda x: float(x)    # on fait un tri personnalisé (en gros, chaque elt est converti en float, puis on trie comme des float)
        uniqueItems.sort(key=numeric_sort)

        ComboBox_sortie = QComboBox()
        ComboBox_sortie.addItem("Tous")
        for j in range(len(uniqueItems)):
            ComboBox_sortie.addItem(uniqueItems[j])

        return ComboBox_sortie


    def zoneFiltre(self):
        try:
            # Initialisation du layout horizontal pour le filtre
            for i in reversed(range(self.layout_filter.count())):
                #widget = self.layout_filter.itemAt(i).widget()
                self.layout_filter.itemAt(i).widget().deleteLater()

            # Bouton
            btnFiltre = QPushButton("Filtrer")
            btnFiltre.clicked.connect(self.filtrer)
            btnFiltre.setStyleSheet("background-color: cyan")
            self.layout_filter.addWidget(btnFiltre)

            # ID
            self.layout_filter.addWidget(QLabel("ID :"))
            self.cmbID = self.trierEtDoublon(2)
            self.layout_filter.addWidget(self.cmbID)

            # Nom
            self.layout_filter.addWidget(QLabel("Nom :"))
            self.cmbNom = QComboBox()
            self.cmbNom.addItem("Tous")
            for j in range(self.table.rowCount() - 1):
                self.cmbNom.addItem(self.table.item(j, 3).text())
            self.layout_filter.addWidget(self.cmbNom)

            #Type
            self.layout_filter.addWidget(QLabel("Type :"))
            self.cmbType = QComboBox()
            self.cmbType.addItem("Tous")
            self.data_types = (Ctrl_TypeProjet()).lireTypes()
            for eltType in self.data_types:
                self.cmbType.addItem(eltType[1], eltType[0])
            self.layout_filter.addWidget(self.cmbType)

            #Etat
            self.layout_filter.addWidget(QLabel("Etat :"))
            self.cmbEtat = QComboBox()
            self.cmbEtat.addItem("Tous")
            self.data_etats = (Ctrl_EtatProjet()).lireEtats()
            for eltEtat in self.data_etats:
                self.cmbEtat.addItem(eltEtat[1], eltEtat[0])
            self.layout_filter.addWidget(self.cmbEtat)
            
            # Charge
            self.layout_filter.addWidget(QLabel("Charge :"))            
            self.cmbCharge = self.trierEtDoublon(6)
            self.layout_filter.addWidget(self.cmbCharge)

           # Temps passé
            self.layout_filter.addWidget(QLabel("Temps passé :"))
            self.cmbTempsPasse = self.trierEtDoublon(7)
            self.layout_filter.addWidget(self.cmbTempsPasse)

            # Descriptif
            self.layout_filter.addWidget(QLabel("Descriptif :"))
            self.txtDescriptif = QLineEdit()
            self.layout_filter.addWidget(self.txtDescriptif)

            # Remarque
            self.layout_filter.addWidget(QLabel("Remarque :"))
            self.txtRemarque = QLineEdit()
            self.layout_filter.addWidget(self.txtRemarque)


        except Exception as err:
            self.chpsErreur.setText(f"Erreur : {err.args[0]}")


    def filtrer(self):
        try:
            filtre_id = self.cmbID.currentText()
            filtre_nom = self.cmbNom.currentText()
            filtre_type = self.cmbType.currentText()
            filtre_etat = self.cmbEtat.currentText()
            filtre_charge = self.cmbCharge.currentText()
            filtre_tempsPasse = self.cmbTempsPasse.currentText()
            filtre_descriptif = self.txtDescriptif.text()
            filtre_remarque = self.txtRemarque.text()

            cmbFiltre_Type = QComboBox()
            cmbFiltre_Etat = QComboBox()
            for row in range(self.table.rowCount() - 1):
                bAfficheLigne = True

                if filtre_id != "Tous" and filtre_id != self.table.item(row, 2).text():
                    bAfficheLigne = False

                if filtre_nom != "Tous" and filtre_nom != self.table.item(row, 3).text():
                    bAfficheLigne = False

                cmbFiltre_Type = self.table.cellWidget(row, 4)
                if filtre_type != "Tous" and filtre_type != cmbFiltre_Type.currentText():
                    bAfficheLigne = False

                cmbFiltre_Etat = self.table.cellWidget(row, 5)
                if filtre_etat != "Tous" and filtre_etat != cmbFiltre_Etat.currentText():
                    bAfficheLigne = False

                if bAfficheLigne :
                    self.table.setRowHidden(row, False)
                else:
                    self.table.setRowHidden(row, True)


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




# #########################       TACHE       ####################################################
class vue_GestionTache(QWidget):
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

        #Filtre
        self.layout_filter = QHBoxLayout()
        self.zoneFiltre()
        layout.addRow(self.layout_filter)

        #Ajout du bouton "Maj"
        btn = QPushButton("Mise à jour")
        btn.setStyleSheet("background-color: green")
        btn.clicked.connect(self.maj)
        layout.addWidget(btn)

        #Ajout du layout à la fenetre
        self.setLayout(layout)


    def remplirTableau(self):
        try:
            ctrl_Tache = Ctrl_Tache()
            self.data = ctrl_Tache.lireTaches()
            self.data_projets = (Ctrl_Projet()).lireProjets()
            
            # Initialisation de la structure de la table
            self.table.clear()  # on efface tout
            self.table.setColumnCount(8)
            self.table.setHorizontalHeaderLabels(["Maj", "Del", "ID", "date", "projet", "Temps passé (j)", "Temps prévu (j)", "Description"])
            self.table.setColumnWidth(0, 40)
            self.table.setColumnWidth(1, 40)
            self.table.setColumnWidth(2, 100)    # ID
            self.table.setColumnWidth(3, 100)    # Date
            self.table.setColumnWidth(4, 200)    # Projet
            self.table.setColumnWidth(5, 75)     # Temps passé
            self.table.setColumnWidth(6, 75)     # Temps prévu
            self.table.setColumnWidth(7, 500)    # Description
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
                
                # Date
                self.table.setItem(i, 3, QTableWidgetItem(datetime.date.strftime (elt[1], '%Y-%m-%d')))

                # Projet
                cmbProjet = QComboBox()
                for eltProjet in self.data_projets:
                    cmbProjet.addItem(eltProjet[1], eltProjet[0])
                cmbProjet.setCurrentIndex(cmbProjet.findData(elt[2]))
                self.table.setCellWidget(i, 4, cmbProjet)

                # Temps passé
                self.table.setItem(i, 5, QTableWidgetItem(str(elt[3])))

                # Temps prévu
                self.table.setItem(i, 6, QTableWidgetItem(str(elt[4])))

                # Description
                self.table.setItem(i, 7, QTableWidgetItem(elt[5]))

                i += 1

            # On prépare la ligne pour "ajout"
            self.table.setItem(i, 2, QTableWidgetItem(">>Ajouter>>"))
            self.table.setItem(i, 3, QTableWidgetItem(datetime.date.strftime (datetime.date.today(), '%Y-%m-%d')))
            cmbProjet = QComboBox()
            for eltProjet in self.data_projets:
                cmbProjet.addItem(eltProjet[1], eltProjet[0])
            self.table.setCellWidget(i, 4, cmbProjet)

            # On redimensionne automatiquement les cellules en fonction de leur contenu            
            self.table.resizeRowsToContents()
            self.table.resizeColumnsToContents()

            # On clot l'accès à la BDD
            ctrl_Tache.cloreBDD()

        except Exception as err:
            self.chpsErreur.setText(f"Erreur : {err.args[0]}")


    def trierEtDoublon(self, column, typeTri):        
        
        uneListe = []   # on récupère les valeurs de la colonne
        for j in range(self.table.rowCount() - 1):
            uneListe.append(self.table.item(j, column).text())

        items = set(uneListe)   # un set permet d'avoir des valeurs uniques

        uniqueItems = list(items)     # on le convertit en liste pour pouvoir le trier
        if typeTri == "int":
            numeric_sort = lambda x: int(x)  
        elif typeTri == "date":
            numeric_sort = lambda x: str(x)
        else:
            numeric_sort = lambda x: float(x)    # on fait un tri personnalisé (en gros, chaque elt est converti en float, puis on trie comme des float)
        uniqueItems.sort(key=numeric_sort)

        ComboBox_sortie = QComboBox()
        ComboBox_sortie.addItem("Tous")
        for j in range(len(uniqueItems)):
            ComboBox_sortie.addItem(uniqueItems[j])

        return ComboBox_sortie
    

    def zoneFiltre(self):
        try:
            # Initialisation du layout horizontal pour le filtre
            for i in reversed(range(self.layout_filter.count())):
                self.layout_filter.itemAt(i).widget().deleteLater()

            # Bouton
            btnFiltre = QPushButton("Filtrer")
            btnFiltre.clicked.connect(self.filtrer)
            btnFiltre.setStyleSheet("background-color: cyan")
            self.layout_filter.addWidget(btnFiltre)

            # ID
            self.layout_filter.addWidget(QLabel("ID :"))
            self.cmbID = self.trierEtDoublon(2, "int")
            self.layout_filter.addWidget(self.cmbID)

            # Date
            self.layout_filter.addWidget(QLabel("Date :"))
            self.cmbDate = self.trierEtDoublon(3, "date")
            self.layout_filter.addWidget(self.cmbDate)

            #Projet
            self.layout_filter.addWidget(QLabel("Projet :"))
            self.cmbProjet = QComboBox()
            self.cmbProjet.addItem("Tous")
            self.data_projets = (Ctrl_Projet()).lireProjets()
            for eltProjet in self.data_projets:
                self.cmbProjet.addItem(eltProjet[1], eltProjet[0])
            self.layout_filter.addWidget(self.cmbProjet)

        except Exception as err:
            self.chpsErreur.setText(f"Erreur : {err.args[0]}")


    def filtrer(self):
        try:
            filtre_id = self.cmbID.currentText()
            filtre_date = self.cmbDate.currentText()
            filtre_projet = self.cmbProjet.currentText()


            cmbFiltre_Projet = QComboBox()
            for row in range(self.table.rowCount() - 1):
                bAfficheLigne = True

                if filtre_id != "Tous" and filtre_id != self.table.item(row, 2).text():
                    bAfficheLigne = False

                if filtre_date != "Tous" and filtre_date != self.table.item(row, 3).text():
                    bAfficheLigne = False

                cmbFiltre_Projet = self.table.cellWidget(row, 4)
                if filtre_projet != "Tous" and filtre_projet != cmbFiltre_Projet.currentText():
                    bAfficheLigne = False

                if bAfficheLigne :
                    self.table.setRowHidden(row, False)
                else:
                    self.table.setRowHidden(row, True)


        except Exception as err:
            self.chpsErreur.setText(f"Erreur : {err.args[0]}")


    def maj(self):
        ctrl_Tache = Ctrl_Tache()
        uneTache = Tache()
        msgInfo = ""
        self.chpsErreur.setText("")
        self.table.selectColumn(0)   # pour prendre en compte une maj meme si on a oublié d'enlever le mode édit sur une cellule
        cbxMaj = QCheckBox()
        cbxDel = QCheckBox()
        cmbProjet = QComboBox()

        try:
            # Update ou delete
            for row in range(self.table.rowCount()-1):
                cbxMaj = self.table.cellWidget(row, 0)
                cbxDel = self.table.cellWidget(row, 1)
                
                if cbxMaj.isChecked or cbxDel.isChecked: 
                    # ID
                    uneTache.id = self.table.item(row, 2).text()
                    # Date
                    uneTache.date = self.table.item(row, 3).text().strip()
                    # Projet
                    cmbProjet = self.table.cellWidget(row, 4)
                    uneTache.projet_id = cmbProjet.itemData(cmbProjet.currentIndex())
                    # Temps passe
                    uneTache.tempsPasse = self.table.item(row, 5).text().strip()
                    # Temps passe
                    uneTache.tempsPrevu = self.table.item(row, 6).text().strip()
                    # Description
                    if self.table.item(row, 7) == None:
                        uneTache.description = ""
                    else:
                        uneTache.description = self.table.item(row, 7).text().strip()

                    if cbxDel.isChecked():
                        ctrl_Tache.deleteTache(uneTache)
                    elif cbxMaj.isChecked():
                        ctrl_Tache.majTache(uneTache)

            # Insert
            row = len(self.data)
            if self.table.item(row, 3) == None:
                print("rien à ajouter")
            else:
                # Date
                uneTache.date = self.table.item(row, 3).text().strip()
                # Projet
                cmbProjet = self.table.cellWidget(row, 4)
                uneTache.projet_id = cmbProjet.itemData(cmbProjet.currentIndex())
                # Temps passe
                if self.table.item(row, 5) == None:
                    uneTache.tempsPasse = 0
                else:
                    uneTache.tempsPasse = self.table.item(row, 5).text().strip()
                # Temps prévu
                if self.table.item(row, 6) == None:
                    uneTache.tempsPrevu = 0
                else:
                    uneTache.tempsPrevu = self.table.item(row, 6).text().strip()
                # Description
                if self.table.item(row, 7) == None:
                    uneTache.description = ""
                else:
                    uneTache.description = self.table.item(row, 7).text().strip()
              
                if (uneTache.description != ""):
                    ctrl_Tache.ajouterTache(uneTache)
            

            # Cloture de la BDD
            ctrl_Tache.cloreBDD()
            
            if msgInfo != "":
                self.chpsInfo.setText(f"Maj de la BDD faite : {msgInfo}")

            # Actualisation du tableau
            self.remplirTableau()
            self.zoneFiltre()
        
        except Exception as err:
            self.chpsErreur.setText(f"Erreur : {err.args[0]}")
