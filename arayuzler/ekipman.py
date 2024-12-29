import psycopg2
class Ekipman:
    def __init__(self):
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
        query = "SELECT id, ekipman_adi, ekipman_adedi, fiyat FROM ekipmanlar"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return [Ekipman(row[0], row[1], row[2], row[3]) for row in rows]

    def rent_equipment(self, equipment_id):
        query = "UPDATE ekipmanlar SET ekipman_adedi = ekipman_adedi - 1 WHERE id = %s AND ekipman_adedi > 0"
        self.cursor.execute(query, (equipment_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0