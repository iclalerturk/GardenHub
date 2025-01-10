from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2
import kullanicilar
import kullaniciAnaSayfa
import ilkSayfa_py
from PyQt5.QtWidgets import QMessageBox
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
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(675, 280, 541, 621))
        self.groupBox.setStyleSheet("""
QGroupBox {
    border: 2px solid rgb(131, 65, 0); /* Kenar rengi ve kalınlığı */
    border-radius: 15px; /* Köşe yuvarlama yarıçapı */
    margin-top: 10px; /* Başlık kısmı için üst boşluk */
    background-color: rgb(191, 183, 165); /* Arkaplan rengi */
}
""")

        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 40, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("""background-color: rgb(191, 183, 165);""")
        self.verticalGroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.verticalGroupBox.setGeometry(QtCore.QRect(40, 130, 450, 381))
        self.verticalGroupBox.setStyleSheet("background-color: rgb(191, 183, 165);\n"
"border-color:  rgb(191, 183, 165);\n"
"")
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalGroupBox)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.ad_line = QtWidgets.QLineEdit(self.verticalGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ad_line.setFont(font)
        self.ad_line.setStyleSheet("background-color: rgb(254, 255, 251);\n"
"border-radius: 10px;")
        self.ad_line.setObjectName("ad_line")
        self.verticalLayout_2.addWidget(self.ad_line)
        self.soyad_label = QtWidgets.QLabel(self.verticalGroupBox)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.soyad_label.setFont(font)
        self.soyad_label.setObjectName("soyad_label")
        self.verticalLayout_2.addWidget(self.soyad_label)
        self.soyad_line = QtWidgets.QLineEdit(self.verticalGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.soyad_line.setFont(font)
        self.soyad_line.setStyleSheet("background-color: rgb(254, 255, 251);\n"
"border-radius: 10px;")
        self.soyad_line.setObjectName("soyad_line")
        self.verticalLayout_2.addWidget(self.soyad_line)
        self.label_5 = QtWidgets.QLabel(self.verticalGroupBox)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.mail_line = QtWidgets.QLineEdit(self.verticalGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.mail_line.setFont(font)
        self.mail_line.setStyleSheet("background-color: rgb(254, 255, 251);\n"
"border-radius: 10px;"
"")
        self.mail_line.setObjectName("mail_line")
        self.verticalLayout_2.addWidget(self.mail_line)
        self.label_6 = QtWidgets.QLabel(self.verticalGroupBox)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.dateEdit = QtWidgets.QDateEdit(self.verticalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("background-color: rgb(254, 255, 251);\n"
"border-radius: 10px;"
"")
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_2.addWidget(self.dateEdit)
        self.label_7 = QtWidgets.QLabel(self.verticalGroupBox)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(" border-color: rgb(191, 183, 165);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.sifre_line = QtWidgets.QLineEdit(self.verticalGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sifre_line.setFont(font)
        self.sifre_line.setStyleSheet("background-color: rgb(254, 255, 251);\n"
"border-radius: 10px;"
"")
        self.sifre_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sifre_line.setObjectName("sifre_line")
        self.verticalLayout_2.addWidget(self.sifre_line)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(360, 530, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("""
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
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        
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
        self.label.setText(_translate("MainWindow", "KAYIT OL"))
        self.label_3.setText(_translate("MainWindow", "Ad"))
        self.soyad_label.setText(_translate("MainWindow", "Soyad"))
        self.label_5.setText(_translate("MainWindow", "E-Mail"))
        self.label_6.setText(_translate("MainWindow", "Doğum Tarihi"))
        self.label_7.setText(_translate("MainWindow", "Şifre"))
        self.pushButton.setText(_translate("MainWindow", "KAYDET"))
        self.pushButton_2.setText(_translate("MainWindow", "<- Geri"))
        self.label2.setText(_translate("MainWindow", "GARDEN HUB"))
import resimler_rc


class KaydolSayfa(QtWidgets.QMainWindow):
        def __init__(self) -> None:
                super().__init__()
                self.ui = Ui_MainWindow()  # Burada doğru bir şekilde ui nesnesi başlatılıyor.
                self.ui.setupUi(self)
                self.ui.pushButton_2.clicked.connect(self.geriGit)
                self.ui.pushButton.clicked.connect(self.kaydet)
        def geriGit(self):
            self.close()
            self.ilkSayfa = ilkSayfa_py.IlkSayfa()
            self.ilkSayfa.show()
            self.close()
        def kaydet(self):
            hostname = 'localhost'
            username = 'postgres'
            database = 'GardenHub'
            password = '1234'
            port_id = '5432'
            conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port_id          
            )
            cursor = conn.cursor()
            isim=self.ui.ad_line.text()
            soyisim=self.ui.soyad_line.text()
            mail=self.ui.mail_line.text()
            sifre=self.ui.sifre_line.text()
            bdate=self.ui.dateEdit.text()

            cursor.execute("SELECT kullanici_mail_var_mi(%s);", (mail,))
            conn.commit()
            varmi = cursor.fetchone()[0]
            if varmi:                 
                QMessageBox.information(self, "Bilgi", "Bu Maile Sahip Kullanıcı Var.")
                conn.close()
            else:             
                try:
                    query = "INSERT INTO kullanicilar VALUES( %s, %s, nextval('kullanici_id_seq'),%s, %s, %s)"               
                    cursor.execute(query, (isim, soyisim, mail, sifre, bdate))               
                    conn.commit()
                    conn.close()
                    kullanici = kullanicilar.Kullanici.get_user_from_db(mail, sifre) 
                    QMessageBox.information(self, "Bilgi", "Kaydınız başarı ile tamamlandı.\nkullanici tipini kullanici olarak oluşturan trigger tetiklendi.")
                    self.close()
                    self.ilkSayfa = kullaniciAnaSayfa.KullaniciAnaSayfa(kullanici)
                    self.ilkSayfa.show()     
                except Exception as e:
                    self.conn.rollback() 
                    QMessageBox.information(self, "Bilgi", "18 Yaşından küçükler kaydolamaz. Kayıt başarısız oldu.")
                    print(e)
                    conn.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = KaydolSayfa()
    window.show()
    sys.exit(app.exec_())



