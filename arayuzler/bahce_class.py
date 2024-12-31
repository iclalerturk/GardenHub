import psycopg2

class Bahce:
    def __init__(self, bahce_id=None, alan=None, konum=None, toprak_tipi=None, durum=None, fiyat=None):
        self.bahce_id = bahce_id
        self.alan = alan
        self.konum = konum
        self.toprak_tipi = toprak_tipi
        self.durum = durum
        self.fiyat = fiyat


    @staticmethod
    def get_bahce_from_db(bahce_id):
        hostname = 'localhost'
        username = 'postgres'
        database = 'GardenHub'
        password = '1234'
        port_id = '5432'
        try:
            conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port_id
                    
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Bahceler WHERE bahce_id = %s", (bahce_id,))
            user_data = cursor.fetchone()
            conn.close()
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
        



