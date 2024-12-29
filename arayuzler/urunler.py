import psycopg2

class Urunler:
    def __init__(self, adi, kilosu, fiyati, sahipi_id):
        self.adi = adi
        self.kilosu = kilosu
        self.fiyati = fiyati
        self.sahipi_id = sahipi_id


    
    @staticmethod
    def get_urun_from_db():
        hostname = 'localhost'
        username = 'postgres'
        database = 'GardenHub'
        password = '1234'
        port_id = '5432'
        try:
            conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port_id                   
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM urunler")
            user_data = cursor.fetchall()
            conn.close()
            if user_data:
                urunler_listesi = []
                for data in user_data:
                    urunler_listesi.append(Urunler(
                        adi=data[0],
                        kilosu=data[1],
                        fiyati=data[2],
                        sahipi_id=data[3]
                    ))
                return urunler_listesi  # Listeyi döndürüyoruz
            return None
        except Exception as e:
            print("Error: ", e)
            return None
        
    def urunekle(adi,kilosu,fiyati, sahipi_id):
        hostname = 'localhost'
        username = 'postgres'
        database = 'GardenHub'
        password = '1234'
        port_id = '5432'
        try:
            conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port_id                   
            )
            cursor = conn.cursor()
            cursor.execute("insert into urunler values( %s , %s, %s)",adi, kilosu, fiyati, sahipi_id)

        # cur.execute(query)
        # conn.commit()
        except Exception as e:
            print("Error: ", e)
            return None
