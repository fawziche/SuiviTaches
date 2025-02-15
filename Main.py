import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,  QTabWidget, QWidget
from Vues import *



class SuiviTacheFenetre(QMainWindow):
    def __init__(self):
        #Initialisation de la fenetre
        QWidget.__init__(self)
        self.setWindowTitle("Suivi des taches")
        self.resize(2000,1000)
        self.move(50,50)
    
        #Initialisation des onglets
        self.tab_widget = QTabWidget()        
        
        uneVue_GestionTache = vue_GestionTache()
        self.tab_widget.addTab(uneVue_GestionTache, "Gestion des taches")

        uneVue_GestionProjet = vue_GestionProjet()
        self.tab_widget.addTab(uneVue_GestionProjet, "Gestion des projets")

        uneVue_GestionEtat = vue_GestionEtat()
        self.tab_widget.addTab(uneVue_GestionEtat, "Gestion des états")

        uneVue_GestionType = vue_GestionType()
        self.tab_widget.addTab(uneVue_GestionType, "Gestion des types")

        #On choisit l'onglet selectionné par défaut
        self.tab_widget.setCurrentIndex(0)

        #On ajoute la possibilité de fermer (ou non) les onglets
        self.tab_widget.setTabsClosable(False)   #mettre à True pour pouvoir les fermer
        self.tab_widget.tabCloseRequested.connect(self.close_current_tab)

        self.setCentralWidget(self.tab_widget)
        

    
    def close_current_tab(self, i):
 
        # if there is only one tab
        if self.tab_widget.count() < 2:
            # do nothing
            return
 
        # else remove the tab
        self.tab_widget.removeTab(i)
    


try:
    if  __name__ == '__main__':
        app = QApplication(sys.argv)
        window = SuiviTacheFenetre()
        window.show()
        sys.exit(app.exec_())       

except Exception as err:
    print(f"Erreur : {err.args[0]}")



