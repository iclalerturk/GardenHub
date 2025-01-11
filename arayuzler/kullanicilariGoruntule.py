from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2
import yoneticiAnaSayfa

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon(':/gardenPic/saksı-Photoroom2.png'))
        MainWindow.setFixedSize(1920, 1080)
        MainWindow.setStyleSheet("background-color: rgb(47, 91, 76);\n")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(47, 91, 76);")
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(555, 380, 922, 571))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("""

    QTableWidget::item {
        font: 12pt "Maiandra GD";  /* Hücre yazı tipi ve boyutu */
        background-color: rgb(191, 183, 165);  /* Hücre arka plan rengi */
        color: black;  /* Hücre yazı rengi */
    }
    QHeaderView::section {

        background-color: rgb(170, 160, 140);  /* Başlık arka plan rengi */
        color: brown;  /* Başlık yazı rengi */
        font: bold 12pt "Maiandra GD";
    }
    QTableWidget::item:selected {
        background-color: rgb(160, 160, 140);  /* Seçili hücre arka plan rengi */
    }
    
""")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(300)
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

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1545, 750, 300, 175))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
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

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(1545, 525, 300, 175))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        self.pushButton3.setFont(font)
        self.pushButton3.setStyleSheet("QPushButton {\n"
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
        self.pushButton3.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Garden Hub"))
        self.label.setText(_translate("MainWindow", "GARDEN HUB"))
        self.pushButton_2.setText(_translate("MainWindow", "<- Geri"))
        self.pushButton.setText(_translate("MainWindow", "KİRACI OLAN\nKULLANICILARI\nGÖRÜNTÜLE"))
        self.pushButton3.setText(_translate("MainWindow", "KİRACI OLMAYAN\nKULLANICILARI\nGÖRÜNTÜLE"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "KULLANICI ADI"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "KULLANICI SOYADI"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "KULLANICI MAİLİ"))

import resimler_rc

class KullanicilariGoruntule(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()  # Burada doğru bir şekilde ui nesnesi başlatılıyor.
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.geriGit)
        self.ui.pushButton.clicked.connect(self.get_kiraci_olan_kullanicilar)
        self.ui.pushButton3.clicked.connect(self.get_kiraci_olmayan_kullanicilar)
        self.get_user()

    def get_kiraci_olmayan_kullanicilar(self):
        hostname = 'localhost'
        username = 'postgres'
        database = 'GardenHub'
        password = '1234'
        port_id = '5432'
        try:
            conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port_id
            )
            cursor = conn.cursor()
            cursor.execute("SELECT isim,soyisim,mail From kullanicilar EXCEPT SELECT isim,soyisim,mail From kullanicilar WHERE user_type='Kiraci'")          
            users = cursor.fetchall()
            conn.close()
            self.ui.tableWidget.setRowCount(len(users))
            for row_idx, user in enumerate(users):
                self.ui.tableWidget.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(user[0]))
                self.ui.tableWidget.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(user[1]))
                self.ui.tableWidget.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(user[2]))
        except Exception as e:
            print



    def get_kiraci_olan_kullanicilar(self):
        hostname = 'localhost'
        username = 'postgres'
        database = 'GardenHub'
        password = '1234'
        port_id = '5432'
        try:
            conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port_id
            )
            cursor = conn.cursor()
            cursor.execute("SELECT isim,soyisim,mail From kullanicilar EXCEPT SELECT isim,soyisim,mail From kullanicilar WHERE user_type='Kullanici'")          
            users = cursor.fetchall()
            conn.close()
            self.ui.tableWidget.setRowCount(len(users))
            for row_idx, user in enumerate(users):
                self.ui.tableWidget.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(user[0]))
                self.ui.tableWidget.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(user[1]))
                self.ui.tableWidget.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(user[2]))
        except Exception as e:
            print("Error: ", e)


    def geriGit(self):
        self.close()
        self.ilkSayfa = yoneticiAnaSayfa.YoneticiAnaSayfa()
        self.ilkSayfa.show()
    
    def get_user(self):
        hostname = 'localhost'
        username = 'postgres'
        database = 'GardenHub'
        password = '1234'
        port_id = '5432'
        try:
            conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port_id
                    
            )
            cursor = conn.cursor()
            cursor.execute("SELECT isim,soyisim,mail From kullanicilar")
            
            users = cursor.fetchall()
            conn.close()
            self.ui.tableWidget.setRowCount(len(users))
            for row_idx, user in enumerate(users):
                self.ui.tableWidget.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(user[0]))
                self.ui.tableWidget.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(user[1]))
                self.ui.tableWidget.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(user[2]))
        except Exception as e:
            print("Error: ", e)

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = KullanicilariGoruntule()
    window.show()
    sys.exit(app.exec_())