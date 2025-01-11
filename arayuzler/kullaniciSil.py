from PyQt5 import QtCore, QtGui, QtWidgets
import yoneticiAnaSayfa
import psycopg2
from PyQt5.QtWidgets import QMessageBox
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
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(675, 320, 541, 400))
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
        self.label.setGeometry(QtCore.QRect(40, 40, 430, 61))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("""background-color: rgb(191, 183, 165);""")
        self.verticalGroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.verticalGroupBox.setGeometry(QtCore.QRect(40, 130, 450, 150))
        self.verticalGroupBox.setStyleSheet("background-color: rgb(191, 183, 165);\n"
"border-color:  rgb(191, 183, 165);\n"
"")
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        
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
        
        
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(360, 275, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: rgb(131, 65, 0);
                border-radius: 20px;  /* Yuvarlaklık */
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
        self.label.setText(_translate("MainWindow", "KULLANICI SİL"))
        self.label_5.setText(_translate("MainWindow", "E-Mail"))
        self.pushButton.setText(_translate("MainWindow", "SİL"))
        self.pushButton_2.setText(_translate("MainWindow", "<- Geri"))
        self.label2.setText(_translate("MainWindow", "GARDEN HUB"))
import resimler_rc


class KullaniciSil(QtWidgets.QMainWindow):
        def __init__(self) -> None:
                super().__init__()
                self.ui = Ui_MainWindow()  # Burada doğru bir şekilde ui nesnesi başlatılıyor.
                self.ui.setupUi(self)
                self.ui.pushButton_2.clicked.connect(self.geriGit)
                self.ui.pushButton.clicked.connect(self.user_remove)
        def geriGit(self):
            self.close()
            self.ilkSayfa = yoneticiAnaSayfa.YoneticiAnaSayfa()
            self.ilkSayfa.show()
            self.close()
        def user_remove(self):
            hostname = 'localhost'
            username = 'postgres'
            database = 'GardenHub'
            password = '1234'
            port_id = '5432'
            conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port_id          
            )
            cursor = conn.cursor()
            mail=self.ui.mail_line.text()
            cursor.execute("SELECT kullanici_mail_var_mi(%s);", (mail,))
            varmi = cursor.fetchone()[0]
            if varmi:                 
                query = "DELETE FROM kullanicilar WHERE mail = %s"
                cursor.execute(query, (mail,))
                conn.commit()
                conn.close()
                QMessageBox.information(self, "Bilgi", "Kullanıcı Silme İşlemi Başarılı.\n Trigger tetiklendi.\n Kiralamalar tablosundan kullanici silindi.\n Kiraladığı bahçeler bos durumuna getirildi.")
            else:
                QMessageBox.information(self, "Bilgi", "Bu Maile Sahip Kullanıcı Yok.")
                
                conn.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = KullaniciSil()
    window.show()
    sys.exit(app.exec_())
    



