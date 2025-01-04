from PyQt5 import QtCore, QtGui, QtWidgets

import yoneticiGiris 
import kullaniciGiris
import ilkSayfa_py
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1920, 1080)
        MainWindow.setStyleSheet("background-color: rgb(47, 91, 76);\n"
"background-color: rgb(47, 91, 76);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(34, 136, 85);\n"
"background-color: rgb(47, 91, 76);")
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(11, 614, 878, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(450, 420, 1000, 350))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(150, 0, 150, 0)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("""
            QPushButton {
                background-color: rgb(191, 183, 165);
                border-radius: 20px;  /* Yuvarlaklık */
                padding: 10px;
                font-size: 38px;
            }
            QPushButton:hover {
                background-color: rgb(210, 200, 180);
            }
            QPushButton:pressed {
                background-color: rgb(170, 160, 140);
            }
        """)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("""
            QPushButton {
                background-color: rgb(191, 183, 165);
                border-radius: 20px;  /* Yuvarlaklık */
                padding: 10px;
                font-size: 38px;
            }
            QPushButton:hover {
                background-color: rgb(210, 200, 180);
            }
            QPushButton:pressed {
                background-color: rgb(170, 160, 140);
            }
        """)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)

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

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 20, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("""
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
        self.pushButton_2.setObjectName("pushButton_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "<- Geri"))
        self.pushButton_3.setText(_translate("MainWindow", "KULLANICI GİRİŞİ"))
        self.pushButton_4.setText(_translate("MainWindow", "YÖNETİCİ GİRİŞİ"))
        self.label.setText(_translate("MainWindow", "GARDEN HUB"))
    

import resimler_rc



class kullaniciSecSayfasi(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()  # Burada doğru bir şekilde ui nesnesi başlatılıyor.
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.openYoneticiGiris)
        self.ui.pushButton_3.clicked.connect(self.openKullaniciGiris)
        self.ui.pushButton_2.clicked.connect(self.geriGit)

    def geriGit(self):
        self.close()
        self.ilkSayfa = ilkSayfa_py.IlkSayfa()
        self.ilkSayfa.show()
        self.close()
    
    def openYoneticiGiris(self):
        self.yoneticiGirisSayfasi = yoneticiGiris.YoneticiGirisSayfa()
        self.yoneticiGirisSayfasi.show()
        self.close() 
    
    def openKullaniciGiris(self):
        self.kullaniciGirisSayfasi = kullaniciGiris.KullaniciGirisSayfa()
        self.kullaniciGirisSayfasi.show()
        self.close()
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = kullaniciSecSayfasi()
    window.show()
    sys.exit(app.exec_())