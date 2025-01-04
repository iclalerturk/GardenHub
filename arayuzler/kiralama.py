import psycopg2
from PyQt5 import QtWidgets
class Kiralama:
    def __init__(self, kiralama_id=None, kullanici_id=None, bahce_id=None, baslangic_tarihi=None, sure=None, mail=None):
        self.kiralama_id = kiralama_id
        self.kullanici_id = kullanici_id
        self.bahce_id = bahce_id
        self.baslangic_tarihi = baslangic_tarihi
        self.sure = sure
        self.mail = mail
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
    
    def get_kiralama_from_db(self):
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT bahce_id,kullanici_id, baslangic_tarihi FROM Kiralamalar")
            self.conn.commit()
            user_data = self.cursor.fetchall()
            query = "SELECT mail FROM kullanici_mail WHERE kullanici_id = %s" #kullanici_mail viewi kullanıldı               
            if user_data:
                kiralamalar_listesi = []
                for data in user_data:
                    self.cursor.execute(query, (data[1],))
                    self.conn.commit()
                    mail2 = self.cursor.fetchone()[0]
                    kiralamalar_listesi.append(Kiralama(
                        bahce_id=data[0],
                        mail=mail2,
                        baslangic_tarihi=data[2],    
                    ))
                        
                return kiralamalar_listesi
            return None
    
    def showKiralamaDetails(self, mail, sonuc):
        
            self.cursor = self.conn.cursor()
            
            query = "SELECT kullanici_id FROM kullanici_mail WHERE mail = %s"
            self.cursor.execute(query, (mail,))
            user_id = self.cursor.fetchone()
            query = "SELECT bahce_id, baslangic_tarihi FROM Kiralamalar WHERE kullanici_id = %s"
            if user_id:               
                self.cursor.execute(query, (user_id,))
                rows = self.cursor.fetchall()
                
                return rows
                
            else:
                sonuc=1
                return None

            
    
    def bahce_kirala(self, kullanici_id, bahce_id, baslangic_tarihi):
        
        try:       
            self.cursor = self.conn.cursor()
            self.cursor.execute("INSERT INTO kiralamalar VALUES (nextval('kiralama_id_seq'),%s, %s, %s)", 
                       (kullanici_id, bahce_id, baslangic_tarihi))
            self.conn.commit()  
        except Exception as e:
            print("Error: ", e)
            return None
    
    
    def kiralama_iptal(self,kiralama_id):

        self.cursor = self.conn.cursor()
        self.cursor.execute("DELETE FROM Kiralamalar WHERE kiralama_id = %d",kiralama_id)
        self.conn.commit()