# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 15:32:41 2023

@author: naouf
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class Fenetre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mon interface")
        self.setGeometry(100, 100, 600, 600)

        # Labels pour les variables
        VM_in_label = QLabel("VM_in :", self)
        VM_in_label.move(50, 50)
        t_label = QLabel("t :", self)
        t_label.move(50, 100)
        H2O2_in_label = QLabel("H2O2_in :", self)
        H2O2_in_label.move(50, 150)
        Ic_label = QLabel("Ic :", self)
        Ic_label.move(50, 200)
        V_label = QLabel("V :", self)
        V_label.move(50, 250)
        S_label = QLabel("S :", self)
        S_label.move(50, 300)
        pH_label = QLabel("pH :", self)
        pH_label.move(50, 350)
        HSO4_in_label = QLabel("HSO4_in", self)
        HSO4_in_label.move(50, 400)
        O2_in_label = QLabel("O2_in", self)
        O2_in_label.move(50, 450)

        # Champs de saisie pour les variables
        self.VM_in_entry = QLineEdit(self)
        self.VM_in_entry.move(150, 50)
        self.t_entry = QLineEdit(self)
        self.t_entry.move(150, 100)
        self.H2O2_in_entry = QLineEdit(self)
        self.H2O2_in_entry.move(150, 150)
        self.Ic_entry = QLineEdit(self)
        self.Ic_entry.move(150, 200)
        self.V_entry = QLineEdit(self)
        self.V_entry.move(150, 250)
        self.S_entry = QLineEdit(self)
        self.S_entry.move(150, 300)
        self.pH_entry = QLineEdit(self)
        self.pH_entry.move(150, 350)
        self.HSO4_in_entry = QLineEdit(self)
        self.HSO4_in_entry.move(150, 400)
        self.O2_in_entry = QLineEdit(self)
        self.O2_in_entry.move(150, 450)

        # Bouton pour déclencher le calcul
        self.calculer_button = QPushButton("Calculer", self)
        self.calculer_button.move(50, 400)
        self.calculer_button.clicked.connect(self.calculer)

        # Champ pour afficher le résultat
        self.resultat_label = QLabel(self)
        self.resultat_label.move(50, 450)

        # Initialisation des variables globales
        self.VM_in = None
        self.t = None
        self.H2O2_in = None
        self.Ic = None
        self.V = None
        self.S = None
        self.pH = None
        self.HSO4_in = None
        self.O2_in = None
        
    def calculer(self):
        self.VM_in = float(self.VM_in_entry.text())
        self.t = float(self.t_entry.text())
        self.H2O2_in = float(self.H2O2_in_entry.text())
        self.Ic = float(self.Ic_entry.text())
        self.V = float(self.V_entry.text())
        self.S = float(self.S_entry.text())
        self.pH = float(self.pH_entry.text())
        self.HSO4_in = float(self.HSO4_in_entry.text())
        self.O2_in = float(self.O2_in_entry.text())
        
        D = self.VM_in + self.t + self.H2O2_in + self.Ic + self.V + self.S + self.pH + self.HSO4_in + self.O2_in

        self.resultat_label.setText("Résultat : {}".format(D))
        self.resultat_label.move(50, 500) # déplace le label pour qu'il ne chevauche pas les autres champs

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = Fenetre()
    
    layout = QVBoxLayout()
    layout.addWidget(fenetre.calculer_button)
    layout.addWidget(fenetre.resultat_label)
    
    widget = QWidget()
    widget.setLayout(layout)
    
    fenetre.setCentralWidget(widget)
    fenetre.show()
    
    sys.exit(app.exec_())
