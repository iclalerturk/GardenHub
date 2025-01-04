import psycopg2

class Yonetici:
    def __init__(self, mail, sifre):
        
        self.mail = mail
        self.sifre = sifre
    @staticmethod
    def get_admin_from_db(mail, sifre):
        hostname = 'localhost'
        username = 'postgres'
        database = 'GardenHub'
        password = '1234'
        port_id = '5432'
        try:
            conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port_id
                    
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM yonetici WHERE mail = %s AND sifre = %s", (mail, sifre))
            admin_data = cursor.fetchone()
            conn.close()
            if admin_data:
                return Yonetici(
                    
                    mail=admin_data[0],
                    sifre=admin_data[1],
                    
                )
            return None
        except Exception as e:
            print("Error: ", e)

    
        



