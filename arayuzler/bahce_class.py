import psycopg2

class Bahce:
    def __init__(self, bahce_id=None, alan=None, konum=None, toprak_tipi=None, durum=None, fiyat=None):
        self.bahce_id = bahce_id
        self.alan = alan
        self.konum = konum
        self.toprak_tipi = toprak_tipi
        self.durum = durum
        self.fiyat = fiyat

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

    def get_bahce_from_db(self,bahce_id):  
        try:
            self.cursor.execute("SELECT * FROM Bahceler WHERE bahce_id = %s", (bahce_id,))
            user_data = self.cursor.fetchone()
            self.conn.close()
            if bahce_id:
                return Bahce(
                    bahce_id=user_data[0],
                    alan=user_data[1],
                    konum=user_data[2],
                    toprak_tipi=user_data[3],
                    durum=user_data[4],
                    fiyat=user_data[5],
                    
                )
            return None
        except Exception as e:
            print("Error: ", e)
        
    def get_bahce(self, toprak):
        query = "SELECT bahce_id FROM bahceler WHERE toprak_tipi = %s ORDER BY bahce_id DESC"
        self.cursor.execute(query, (toprak,))
        rows = self.cursor.fetchall()
        return rows


