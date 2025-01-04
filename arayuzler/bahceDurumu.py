
from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2
import yoneticiAnaSayfa

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
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
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1545, 750, 300, 175))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
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
        self.pushButton_3.setObjectName("pushButton_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "GARDEN HUB"))
        self.pushButton_2.setText(_translate("MainWindow", "<- Geri"))
        self.pushButton_3.setText(_translate("MainWindow", "İstenilen Kullanıcının\nKiralama Bilgilerini\n Gör"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Bahçe Numarası"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Kullanıcı Maili")) #bunu nasıl alıcaz analamadım 
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Kiralama Tarihi"))
        item = self.tableWidget.horizontalHeaderItem(3)
        

import resimler_rc


class BahceDurumunuGor(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()  # Burada doğru bir şekilde ui nesnesi başlatılıyor.
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.geriGit)
        self.ui.pushButton_3.clicked.connect(self.showMailDialog)
        self.load_bahce()
    
    def geriGit(self):
        self.close()
        self.ilkSayfa = yoneticiAnaSayfa.YoneticiAnaSayfa()
        self.ilkSayfa.show()
        
    def showMailDialog(self):
        mail, ok = QtWidgets.QInputDialog.getText(self, 'Mail Girin', 'Kullanıcı mailini girin:')
        if ok and mail:
            self.showKiralamaDetails(mail)
    
    def showKiralamaDetails(self, mail):
        hostname = 'localhost'
        username = 'postgres'
        database = 'GardenHub'
        password = '1234'
        port_id = '5432'
        try:
            conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port_id)
            cursor = conn.cursor()

            query = "SELECT kullanici_id FROM kullanicilar WHERE mail = %s"
            cursor.execute(query, (mail,))
            user_id = cursor.fetchone()
            if user_id:
                user_id = user_id[0]
                query = "SELECT bahce_id, baslangic_tarihi FROM Kiralamalar WHERE kullanici_id = %s"
                cursor.execute(query, (user_id,))
                rows = cursor.fetchall()

                if rows:
                    msg = QtWidgets.QMessageBox(self)
                    # msg.setIcon(QtWidgets.QMessageBox.Information)
                    msg.setWindowTitle("Kiralama Bilgileri")
                    msg.setText(f"Mail: {mail}")
                    table ="""
                    <table border='1' style='background-color: white; border-collapse: collapse; width: 100%;'>
                        <tr>
                            <th style='background-color: rgb(240, 240, 240);'>Bahçe Numarası</th>
                            <th style='background-color: rgb(240, 240, 240);'>Kiralama Tarihi</th>
                        </tr>
                    """
                    for row in rows:

                        table += f"<tr style='background-color: white;'><td>{row[0]}</td><td>{row[1].strftime('%Y-%m-%d')}</td></tr>"
                    table += "</table>"
                    msg.setInformativeText(table)
                    msg.setStyleSheet("""
                        QMessageBox {
                            background-color: rgb(255, 255, 255);  /* Açık yeşil arka plan */
                            color: black;  /* Yazı rengi */
                        }
                        QMessageBox QLabel {
                            background-color: rgb(255, 255, 255); 
                        }
                        QMessageBox QPushButton {
                            background-color: rgb(131, 65, 0);  /* Buton arka plan rengi */
                            color: black;  /* Buton yazı rengi */           
                        }
                        QMessageBox QPushButton:hover {
                            background-color: rgb(170, 70, 0);  /* Buton üzerine gelindiğinde renk değişimi */
                        }
                        QMessageBox QPushButton:pressed {
                            background-color: rgb(145, 70, 0);  /* Buton basıldığında renk değişimi */
                        }
                                      
                    """)
                    msg.exec_()
                else:
                    QtWidgets.QMessageBox.warning(self, "Uyarı", "Bu mail ile kiralanmış bir bahçe bulunmamaktadır.")
            else:
                QtWidgets.QMessageBox.warning(self, "Uyarı", "Geçersiz mail adresi.")
            conn.close()
        except Exception as e:
            print("Error: ", e)
            QtWidgets.QMessageBox.critical(self, "Error", f"Veritabanı hatası: {e}")
   
    def load_bahce(self):
        hostname = 'localhost'
        username = 'postgres'
        database = 'GardenHub'
        password = '1234'
        port_id = '5432'
        try:
            conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port_id                 
            )
            self.cursor = conn.cursor()

            query = "SELECT bahce_id,kullanici_id, baslangic_tarihi FROM Kiralamalar"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            query = "SELECT mail FROM kullanici_mail WHERE kullanici_id = %s" #kullanici_mail viewi kullanıldı
            conn.commit()
            self.ui.tableWidget.setRowCount(len(rows))
            for row_idx, row in enumerate(rows):
                self.cursor.execute(query,(row[1],))
                mail = self.cursor.fetchone()[0]
                conn.commit()
                self.ui.tableWidget.setRowCount(len(rows))
                self.ui.tableWidget.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.ui.tableWidget.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(mail))
                self.ui.tableWidget.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(row[2].strftime("%Y-%m-%d")))
            conn.close()       
               
        except Exception as e:
            print("Error: ", e)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = BahceDurumunuGor()
    window.show()
    sys.exit(app.exec_())