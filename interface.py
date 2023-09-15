import sys, time

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import pdfToExcel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Paramètres de la fenêtre
        self.setWindowTitle("Transforme un pdf en excel - DSSR")
        self.setWindowIcon(QIcon('sncf_reseau.ico'))

        # Création des inputs qui vont jouer dans le script                
        self.input1 = QLineEdit()
        self.input1.setFixedSize(200,25)
        self.input1.setStyleSheet("background-color: white; color:black;")
        
        self.input2 = QLineEdit()
        self.input2.setFixedSize(200,25)
        self.input2.setStyleSheet("background-color: white; color:black;")
        
        self.input3 = QLineEdit()
        self.input3.setFixedSize(200,25)
        self.input3.setStyleSheet("background-color: white; color:black;")

        self.form = QFormLayout()
        self.form.addRow("Le chemin d'accès au fichier : ", self.input1)
        self.form.addRow("Le chemin de sortie : ", self.input2)
        self.form.addRow("Le nom du fichier de sortie : ", self.input3)

        # Checkbox pour le mot de passe 
        self.chBox = QCheckBox()
        self.chBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.chBox.stateChanged.connect(self.clickBox)
        self.form.addRow("Votre fichier comporte-t'il un mot de passe ?", self.chBox)

        # Création du boutton
        self.p = None    
 
        self.button = QPushButton("Donne-moi un fichier excel")
        self.button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button.pressed.connect(self.start_process)
        self.form.addRow(self.button)

        container = QWidget()
        container.setLayout(self.form)
        self.setCentralWidget(container)

    def clickBox(self):
        if self.chBox.isChecked() == True:
            self.input4 = QLineEdit()
            self.input4.setEchoMode(QLineEdit.EchoMode.Password)
            self.form.insertRow(4, "Le mot de passe : ", self.input4)
        else:
            self.form.removeRow(4)

    def start_process(self):
        input = self.input1.text()
        output = self.input2.text()
        name = self.input3.text()

        self.qp = QProcess()

        if self.chBox.isChecked():
            mdp = self.input4.text()
            pdfToExcel.transform(input, output, name, mdp)
        else:
            pdfToExcel.transform(input, output, name)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    app.setStyleSheet("""
        QWidget {
            background-color: "black";
            color: "white";
            font-size : 12px;
        }

        QCheckBox::indicator {
            margin: 8px;
            width: 5px;
            height: 5px;
        }

        QCheckBox::indicator:checked {
            image: url(check.png);
            background-color: "white";
            width:20px;
            height:20px;
            margin: 0px;
        }
        
        QPushButton {
            background-color: white;
            font-size: 12px;
            font: bold;
            color: "black";
            margin: 5 120 5 120px;
        }

    """)

    window.show()
    sys.exit(app.exec())
