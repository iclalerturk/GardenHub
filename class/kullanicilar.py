from datetime import date, timedelta
import psycopg2
class Kullanici:
    def __init__(self, isim, soyisim, kullanici_id, mail, sifre, bdate=None, butce=0, user_type=None):
        self.isim = isim
        self.soyisim = soyisim
        self.kullanici_id = kullanici_id
        self.mail = mail
        self.sifre = sifre
        self.bdate = bdate
        self.butce = butce
        self.user_type = user_type

        # Validation checks
        if self.user_type not in ['Kiraci', 'Kullanici', None]:
            raise ValueError("user_type must be either 'Kiraci' or 'Kullanici'")

        if self.bdate and not self.is_18_years_old():
            raise ValueError("User must be at least 18 years old")

    def is_18_years_old(self):
        if not self.bdate:
            return False
        today = date.today()
        return today - self.bdate >= timedelta(days=18 * 365)

    def update_budget(self, amount):
        self.butce += amount

    def change_password(self, new_password):
        self.sifre = new_password
    def get_user_from_db(mail, sifre):
        try:
            conn = psycopg2.connect(
                hostname = 'localhost',
                username = 'postgres',
                database = 'GardenHub',
                password = '1234',
                port_id = '5432'
            )
            cursor = conn.cursor()
            query = "SELECT isim, soyisim, kullanici_id, mail, sifre, bdate, butce, user_type FROM kullanicilar WHERE mail = %s AND sifre = %s"
            cursor.execute(query, (mail, sifre))
            user_data = cursor.fetchone()

            # Kullanıcı bulunduysa, Kullanici nesnesi oluştur
            if user_data:
                return Kullanici(
                    isim=user_data[0],
                    soyisim=user_data[1],
                    kullanici_id=user_data[2],
                    mail=user_data[3],
                    sifre=user_data[4],
                    bdate=user_data[5],
                    butce=user_data[6],
                    user_type=user_data[7]
                )
            else:
                return None

        except Exception as e:
            print(f"Veritabanı hatası: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()


    def kullanici_giris():
        """Kullanıcı giriş işlemi."""
        mail = input("E-posta adresinizi girin: ")
        sifre = input("Şifrenizi girin: ")

        kullanici = Kullanici.get_user_from_db(mail, sifre)

        if kullanici:
            print(f"Hoş geldiniz, {kullanici.isim}!")
            return kullanici
        else:
            print("Giriş başarısız. E-posta veya şifre yanlış.")
            return None
       
        
        



