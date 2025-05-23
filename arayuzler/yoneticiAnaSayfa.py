from PyQt5 import QtCore, QtGui, QtWidgets
import ilkSayfa_py
import bahceDurumu
import ekipmanEkle
import kullaniciSil
import kullaniciEkle
import kullanicilariGoruntule
import ekipmanlarYonetici

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon(':/gardenPic/saksı-Photoroom2.png'))
        MainWindow.setFixedSize(1920, 1080)
        MainWindow.setStyleSheet("background-color: rgb(47, 91, 76);\n"
"background-color: rgb(47, 91, 76);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(34, 136, 85);\n"
"background-color: rgb(47, 91, 76);")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(600, 400, 731, 334))
        self.widget.setObjectName("widget")
       
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(325, 125, 1300, 250))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(55)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"background-image: url(:/gardenPic/ustYazi.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(1550, -90, 487, 500))
        self.graphicsView.setStyleSheet("border-color: rgb(47, 91, 76);\n"
"border-left-color: rgb(47, 91, 76);\n"
"background: transparent;\n"
"\n"
"background-image:  url(:/gardenPic/saksı-Photoroom.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"")
        
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("\n"
"            QPushButton {\n"
"                background-color: rgb(191, 183, 165);\n"
"                border-radius: 20px;  /* Yuvarlaklık */\n"
"                padding: 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(210, 200, 180);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: rgb(170, 160, 140);\n"
"            }")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("\n"
"            QPushButton {\n"
"                background-color: rgb(191, 183, 165);\n"
"                border-radius: 20px;  /* Yuvarlaklık */\n"
"                padding: 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(210, 200, 180);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: rgb(170, 160, 140);\n"
"            }")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("\n"
"            QPushButton {\n"
"                background-color: rgb(191, 183, 165);\n"
"                border-radius: 20px;  /* Yuvarlaklık */\n"
"                padding: 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(210, 200, 180);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: rgb(170, 160, 140);\n"
"            }\n"
"        ")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("\n"
"            QPushButton {\n"
"                background-color: rgb(191, 183, 165);\n"
"                border-radius: 20px;  /* Yuvarlaklık */\n"
"                padding: 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(210, 200, 180);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: rgb(170, 160, 140);\n"
"            }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("\n"
"            QPushButton {\n"
"                background-color: rgb(191, 183, 165);\n"
"                border-radius: 20px;  /* Yuvarlaklık */\n"
"                padding: 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(210, 200, 180);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: rgb(170, 160, 140);\n"
"            }")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("\n"
"            QPushButton {\n"
"                background-color: rgb(191, 183, 165);\n"
"                border-radius: 20px;  /* Yuvarlaklık */\n"
"                padding: 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(210, 200, 180);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: rgb(170, 160, 140);\n"
"            }")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)

        self.pushButton_cikis = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cikis.setGeometry(QtCore.QRect(20, 20, 150, 51))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_cikis.setFont(font)
        self.pushButton_cikis.setStyleSheet("""
            QPushButton {
                background-color: rgb(131, 65, 0);
                border-radius: 10px;  /* Yuvarlaklık */
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgb(170, 70, 0);
            }
            QPushButton:pressed {
                background-color: rgb(145, 70, 0);
            }
        """)
        self.pushButton_cikis.setObjectName("pushButton_cikis")

        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(-70, 600, 487, 500))
        self.graphicsView_2.setStyleSheet("border-color: rgb(47, 91, 76);\n"
"border-left-color: rgb(47, 91, 76);\n"
"background: transparent;\n"
"\n"
"background-image: url(:/gardenPic/saksı-Photoroom2.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"")
        self.graphicsView_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView_2.setObjectName("graphicsView_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Garden Hub"))
        self.pushButton_5.setText(_translate("MainWindow", "\n"
"KULLANICI\n"
"SİL\n"
""))
        self.pushButton_3.setText(_translate("MainWindow", "\n"
"EKİPMAN\n"
"EKLE\n"
""))
        self.pushButton.setText(_translate("MainWindow", "\n"
"KULLANICI \n"
" GÖRÜNTÜLEME\n"
""))
        self.pushButton_2.setText(_translate("MainWindow", "\n"
"KULLANICI\n"
"EKLE\n"
""))
        self.pushButton_6.setText(_translate("MainWindow", "\n"
"EKİPMANLARIN\n"
"DURUMUNU GÖR\n"
""))
        self.pushButton_4.setText(_translate("MainWindow", "\n"
"BAHÇELERİN\n"
"DURUMUNU GÖR\n"
""))
        self.pushButton_cikis.setText(_translate("MainWindow", "ÇIKIŞ YAP"))
        self.label.setText(_translate("MainWindow", "GARDEN HUB"))
import resimler_rc


class YoneticiAnaSayfa(QtWidgets.QMainWindow):
        def __init__(self) -> None:
                super().__init__()
                self.ui = Ui_MainWindow()  # Burada doğru bir şekilde ui nesnesi başlatılıyor.
                self.ui.setupUi(self)
                self.ui.pushButton_6.clicked.connect(self.ekipmanlarYoneticiGit)
                self.ui.pushButton.clicked.connect(self.kullanicilariGoruntule)
                self.ui.pushButton_2.clicked.connect(self.kullaniciEkleyeGit)
                self.ui.pushButton_5.clicked.connect(self.kullaniciSileGit)
                self.ui.pushButton_3.clicked.connect(self.ekipmanEkleyeGit)
                self.ui.pushButton_4.clicked.connect(self.bahceDurumunuGor)
                self.ui.pushButton_cikis.clicked.connect(self.cikisYap)
                
        def cikisYap(self):
                self.close()
                self.ilkSayfa = ilkSayfa_py.IlkSayfa()
                self.ilkSayfa.show()

        def bahceDurumunuGor(self):
            self.close()
            self.ilkSayfa = bahceDurumu.BahceDurumunuGor()
            self.ilkSayfa.show()

        def kullanicilariGoruntule(self):
            self.close()
            self.ilkSayfa = kullanicilariGoruntule.KullanicilariGoruntule()
            self.ilkSayfa.show()
        
        def kullaniciEkleyeGit(self):
                self.close()
                self.ilkSayfa = kullaniciEkle.KullaniciEkle()
                self.ilkSayfa.show()

        def kullaniciSileGit(self):
                self.close()
                self.ilkSayfa = kullaniciSil.KullaniciSil()
                self.ilkSayfa.show()

        def ekipmanlarYoneticiGit(self):
                self.close()
                self.ilkSayfa = ekipmanlarYonetici.EkipmanlarYonetici()
                self.ilkSayfa.show()
        
        def ekipmanEkleyeGit(self):
                self.close()
                self.ilkSayfa = ekipmanEkle.EkipmanEkle()
                self.ilkSayfa.show()
              
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = YoneticiAnaSayfa()
    window.show()
    sys.exit(app.exec_())