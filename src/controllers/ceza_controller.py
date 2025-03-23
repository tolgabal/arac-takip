import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..', 'models')))

from models.database import DbConnector
from models.entity.ceza import Ceza

class CezaRepository:
    def __init__(self):
        self.db = DbConnector()
        self.conn = self.db.connect()
        
    """Yeni bir ceza bilgisi ekler"""
    def insert_Ceza(self, ceza: Ceza):
        query = """
        INSERT INTO Ceza (arac_id, tarih, tutar, aciklama, odendi_mi)
        VALUES (?, ?, ?, ?, ?)
        """
            
        cursor = self.conn.cursor()
        cursor.execute(query,(ceza.arac_id, ceza.tarih, ceza.tutar, ceza.aciklama, ceza.odendi_mi))
        self.conn.commit()
        ceza.id = cursor.lastrowid
        print("Ceza eklemee islemi basarili",ceza)
          
    """Ceza listeleme"""
    def get_All_Ceza(self):
        query = "SELECT * FROM ceza"
        cursor = self.conn.cursor()   
        cursor.execute(query)
        return[Ceza.from_tuple(row) for row in cursor.fetchall()]    

    """Arac Id ile ceza getirme"""
    def get_Ceza_By_AracId(self, arac_id: int):
        query = "SELECT * FROM ceza WHERE arac_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query,(arac_id,))
        return Ceza.from_tuple(cursor.fetchall())
    
    """Ceza bilgisi guncelleme"""
    def update_Ceza(self, ceza: Ceza):
        if ceza.id is None:
            raise ValueError("Guncellenecek cezanin Id'si olmali.")
        
        query = """
            UPDATE ceza SET arac_id = ?, tarih = ?, tutar = ?, aciklama = ?, odendi_mi = ?
            WHERE id = ?
        """
        cursor = self.conn.cursor()
        cursor.execute(query,(ceza.arac_id, ceza.tarih, ceza.tutar, ceza.aciklama, ceza.odendi_mi))
        self.conn.commit()
        print("Ceza guncelleme islemi basarili.", ceza)
        
    "Ceza Silme"
    def delete_Ceza(self, ceza_id: int):
        query = "DELETE FROM ceza WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query,(ceza_id,))
        self.conn.commit()
        print("Ceza silme islemi basarili")
        
    def close(self):
        self.db.close()        
                    
            
        