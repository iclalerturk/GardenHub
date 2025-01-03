import psycopg2

class Urunler:
    def __init__(self,urun_id=None, urun_adi=None, kg=None, fiyat=None, sahip_id=None):
        self.urun_id = urun_id
        self.urun_adi = urun_adi
        self.kg = kg
        self.fiyat = fiyat
        self.sahip_id = sahip_id
        
        self.hostname = 'localhost'
        self.username = 'postgres'
        self.database = 'GardenHub'
        self.password = '1234'
        self.port_id = '5432'
        try:
            self.conn = psycopg2.connect(host=self.hostname, user=self.username, password=self.password, dbname=self.database, port=self.port_id                   
            )
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("Error: ", e)



    def get_urun_from_db(self):
        try:
            query = "SELECT urun_id, urun_adi, kg, fiyat, sahip_id from urunler"
            self.cursor.execute(query)
            user_data = self.cursor.fetchall()
            return [Urunler(row[0], row[1], row[2], row[3], row[4]) for row in user_data]
        except Exception as e:
            print("Error: ", e)
            return []
        
    def urunekle(self,urun_adi,kg,fiyat, sahip_id):
        
        self.cursor.execute("insert into urunler values( %s , %s, %s)",urun_adi, kg, fiyat, sahip_id)
    
    def urunSatinAl(self,urun_id,kg):
        query = "SELECT fiyat FROM urunler WHERE urun_id = %s"
        self.cursor.execute(query, (urun_id,))
        price = self.cursor.fetchone()[0]
        query = "UPDATE urunler SET kg = kg - %s WHERE urun_id = %s AND kg > 0"
        self.cursor.execute(query, (kg,urun_id,))
        self.conn.commit()

