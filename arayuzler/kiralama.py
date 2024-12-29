import psycopg2

class Kiralama:
    def __init__(self, kiralama_id, kullanici_id, bahce_id, baslangic_tarihi, sure):
        self.kiralama_id = kiralama_id
        self.kullanici_id = kullanici_id
        self.bahce_id = bahce_id
        self.baslangic_tarihi = baslangic_tarihi
        self.sure = sure
        

    @staticmethod
    def get_kiralama_from_db():
        hostname = 'localhost'
        username = 'postgres'
        database = 'GardenHub'
        password = '1234'
        port_id = '5432'
        try:
            conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port_id
                    
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Kiralamalar")
            user_data = cursor.fetchall()
            conn.close()
            if user_data:
                kiralamalar_listesi = []
                for data in user_data:
                    kiralamalar_listesi.append(Kiralama(
                        kiralama_id=data[0],
                        kullanici_id=data[1],
                        bahce_id=data[2],
                        baslangic_tarihi=data[3]
                        sure=data[4]
                    ))
                        
                return kiralamalar_listesi
            return None
        except Exception as e:
            print("Error: ", e)
    
    def tarla_kirala(kiralama_id, kullanici_id, bahce_id, baslangic_tarihi, sure):
        
        hostname = 'localhost'
        username = 'postgres'
        database = 'GardenHub'
        password = '1234'
        port_id = '5432'
        
        try:
            conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port_id                   
            )
            cursor = conn.cursor()
            cursor.execute("insert into Kiralamalar values( %d , %d, %d, %s ,%d )",kiralama_id, kullanici_id, bahce_id, baslangic_tarihi, sure)
            conn.close()
        # cur.execute(query)
        # conn.commit()
        except Exception as e:
            print("Error: ", e)
            return None
    
    
    def kiralama_iptal(kiralama_id):
        hostname = 'localhost'
        username = 'postgres'
        database = 'GardenHub'
        password = '1234'
        port_id = '5432'

        try:
            conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port_id                   
            )
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Kiralamalar WHERE kiralama_id = %d",kiralama_id)
            conn.close()
        
        except Exception as e:
            print("Error: ", e)
            return None
