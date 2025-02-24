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

    @staticmethod
    def get_user_from_db(mail, sifre):
        hostname = 'localhost'
        username = 'postgres'
        database = 'GardenHub'
        password = '1234'
        port_id = '5432'
        try:
            conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port_id
                    
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM kullanicilar WHERE mail = %s AND sifre = %s", (mail, sifre))
            user_data = cursor.fetchone()
            conn.close()
            if user_data:
                return Kullanici(
                    isim=user_data[0],
                    soyisim=user_data[1],
                    kullanici_id=user_data[2],
                    mail=user_data[3],
                    sifre=user_data[4],
                    bdate=user_data[5],
                    butce=user_data[6],
                    user_type=user_data[7],
                )
            return None
        except Exception as e:
            print("Error: ", e)

    def bakiye_guncelle(self, bakiye):
        hostname = 'localhost'
        username = 'postgres'
        database = 'GardenHub'
        password = '1234'
        port_id = '5432'
        try:
            conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port_id)
            cursor = conn.cursor()

            cursor.execute("UPDATE kullanicilar SET butce = %s WHERE kullanici_id = %s", (bakiye, self.kullanici_id))
            conn.commit()
            conn.close()
        except Exception as e:
            print("Error: ", e) 



