import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QStackedWidget
)
from PyQt5.QtCore import Qt

class Kullanici:
    """Kullanıcı sınıfı (örnek için basitleştirilmiş)."""
    def __init__(self, isim, mail):
        self.isim = isim
        self.mail = mail

    @staticmethod
    def get_user_from_db(mail, sifre):
        # Burada veritabanı kontrolü yapılabilir. Örnek olarak sabit bir kullanıcı döndürüyoruz.
        if mail == "test@example.com" and sifre == "12345":
            return Kullanici(isim="Test Kullanıcı", mail=mail)
        return None


class GirisEkrani(QWidget):
    """Giriş ekranı."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.label = QLabel("Giriş Yapın")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("E-posta")
        self.layout.addWidget(self.email_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Şifre")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.login_button = QPushButton("Giriş Yap")
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button)

        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red;")
        self.layout.addWidget(self.error_label)

        self.setLayout(self.layout)

    def login(self):
        """Giriş işlemi."""
        email = self.email_input.text()
        sifre = self.password_input.text()

        kullanici = Kullanici.get_user_from_db(email, sifre)

        if kullanici:
            self.error_label.setText("")
            self.parent().go_to_main_page(kullanici)
        else:
            self.error_label.setText("Hatalı e-posta veya şifre!")


class AnaSayfa(QWidget):
    """Ana sayfa."""
    def __init__(self, kullanici, parent=None):
        super().__init__(parent)
        self.kullanici = kullanici
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.label = QLabel(f"Hoş geldiniz, {self.kullanici.isim}!")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        self.logout_button = QPushButton("Çıkış Yap")
        self.logout_button.clicked.connect(self.logout)
        self.layout.addWidget(self.logout_button)

        self.setLayout(self.layout)

    def logout(self):
        """Çıkış yap ve giriş ekranına dön."""
        self.parent().go_to_login_page()


class MainWindow(QWidget):
    """Ana pencere, sayfalar arası geçişi yönetir."""
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Giriş Sistemi")
        self.resize(400, 300)

        self.stack = QStackedWidget(self)
        self.giris_ekrani = GirisEkrani(self)
        self.stack.addWidget(self.giris_ekrani)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.stack)

    def go_to_main_page(self, kullanici):
        """Ana sayfaya geçiş."""
        self.ana_sayfa = AnaSayfa(kullanici, self)
        self.stack.addWidget(self.ana_sayfa)
        self.stack.setCurrentWidget(self.ana_sayfa)

    def go_to_login_page(self):
        """Giriş ekranına geri dön."""
        self.stack.setCurrentWidget(self.giris_ekrani)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
