from jeeva import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QDate
import main
import sys
import time


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        main.TaskExe()






startExe = MainThread()


class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        self.gui.start_btn.clicked.connect(self.startTask)
        self.gui.Exit_btn.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

    def startTask(self):
        self.gui.label1 = QtGui.QMovie("G.U.I Material//ExtraGui//Health_Template.gif")
        self.gui.gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("G.U.I Material//ExtraGui//initial.gif")
        self.gui.gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("G.U.I Material//ExtraGui//Jarvis_Gui (2).gif")
        self.gui.gif_3.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4 = QtGui.QMovie("G.U.I Material//VoiceReg//Siri_1.gif")
        self.gui.gif_4.setMovie(self.gui.label4)
        self.gui.label4.start()

        self.gui.label5 = QtGui.QMovie("G.U.I Material//B.G//Iron_Template_1.gif")
        self.gui.gif_5.setMovie(self.gui.label5)
        self.gui.label5.start()

        self.gui.label6 = QtGui.QMovie("G.U.I Material//ExtraGui//Earth.gif")
        self.gui.gif_6.setMovie(self.gui.label6)
        self.gui.label6.start()

        self.gui.label7 = QtGui.QMovie("G.U.I Material//ExtraGui//jarvis breaking.gif")
        self.gui.gif_7.setMovie(self.gui.label7)
        self.gui.label7.start()

        startExe.start()

    # def run(self):
    #   main.TaskExe()


GuiApp = QApplication(sys.argv)
jarvis_gui = Gui_Start()
jarvis_gui.show()
exit(GuiApp.exec_())
