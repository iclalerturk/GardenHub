from PyQt5 import QtCore, QtGui, QtWidgets
import yoneticiGiris
import kullaniciSecSayfasi_py

class kullaniciSecSayfasi(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.kullaniciSecSayfa = kullaniciSecSayfasi_py.Ui_MainWindow()
        self.kullaniciSecSayfa.setupUi(self)
        self.kullaniciSecSayfa.pushButton_4.clicked.connect(self.openYoneticiGiris)

    def openYoneticiGiris(self):
        self.yoneticiGirisSayfasi = yoneticiGiris.YoneticiGirisSayfa()
        self.yoneticiGirisSayfasi.show()
        self.close()    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = kullaniciSecSayfasi()
    ui.show()
    sys.exit(app.exec_())