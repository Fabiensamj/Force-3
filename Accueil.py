# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# Fichier générant une fenêtre permettant à l'utilisateur de jouer au jeu FORCE 3
#
# Cette interface permet à l'utilisateur de jouer sur plusieurs modes:
#
#       Joueur contre Joueur || Joueur contre le robot || Robot contre Robot
#



from PyQt5 import QtCore, QtGui, QtWidgets
from partie import iaVSia, jVSia, jVSj
import os

class Ui_mainWindow(object):

#=============================================================================#
#===========================Fenêtre principale du jeu=========================#
#=============================================================================#


#Fonction définissant les composants de la fenêtre

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(860, 738)
        mainWindow.setStyleSheet("*{background-color:rgb(255, 255, 255)}\n")
        mainWindow.setWindowIcon(QtGui.QIcon('imgs/force3.png'))

        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Infos = QtWidgets.QLabel(self.centralwidget)
        self.Infos.setGeometry(QtCore.QRect(20, 40, 71, 61))
        self.Infos.setText("")
        self.Infos.setPixmap(QtGui.QPixmap("imgs/but_credits.png"))
        self.Infos.setScaledContents(True)
        self.Infos.setObjectName("Infos")

        self.Titre = QtWidgets.QLabel(self.centralwidget)
        self.Titre.setGeometry(QtCore.QRect(290, 20, 261, 101))
        self.Titre.setStyleSheet("QLabel{ color: #007eff; font-family: \'Raleway\',sans-serif; font-size: 62px; font-weight: 800; line-height: 72px; margin: 0 0 24px; text-align: center; text-transform: uppercase; }")
        self.Titre.setAlignment(QtCore.Qt.AlignCenter)
        self.Titre.setObjectName("Titre")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(160, 300, 541, 311))
        self.frame.setStyleSheet("QFrame{background-color:rgb(156, 156, 156)}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.PvsP = QtWidgets.QLabel(self.frame)
        self.PvsP.setGeometry(QtCore.QRect(30, 140, 121, 91))
        self.PvsP.setText("")
        self.PvsP.setPixmap(QtGui.QPixmap("imgs/but_human.png"))
        self.PvsP.setScaledContents(True)
        self.PvsP.setObjectName("PvsP")

        self.PvsIA = QtWidgets.QLabel(self.frame)
        self.PvsIA.setGeometry(QtCore.QRect(370, 140, 121, 91))
        self.PvsIA.setText("")
        self.PvsIA.setPixmap(QtGui.QPixmap("imgs/but_cpu.png"))
        self.PvsIA.setScaledContents(True)
        self.PvsIA.setObjectName("PvsIA")

        self.IAvsIA = QtWidgets.QLabel(self.frame)
        self.IAvsIA.setGeometry(QtCore.QRect(200, 140, 121, 91))
        self.IAvsIA.setText("")
        self.IAvsIA.setPixmap(QtGui.QPixmap("imgs/but_cpvscpu.png"))
        self.IAvsIA.setScaledContents(True)
        self.IAvsIA.setObjectName("IAvsIA")

        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 40, 231, 41))
        self.layoutWidget.setObjectName("layoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.Pseudo = QtWidgets.QLabel(self.layoutWidget)
        self.Pseudo.setStyleSheet("QLabel{ color: #ffffff; font-family: \'Raleway\';  text-align: center; text-transform: uppercase;background-color:#007eff;}")
        self.Pseudo.setObjectName("Pseudo")

        self.horizontalLayout.addWidget(self.Pseudo)

        self.Pseudo_Edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.Pseudo_Edit.setStyleSheet("QLineEdit{\n"
                                        "    width: 100%;\n"
                                        "    padding: 8px 16px;\n"
                                        "    line-height: 25px;\n"
                                        "    font-size: 14px;\n"
                                        "    font-weight: 500;\n"
                                        "    font-family: inherit;\n"
                                        "border: 0px solid #000000;\n"
                                        "    color:#99A3BA;\n"
                                        "    border: 1px solid #007eff;\n"
                                        "  }\n"
                                        "")
        self.Pseudo_Edit.setObjectName("Pseudo_Edit")

        self.horizontalLayout.addWidget(self.Pseudo_Edit)

        self.IAvsIA_but = QtWidgets.QPushButton(self.frame)
        self.IAvsIA_but.setGeometry(QtCore.QRect(200, 260, 121, 31))
        self.IAvsIA_but.setStyleSheet("QPushButton{\n"
                                        "    padding: 0.5em 1em;\n"    
                                        "    background: #007eff;/*Button Color*/\n"
                                        "    color: #FFF;\n"
                                        "    border-bottom: solid 4px #627295;\n"
                                        "    border-radius: 3px;}")
        self.IAvsIA_but.setObjectName("IAvsIA_but")
        #bouton qui ouvre un terminal et permet à l'utilisateur de regarder une partie entre deux robots
        self.IAvsIA_but.clicked.connect(partieIavsIa)


        self.PvIA_but = QtWidgets.QPushButton(self.frame)
        self.PvIA_but.setGeometry(QtCore.QRect(370, 260, 121, 31))
        self.PvIA_but.setStyleSheet("QPushButton{\n"
                                        "    padding: 0.5em 1em;\n"
                                        "    background: #007eff;/*Button Color*/\n"
                                        "    color: #FFF;\n"
                                        "    border-bottom: solid 4px #627295;\n"
                                        "    border-radius: 3px;}")
        self.PvIA_but.setObjectName("PvIA_but")
        #bouton qui ouvre un terminal permettant de jouer contre un robot
        self.PvIA_but.clicked.connect(partiePvsIa)


        self.pvp_but = QtWidgets.QPushButton(self.frame)
        self.pvp_but.setGeometry(QtCore.QRect(30, 260, 121, 31))
        self.pvp_but.setStyleSheet("QPushButton{"
                                        "    padding: 0.5em 1em;\n"
                                        "    background: #007eff;/*Button Color*/\n"
                                        "    color: #FFF;\n"
                                        "    border-bottom: solid 4px #627295;\n"
                                        "    border-radius: 3px;}")
        self.pvp_but.setObjectName("pvp_but")
        #bouton qui ouvre un terminal ou le joueur peut jouer contre un autre joueur
        self.pvp_but.clicked.connect(partiePvsP)


        self.Jeu = QtWidgets.QLabel(self.centralwidget)
        self.Jeu.setGeometry(QtCore.QRect(290, 90, 271, 201))
        self.Jeu.setText("")
        self.Jeu.setPixmap(QtGui.QPixmap("imgs/Jeu.png"))
        self.Jeu.setScaledContents(True)
        self.Jeu.setObjectName("Jeu")

        self.frame.raise_()
        self.Infos.raise_()
        self.Titre.raise_()
        self.Jeu.raise_()

        mainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 25))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)


    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "FORCE 3"))
        self.Titre.setText(_translate("mainWindow", "Force 3"))
        self.Pseudo.setText(_translate("mainWindow", "Pseudo"))
        self.IAvsIA_but.setText(_translate("mainWindow", "IA vs IA"))
        self.PvIA_but.setText(_translate("mainWindow", "Player vs IA"))
        self.pvp_but.setText(_translate("mainWindow", "Player vs Player"))

#=====================================================================================#
#===========================Fonction appliquées sur l'interface=======================#
#=====================================================================================#

def partiePvsP(self):
        os.system('cls')
        mainWindow.hide()
        QtCore.pyqtRemoveInputHook()
        jVSj()
        mainWindow.show()
         
def partieIavsIa(self):
        os.system('cls')
        mainWindow.hide()
        iaVSia()
        mainWindow.show()

def partiePvsIa(self):
        os.system('cls')
        mainWindow.hide()
        QtCore.pyqtRemoveInputHook()
        jVSia()
        mainWindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
