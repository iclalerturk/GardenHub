from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import yoneticiAnaSayfa
import psycopg2

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
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(675, 280, 541, 520))
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
        self.verticalGroupBox.setGeometry(QtCore.QRect(40, 110, 450, 300))
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
        
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(360, 430, 121, 51))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Garden Hub"))
        self.label.setText(_translate("MainWindow", "EKİPMAN EKLE"))
        self.label_3.setText(_translate("MainWindow", "Ekipman Adı"))
        self.soyad_label.setText(_translate("MainWindow", "Ekipman Adedi"))
        self.label_5.setText(_translate("MainWindow", "Ekipman Fiyatı"))
        self.pushButton.setText(_translate("MainWindow", "EKLE"))
        self.pushButton_2.setText(_translate("MainWindow", "<- Geri"))
        self.label2.setText(_translate("MainWindow", "GARDEN HUB"))
import resimler_rc


class EkipmanEkle(QtWidgets.QMainWindow):
        def __init__(self) -> None:
                super().__init__()
                self.ui = Ui_MainWindow()  # Burada doğru bir şekilde ui nesnesi başlatılıyor.
                self.ui.setupUi(self)
                self.ui.pushButton_2.clicked.connect(self.geriGit)
                self.ui.pushButton.clicked.connect(self.add_equipment)
                self.hostname = 'localhost'
                self.username = 'postgres'
                self.database = 'GardenHub'
                self.password = '1234'
                self.port_id = '5432'
                try:
                    self.conn = psycopg2.connect(
                        host=self.hostname, 
                        user=self.username, 
                        password=self.password, 
                        dbname=self.database, 
                        port=self.port_id
                    )
                    self.cursor = self.conn.cursor()
                except Exception as e:
                    print("Error: ", e)
        def geriGit(self):
            self.close()
            self.ilkSayfa = yoneticiAnaSayfa.YoneticiAnaSayfa()
            self.ilkSayfa.show()
            self.close()
        def add_equipment(self):
            try:
                ekipman_adi=self.ui.ad_line.text()
                ekipman_sayisi=self.ui.soyad_line.text()
                fiyat=self.ui.mail_line.text()
                query="select ekipman_ekle(%s,%s,%s)" 
                self.cursor.execute(query, (ekipman_adi,ekipman_sayisi,fiyat))
                self.conn.commit()
                QMessageBox.information(self, "Bilgi", "Ekipman Eklendi.")
            except Exception as e:
                print("Error: ", e)
                self.conn.rollback() 
                QMessageBox.information(self, "Bilgi", "Ekipman Eklenemedi.")
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = EkipmanEkle()
    window.show()
    sys.exit(app.exec_())



