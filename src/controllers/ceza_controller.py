import sys
import os 

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..', 'models')))

from models.database import DbConnector

class CezaRpository:
    def __init__(self):
        self.db = DbConnector()
        self.conn = self.db.connect()
    
    def insert_Ceza(self,arac_id, tarih, tutar, aciklama, odendi_mi):
        query = """
            INSERT INTO ceza (arac_id, tarih, tutar, aciklama, odendi_mi)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor = self.conn.cursor()
        cursor.execute(query,(arac_id, tarih, tutar, aciklama, odendi_mi))
        self.conn.commit()
        print("Ceza Ekleme Islemi Basarili...")
    
    def get_all_ceza(self):
        query = "SELECT * FROM ceza"
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
    def get_Ceza_by_AracId(self,arac_id):
        query = "SELECT * FROM ceza WHERE arac_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query,(arac_id,))
        return cursor.fecthall()
        