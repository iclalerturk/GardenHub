import psycopg2
class Ekipman_class:
    def __init__(self,ekipman_id=None, ekipman_adi=None, ekipman_sayisi=None, fiyat=None):
        self.ekipman_id = ekipman_id
        self.ekipman_adi = ekipman_adi
        self.ekipman_sayisi = ekipman_sayisi
        self.fiyat = fiyat
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
            print("Database connection failed:", e)

    def get_equipments(self):
        query = "SELECT ekipman_id, ekipman_adi, ekipman_sayisi, fiyat FROM ekipman"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return [Ekipman_class(row[0], row[1], row[2], row[3]) for row in rows]

    def rent_equipment(self, equipment_id,kullanici):
        query = "SELECT fiyat, ekipman_sayisi FROM ekipman WHERE ekipman_id = %s"
        self.cursor.execute(query, (equipment_id,))
        price = self.cursor.fetchone()[0]
        # sayi = self.cursor.fetchone()[1]
        if kullanici.butce < price:
           return False
        else:
            query = "UPDATE ekipman SET ekipman_sayisi = ekipman_sayisi - 1 WHERE ekipman_id = %s"
            self.cursor.execute(query, (equipment_id,))
            kullanici.butce -= price
            query = "UPDATE kullanicilar SET butce = %s WHERE kullanici_id = %s "
            self.cursor.execute(query, (kullanici.butce,kullanici.kullanici_id,))
            query = "SELECT * FROM kiralananEkipmanlar WHERE ekipman_id = %s and kullanici_id = %s"
            self.cursor.execute(query, (equipment_id,kullanici.kullanici_id,))
            if self.cursor.fetchone():
                query = "UPDATE kiralananEkipmanlar SET miktar= miktar + 1 WHERE ekipman_id = %s AND kullanici_id = %s"
                self.cursor.execute(query, (equipment_id, kullanici.kullanici_id,))
            else:
                query = "INSERT INTO kiralananEkipmanlar (ekipman_id, kullanici_id, miktar) VALUES (%s, %s, 1)"
                self.cursor.execute(query, (equipment_id, kullanici.kullanici_id,))

            print(kullanici.butce)
            self.conn.commit()
            return True

        