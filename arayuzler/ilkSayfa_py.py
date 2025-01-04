from PyQt5 import QtCore, QtGui, QtWidgets
import kullaniciSecSayfasi_py
import kayit_py


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        #setExtendedState(JFrame.MAXIMIZED_BOTH);
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(996, 672)
        #MainWindow.fixedsize(1920, 1080)
        MainWindow.setFixedSize(1920, 1080)
        #MainWindow.adjustSize()
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
        #self.pushButton_3.setStyleSheet("\n""\n""background-color: rgb(191, 183, 165);")
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "GİRİŞ YAP"))
        self.pushButton_4.setText(_translate("MainWindow", "KAYDOL"))
        self.label.setText(_translate("MainWindow", "GARDEN HUB"))
import resimler_rc


class IlkSayfa(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()  # Burada doğru bir şekilde ui nesnesi başlatılıyor.
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.openKullaniciSec)
        self.ui.pushButton_4.clicked.connect(self.openKaydol)

    def openKullaniciSec(self):
        self.kullaniciSecSayfasi = kullaniciSecSayfasi_py.kullaniciSecSayfasi()
        self.kullaniciSecSayfasi.show()
        self.close()

    def openKaydol(self):
        self.kaydolSayfasi = kayit_py.KaydolSayfa()
        self.kaydolSayfasi.show()
        self.close()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = IlkSayfa()
    window.show()
    sys.exit(app.exec_())