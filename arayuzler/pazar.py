from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog
import urunler
import kullaniciAnaSayfa
import kullanicilar as user

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
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
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
        
        self.pushButton_sirala = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sirala.setGeometry(QtCore.QRect(1550, 815, 261, 131))  # Butonun konumu
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_sirala.setFont(font)
        self.pushButton_sirala.setStyleSheet("QPushButton {\n"
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
        self.pushButton_sirala.setObjectName("pushButton_sirala")
        
        self.pushButton_aggregate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_aggregate.setGeometry(QtCore.QRect(1550, 650, 261, 131))  # Konum
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.pushButton_aggregate.setFont(font)
        self.pushButton_aggregate.setStyleSheet("""
        QPushButton {
            background-color: rgb(131, 65, 0);
            border-radius: 10px;
            padding: 10px;
        }
        QPushButton:hover {
            background-color: rgb(170, 70, 0);
        }
        QPushButton:pressed {
            background-color: rgb(145, 70, 0);
        }
        """)
        self.pushButton_aggregate.setObjectName("pushButton_aggregate")


        self.pushButton_stok = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stok.setGeometry(QtCore.QRect(1550, 485, 261, 131))  # Konum
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.pushButton_stok.setFont(font)
        self.pushButton_stok.setStyleSheet("""
        QPushButton {
            background-color: rgb(131, 65, 0);
            border-radius: 10px;
            padding: 10px;
        }
        QPushButton:hover {
            background-color: rgb(170, 70, 0);
        }
        QPushButton:pressed {
            background-color: rgb(145, 70, 0);
        }
        """)
        self.pushButton_stok.setObjectName("pushButton_stok")
        
        

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
        self.pushButton_sirala.setText("Fiyata Göre\nSırala")
        self.pushButton_aggregate.setText("10kg den fazla\nürünü olan Satıcıların\nStoğunu Göster")
        self.pushButton_stok.setText("Aradığın Ürünün\n Stoğunu Göster")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ÜRÜN ADI"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ÜRÜN KİLOSU"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ÜRÜN FİYATI"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ÜRÜNÜN SAHİBİ"))
import resimler_rc


class Pazar(QtWidgets.QMainWindow):
    def __init__(self,kullanici: user.Kullanici) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()  # Burada doğru bir şekilde ui nesnesi başlatılıyor.
        self.ui.setupUi(self)
        self.kullanici=kullanici
        self.urun=urunler.Urunler()
        self.ui.pushButton_2.clicked.connect(self.geriGit)
        self.ui.pushButton_sirala.clicked.connect(self.sirala)
        self.ui.pushButton_aggregate.clicked.connect(self.load_aggregated_data)
        self.ui.pushButton_stok.clicked.connect(self.cursorVeRecordlaUrununTumStogunuGor)
        self.load_data()
        
    def cursorVeRecordlaUrununTumStogunuGor(self):
        urunAdi, ok = QInputDialog.getText(
            self, 
            "Ürünün Stoğuna Bak", 
            "Aradığınız Ürünü Girin:", 
            
        )
                
        if ok:  # Kullanıcı 'Tamam'a tıkladıysa
            try:
                query = """
                    select urun_stogu_hesapla(%s)
                """
                self.urun.cursor.execute(query,(urunAdi,))
                result = self.urun.cursor.fetchall()
                
                self.ui.tableWidget.setRowCount(len(result))
                self.ui.tableWidget.setColumnCount(3)
                self.ui.tableWidget.setHorizontalHeaderLabels(["Ürünün Adı", "Toplam KG", "Toplam Fiyat"])
                for row_idx, row_data in enumerate(result):
                    parsed_data = row_data[row_idx].split(',')  # Virgülle ayır

                    for col_idx, data in enumerate(parsed_data):
                        self.ui.tableWidget.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(data.strip("()")))

            except Exception as e:
                QMessageBox.critical(self, "Hata", f"Veri yüklenirken bir hata oluştu: {e}")
      
        else:
            QMessageBox.warning(self, "İptal Edildi", "İşlem iptal edildi.")
        

    def geriGit(self):
        self.close()
        self.ilkSayfa = kullaniciAnaSayfa.KullaniciAnaSayfa(self.kullanici)
        self.ilkSayfa.show()
        
    def load_data(self, order_by_price=False):
        self.ui.tableWidget.setRowCount(0)
        gelenUrunler = self.urun.get_urun_from_db(order_by_price)
        self.ui.tableWidget.setRowCount(len(gelenUrunler))
        for row_idx, uruns in enumerate(gelenUrunler):
            self.ui.tableWidget.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(uruns.urun_adi))
            self.ui.tableWidget.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(str(uruns.kg)))
            self.ui.tableWidget.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(f"{uruns.fiyat:.2f} TL"))
            self.ui.tableWidget.setItem(row_idx, 3, QtWidgets.QTableWidgetItem(str(uruns.sahip_id)))
            button = QtWidgets.QPushButton("Satın Al")
            button.setStyleSheet("""
            QPushButton {
                background-color: rgb(131, 65, 0);
            }
            QPushButton:hover {
                background-color: rgb(170, 70, 0);
            }
            QPushButton:pressed {
                background-color: rgb(145, 70, 0);
            }
        """)
            self.ui.tableWidget.setCellWidget(row_idx, 4, button)
            button.clicked.connect(lambda _, r=row_idx: self.satinal_buton_tiklandi(r, gelenUrunler, order_by_price))
            
    def sirala(self):
        self.ui.tableWidget.setRowCount(0)
        self.load_data(order_by_price=True)

    def load_aggregated_data(self):
        try:
            query = """
                SELECT sahip_id, COUNT(*) AS sattigi_urun_sayisi, SUM(kg) AS toplam_kg
                FROM urunler
                GROUP BY sahip_id
                HAVING SUM(kg) > 10
                ORDER BY toplam_kg DESC
            """
            self.urun.cursor.execute(query)
            result = self.urun.cursor.fetchall()

            self.ui.tableWidget.setRowCount(len(result))
            self.ui.tableWidget.setColumnCount(3)
            self.ui.tableWidget.setHorizontalHeaderLabels(["Sahip ID", "Sattığı Ürün Sayısı", "Toplam KG"])
            for row_idx, row_data in enumerate(result):
                self.ui.tableWidget.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(str(row_data[0])))
                self.ui.tableWidget.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(str(row_data[1])))
                self.ui.tableWidget.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(f"{row_data[2]:.2f} KG"))
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Veri yüklenirken bir hata oluştu: {e}")

    
            
    def satinal_buton_tiklandi(self, row_index, gelenUrunler, order_by_price):
        if self.kullanici.butce>=gelenUrunler[row_index].fiyat:
            self.urun.urunSatinAl(gelenUrunler[row_index].urun_id,1)
            self.kullanici.butce -= gelenUrunler[row_index].fiyat
            self.kullanici.bakiye_guncelle(self.kullanici.butce)
            self.load_data(order_by_price) 
            QMessageBox.information(self, "Bilgi", "Satın alma işlemi başarılı.")
        else:
            bakiye_mesaji = f"Yetersiz Bakiye.\nBakiyeniz: {self.kullanici.butce} TL"
            QMessageBox.information(self, "Bakiye Görüntüle", bakiye_mesaji)
            print("Fiyat.",gelenUrunler[row_index].fiyat)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Pazar()
    window.show()
    sys.exit(app.exec_())