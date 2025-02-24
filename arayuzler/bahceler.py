from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import kiralama
import bahce_class
import kullaniciAnaSayfa
import kullanicilar as Kullanici
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from datetime import date
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QIcon(':/gardenPic/saksı-Photoroom2.png'))
        MainWindow.setFixedSize(1920, 1080)
        MainWindow.setStyleSheet("background-color: rgb(47, 91, 76);\n"
"background-color: rgb(47, 91, 76);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(34, 136, 85);\n"
"background-color: rgb(47, 91, 76);")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_geri = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_geri.setGeometry(QtCore.QRect(20, 20, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_geri.setFont(font)
        self.pushButton_geri.setStyleSheet("""
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

        self.pushButton_geri.setObjectName("pushButton_geri")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(325, 20, 1300, 250))
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

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1300, 815, 261, 131))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"                background-color: rgb(131, 65, 0);\n"
"                border-radius: 10px;  /* Yuvarlaklık */\n"
"                padding: 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(170, 70, 0);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: rgb(145, 70, 0);\n"
"            }")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_bahcelerim = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_bahcelerim.setGeometry(QtCore.QRect(1300, 485, 261, 131))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(24)
        self.pushButton_bahcelerim.setFont(font)
        self.pushButton_bahcelerim.setStyleSheet("QPushButton {\n"
"                background-color: rgb(131, 65, 0);\n"
"                border-radius: 10px;  /* Yuvarlaklık */\n"
"                padding: 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(170, 70, 0);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: rgb(145, 70, 0);\n"
"            }")
        self.pushButton_bahcelerim.setObjectName("pushButton_bahcelerim")

        self.pushButton_bahce = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_bahce.setGeometry(QtCore.QRect(1300, 650, 261, 131))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        self.pushButton_bahce.setFont(font)
        self.pushButton_bahce.setStyleSheet("QPushButton {\n"
"                background-color: rgb(131, 65, 0);\n"
"                border-radius: 10px;  /* Yuvarlaklık */\n"
"                padding: 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(170, 70, 0);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: rgb(145, 70, 0);\n"
"            }")
        self.pushButton_bahce.setObjectName("pushButton_bahce")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 300, 721, 81))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"                background-color: rgb(131, 65, 0);\n"
"                border-radius: 10px;  /* Yuvarlaklık */\n"
"                padding: 10px;\n"
"           ")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(500, 400, 721, 550))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(170, 160, 140);\n"
"font: \"Maiandra GD\";")
        self.pushButton_7.setObjectName("7")
        self.gridLayout_3.addWidget(self.pushButton_7, 1, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(170, 160, 140);\n"
"font: \"Maiandra GD\";")
        self.pushButton_9.setObjectName("9")
        self.gridLayout_3.addWidget(self.pushButton_9, 3, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(170, 160, 140);\n"
"font: \"Maiandra GD\";")
        self.pushButton_10.setObjectName("10")
        self.gridLayout_3.addWidget(self.pushButton_10, 3, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(170, 160, 140);\n"
"font: \"Maiandra GD\";")
        self.pushButton_8.setObjectName("8")
        self.gridLayout_3.addWidget(self.pushButton_8, 1, 3, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(170, 160, 140);\n"
"font: \"Maiandra GD\";")
        self.pushButton_6.setObjectName("6")
        self.gridLayout_3.addWidget(self.pushButton_6, 1, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(170, 160, 140);\n"
"font: \"Maiandra GD\";")
        self.pushButton_5.setObjectName("5")
        self.gridLayout_3.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("background-color: rgb(170, 160, 140);\n"
"font: \"Maiandra GD\";")
        self.pushButton_1.setObjectName("1")
        self.gridLayout_3.addWidget(self.pushButton_1, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 160, 140);\n"
"font: \"Maiandra GD\";")
        self.pushButton_2.setObjectName("2")
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(170, 160, 140);\n"
"font: \"Maiandra GD\";")
        self.pushButton_3.setObjectName("3")
        self.gridLayout_3.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(170, 160, 140);\n"
"font: \"Maiandra GD\";")
        self.pushButton_4.setObjectName("4")
        self.gridLayout_3.addWidget(self.pushButton_4, 0, 3, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(170, 160, 140);\n"
"font: \"Maiandra GD\";")
        self.pushButton_12.setObjectName("12")
        self.gridLayout_3.addWidget(self.pushButton_12, 3, 3, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(170, 160, 140);\n"
"font: \"Maiandra GD\";")
        self.pushButton_14.setObjectName("14")
        self.gridLayout_3.addWidget(self.pushButton_14, 4, 1, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background-color: rgb(170, 160, 140);\n"
"font: \"Maiandra GD\";")
        self.pushButton_13.setObjectName("13")
        self.gridLayout_3.addWidget(self.pushButton_13, 4, 0, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background-color: rgb(170, 160, 140);\n"
"font: \"Maiandra GD\";")
        self.pushButton_15.setObjectName("15")
        self.gridLayout_3.addWidget(self.pushButton_15, 4, 2, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("background-color: rgb(170, 160, 140);\n"
"font: \"Maiandra GD\";")
        self.pushButton_16.setObjectName("16")
        self.gridLayout_3.addWidget(self.pushButton_16, 4, 3, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: rgb(170, 160, 140);\n"
"font: \"Maiandra GD\";")
        self.pushButton_11.setObjectName("11")
        self.gridLayout_3.addWidget(self.pushButton_11, 3, 2, 1, 1)

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(325, 20, 1300, 250))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(55)
        self.label2.setFont(font)
        self.label2.setStyleSheet("\n"
"background-image: url(:/gardenPic/ustYazi.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"")
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("titleLabel")



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
        MainWindow.setWindowTitle(_translate("MainWindow", "Garden Hub"))
        self.pushButton.setText(_translate("MainWindow", "Bahçe Kirala"))
        self.pushButton_bahcelerim.setText(_translate("MainWindow", "Kiraladığım\nBahçeler"))
        self.pushButton_bahce.setText(_translate("MainWindow", "Bahçeleri Türüne\n Göre Sınıflandır"))
        self.label.setText(_translate("MainWindow", "Bahçeler"))
        self.label2.setText(_translate("MainWindow", "GARDEN HUB"))
        self.pushButton_geri.setText(_translate("MainWindow", "<- Geri"))
        self.pushButton_7.setText(_translate("MainWindow", "\n"
"7\n"
""))
        self.pushButton_9.setText(_translate("MainWindow", "\n"
"9\n"
""))
        self.pushButton_10.setText(_translate("MainWindow", "\n"
"10\n"
""))
        self.pushButton_8.setText(_translate("MainWindow", "\n"
"8\n"
""))
        self.pushButton_6.setText(_translate("MainWindow", "\n"
"6\n"
""))
        self.pushButton_5.setText(_translate("MainWindow", "\n"
"5\n"
""))
        self.pushButton_1.setText(_translate("MainWindow", "\n"
"1\n"
""))
        self.pushButton_2.setText(_translate("MainWindow", "\n"
"2\n"
""))
        self.pushButton_3.setText(_translate("MainWindow", "\n"
"3\n"
""))
        self.pushButton_4.setText(_translate("MainWindow", "\n"
"4\n"
""))
        self.pushButton_12.setText(_translate("MainWindow", "\n"
"12\n"
""))
        self.pushButton_14.setText(_translate("MainWindow", "\n"
"14\n"
""))
        self.pushButton_13.setText(_translate("MainWindow", "\n"
"13\n"
""))
        self.pushButton_15.setText(_translate("MainWindow", "\n"
"15\n"
""))
        self.pushButton_16.setText(_translate("MainWindow", "\n"
"16\n"
""))
        self.pushButton_11.setText(_translate("MainWindow", "\n"
"11\n"
""))
import resimler_rc

class Bahceler(QtWidgets.QMainWindow):
        def __init__(self, kullanici: Kullanici.Kullanici) -> None:
            super().__init__()
            self.ui = Ui_MainWindow()  # Burada doğru bir şekilde ui nesnesi başlatılıyor.
            self.ui.setupUi(self)
            self.bahceRenkleri()
            self.ui.pushButton_geri.clicked.connect(self.geriGit)
            self.kullanici = kullanici
            self.ui.pushButton.clicked.connect(self.bahceKirala)
            self.ui.pushButton_bahcelerim.clicked.connect(self.kiraladigimBahceler)
            self.ui.pushButton_bahce.clicked.connect(self.bahceTuruSec)     
            self.ui.pushButton_1.clicked.connect(self.birSecildi)
            self.ui.pushButton_2.clicked.connect(self.ikiSecildi)
            self.ui.pushButton_3.clicked.connect(self.ucSecildi)
            self.ui.pushButton_4.clicked.connect(self.dortSecildi)
            self.ui.pushButton_5.clicked.connect(self.besSecildi)
            self.ui.pushButton_6.clicked.connect(self.altiSecildi)
            self.ui.pushButton_7.clicked.connect(self.yediSecildi)
            self.ui.pushButton_8.clicked.connect(self.sekizSecildi)
            self.ui.pushButton_9.clicked.connect(self.dokuzSecildi)
            self.ui.pushButton_10.clicked.connect(self.onSecildi)
            self.ui.pushButton_11.clicked.connect(self.onbirSecildi)
            self.ui.pushButton_12.clicked.connect(self.onikiSecildi)
            self.ui.pushButton_13.clicked.connect(self.onucSecildi)
            self.ui.pushButton_14.clicked.connect(self.ondortSecildi)
            self.ui.pushButton_15.clicked.connect(self.onbesSecildi)
            self.ui.pushButton_16.clicked.connect(self.onaltiSecildi)

        def kiraladigimBahceler(self):
                bahceler = kiralama.Kiralama().get_kiraladigim_bahceler(self.kullanici.kullanici_id)
                yazi = "Kiraladığım Bahçeler:\n"
                for bahce in bahceler:
                        yazi += f"Bahce Numarasi: {bahce[0]}\n"
                QMessageBox.information(self, "Kiraladığım Bahçeler", yazi)

        def bahceKirala(self):
                bahceNo, ok = QInputDialog.getDouble(
                        self, 
                        "Bahce Kirala", 
                        "Kiralamak istediğiniz bahce Numarasini girin:", 
                        0,        # Varsayılan değer
                        -99999,  # Minimum değer
                        999999,  # Maksimum değer
                        0        # Ondalık basamak sayısı
                )         
                if ok:  # Kullanıcı 'Tamam'a tıkladıysa
                        self.bahce = bahce_class.Bahce().get_bahce_from_db(bahceNo)
                        if self.bahce.durum == "Kiralanmis":
                                QMessageBox.warning(self, "Hata", "Bahçe zaten kiralanmış.")
                                return
                        else:   
                                if self.kullanici.butce < self.bahce.fiyat:
                                       QMessageBox.warning(self, "Hata", "Yetersiz Bakiye")
                                       return
                                else:
                                        kiralama.Kiralama().bahce_kirala(self.kullanici.kullanici_id, self.bahce.bahce_id, date.today())
                                        QMessageBox.information(self, "Başarılı", "Bahçe kiralama işlemi başarılı.\n kullanıcı tipi: Kiracı, bahce tipi: Kiralanmis olarak değiştiren trigger tetiklendi.")
                                        getattr(self.ui, f"pushButton_{self.bahce.bahce_id}").setStyleSheet("background-color: rgb(131, 65, 0);\n")
                                        self.kullanici.butce = self.kullanici.butce - self.bahce.fiyat 
                                        self.kullanici.bakiye_guncelle(self.kullanici.butce) 
                              

                else:
                        QMessageBox.warning(self, "İptal Edildi", "Kiralama işlemi iptal edildi.")

        def bahceRenkleri(self):
                for i in range(1, 17):
                        self.bahce = bahce_class.Bahce().get_bahce_from_db(i)
                        if self.bahce.durum == "Kiralanmis":
                                getattr(self.ui, f"pushButton_{i}").setStyleSheet("background-color: rgb(131, 65, 0);\n")
        
        def bahceTuruSec(self):
                tur, ok = QInputDialog.getText(
                        self, 
                        "Bahçe Türüne Göre Sınıflandırma", 
                        "Aramak istediğiniz bahçe türünü girin:", 
                        
                )           
                if ok: 
                        gelenBahceler = bahce_class.Bahce().get_bahce(tur)
                        if gelenBahceler:
                                yazi = "Toprak Türüne Göre Bahçeler:\n"
                                for bahce in gelenBahceler:
                                        yazi += f"Bahce Numarasi: {bahce[0]}\n"
                                QMessageBox.information(self, "Sonuç", yazi)       
                        else:
                                QMessageBox.information(self, "Sonuç Yok", "Belirtilen türde bahçe bulunamadı.")
                else:
                        QMessageBox.warning(self, "İptal Edildi", "İşlemi iptal edildi.")
                        
               



        def birSecildi(self):
                self.bahce_id = 1               
                self.bahce = bahce_class.Bahce().get_bahce_from_db(self.bahce_id)
                QMessageBox.information(self, "Bahçe Bilgileri", f"Alan: {self.bahce.alan}\nKonum: {self.bahce.konum}\nToprak Tipi: {self.bahce.toprak_tipi}\nDurum: {self.bahce.durum}\nFiyat: {self.bahce.fiyat}")
        def ikiSecildi(self):
                self.bahce_id = 2
                self.bahce = bahce_class.Bahce().get_bahce_from_db(self.bahce_id)
                QMessageBox.information(self, "Bahçe Bilgileri", f"Alan: {self.bahce.alan}\nKonum: {self.bahce.konum}\nToprak Tipi: {self.bahce.toprak_tipi}\nDurum: {self.bahce.durum}\nFiyat: {self.bahce.fiyat}")
        def ucSecildi(self):
                self.bahce_id = 3
                self.bahce = bahce_class.Bahce().get_bahce_from_db(self.bahce_id)
                QMessageBox.information(self, "Bahçe Bilgileri", f"Alan: {self.bahce.alan}\nKonum: {self.bahce.konum}\nToprak Tipi: {self.bahce.toprak_tipi}\nDurum: {self.bahce.durum}\nFiyat: {self.bahce.fiyat}")
        def dortSecildi(self):
                self.bahce_id = 4
                self.bahce = bahce_class.Bahce().get_bahce_from_db(self.bahce_id)
                QMessageBox.information(self, "Bahçe Bilgileri", f"Alan: {self.bahce.alan}\nKonum: {self.bahce.konum}\nToprak Tipi: {self.bahce.toprak_tipi}\nDurum: {self.bahce.durum}\nFiyat: {self.bahce.fiyat}")
        def besSecildi(self):
                self.bahce_id = 5
                self.bahce = bahce_class.Bahce().get_bahce_from_db(self.bahce_id)
                QMessageBox.information(self, "Bahçe Bilgileri", f"Alan: {self.bahce.alan}\nKonum: {self.bahce.konum}\nToprak Tipi: {self.bahce.toprak_tipi}\nDurum: {self.bahce.durum}\nFiyat: {self.bahce.fiyat}")
        def altiSecildi(self):
                self.bahce_id = 6
                self.bahce = bahce_class.Bahce().get_bahce_from_db(self.bahce_id)
                QMessageBox.information(self, "Bahçe Bilgileri", f"Alan: {self.bahce.alan}\nKonum: {self.bahce.konum}\nToprak Tipi: {self.bahce.toprak_tipi}\nDurum: {self.bahce.durum}\nFiyat: {self.bahce.fiyat}")
        def yediSecildi(self):
                self.bahce_id = 7
                self.bahce = bahce_class.Bahce().get_bahce_from_db(self.bahce_id)
                QMessageBox.information(self, "Bahçe Bilgileri", f"Alan: {self.bahce.alan}\nKonum: {self.bahce.konum}\nToprak Tipi: {self.bahce.toprak_tipi}\nDurum: {self.bahce.durum}\nFiyat: {self.bahce.fiyat}")
        def sekizSecildi(self):
                self.bahce_id = 8
                self.bahce = bahce_class.Bahce().get_bahce_from_db(self.bahce_id)
                QMessageBox.information(self, "Bahçe Bilgileri", f"Alan: {self.bahce.alan}\nKonum: {self.bahce.konum}\nToprak Tipi: {self.bahce.toprak_tipi}\nDurum: {self.bahce.durum}\nFiyat: {self.bahce.fiyat}")
        def dokuzSecildi(self):
                self.bahce_id = 9
                self.bahce = bahce_class.Bahce().get_bahce_from_db(self.bahce_id)
                QMessageBox.information(self, "Bahçe Bilgileri", f"Alan: {self.bahce.alan}\nKonum: {self.bahce.konum}\nToprak Tipi: {self.bahce.toprak_tipi}\nDurum: {self.bahce.durum}\nFiyat: {self.bahce.fiyat}")
        def onSecildi(self):
                self.bahce_id = 10
                self.bahce = bahce_class.Bahce().get_bahce_from_db(self.bahce_id)
                QMessageBox.information(self, "Bahçe Bilgileri", f"Alan: {self.bahce.alan}\nKonum: {self.bahce.konum}\nToprak Tipi: {self.bahce.toprak_tipi}\nDurum: {self.bahce.durum}\nFiyat: {self.bahce.fiyat}")
        def onbirSecildi(self):
                self.bahce_id = 11
                self.bahce = bahce_class.Bahce().get_bahce_from_db(self.bahce_id)
                QMessageBox.information(self, "Bahçe Bilgileri", f"Alan: {self.bahce.alan}\nKonum: {self.bahce.konum}\nToprak Tipi: {self.bahce.toprak_tipi}\nDurum: {self.bahce.durum}\nFiyat: {self.bahce.fiyat}")
        def onikiSecildi(self):
                self.bahce_id = 12
                self.bahce = bahce_class.Bahce().get_bahce_from_db(self.bahce_id)
                QMessageBox.information(self, "Bahçe Bilgileri", f"Alan: {self.bahce.alan}\nKonum: {self.bahce.konum}\nToprak Tipi: {self.bahce.toprak_tipi}\nDurum: {self.bahce.durum}\nFiyat: {self.bahce.fiyat}")
        def onucSecildi(self):
                self.bahce_id = 13
                self.bahce = bahce_class.Bahce().get_bahce_from_db(self.bahce_id)
                QMessageBox.information(self, "Bahçe Bilgileri", f"Alan: {self.bahce.alan}\nKonum: {self.bahce.konum}\nToprak Tipi: {self.bahce.toprak_tipi}\nDurum: {self.bahce.durum}\nFiyat: {self.bahce.fiyat}")
       
        def ondortSecildi(self):
                self.bahce_id = 14
                self.bahce = bahce_class.Bahce().get_bahce_from_db(self.bahce_id)
                QMessageBox.information(self, "Bahçe Bilgileri", f"Alan: {self.bahce.alan}\nKonum: {self.bahce.konum}\nToprak Tipi: {self.bahce.toprak_tipi}\nDurum: {self.bahce.durum}\nFiyat: {self.bahce.fiyat}")
        def onbesSecildi(self):
                self.bahce_id = 15
                self.bahce = bahce_class.Bahce().get_bahce_from_db(self.bahce_id)
                QMessageBox.information(self, "Bahçe Bilgileri", f"Alan: {self.bahce.alan}\nKonum: {self.bahce.konum}\nToprak Tipi: {self.bahce.toprak_tipi}\nDurum: {self.bahce.durum}\nFiyat: {self.bahce.fiyat}")
        def onaltiSecildi(self):
                self.bahce_id = 16
                self.bahce = bahce_class.Bahce().get_bahce_from_db(self.bahce_id)
                QMessageBox.information(self, "Bahçe Bilgileri", f"Alan: {self.bahce.alan}\nKonum: {self.bahce.konum}\nToprak Tipi: {self.bahce.toprak_tipi}\nDurum: {self.bahce.durum}\nFiyat: {self.bahce.fiyat}")

        def geriGit(self):
                self.close()
                self.ilkSayfa = kullaniciAnaSayfa.KullaniciAnaSayfa(self.kullanici)
                self.ilkSayfa.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Bahceler()
    window.show()
    sys.exit(app.exec_())