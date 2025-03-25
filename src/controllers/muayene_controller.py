import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..', 'models')))

from models.database import DbConnector
from models.entity.muayene import Muayene

class MuayeneRepository:
    def __init__(self):
        self.db = DbConnector()
        self.conn = self.db.connect()
        
    """Yeni bir muayene bilgisi ekler"""
    def insert_Muayene(self, muayene: Muayene):
        query = """
        INSERT INTO muayene (arac_id, baslangic_tarihi, bitis_tarihi, masraf)
        VALUES (?, ?, ?, ?)
        """
        
        cursor = self.conn.cursor()
        cursor.execute(query,(muayene.arac_id, muayene.baslnagic_tarihi, muayene.bitis_tarihi, muayene.masraf))
        self.conn.commit()
        muayene.id = cursor.lastrowid
        print("Muayene ekleme islemi basarili", muayene)

    """Muayene listeleme"""   
    def get_All_Muayene(self):
        query = "SELECT * FROM muayene"
        cursor = self.conn.cursor()
        cursor.execute(query)
        return[Muayene.from_tuple(row) for row in cursor.fetchall()]

    """Arac Id ile muayene bilgisi getirme"""
    def get_Muayene_By_AracId(self, arac_id: int):
        query = "SELECT * FROM muayene where arac_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query,(arac_id,))
        return Muayene.from_tuple(cursor.fetchall())

    """Muayene bilgisi guncelleme""" 
    def update_Muayene(self, muayene: Muayene):
        if muayene.id is None:
            raise ValueError("Guncellenecek muayene bilgisinin Id'si olmali.")
            
        query = """
              UPDATE muayene SET arac_id = ?, baslangic_tarihi = ?, bitis_tarihi = ?, masraf = ?
              WHERE id = ?
        """
        cursor = self.conn.cursor()
        cursor.execute(query,(muayene.arac_id, muayene.baslangic_tarihi, muayene.bitis_tarihi, muayene.masraf))
        self.conn.commit()
        print("Muayene guncelleme islemi basarili", muayene)
      
    """Muayene silme"""
    def delete_Muayene(self, muayene_id: int):
        query = "DELETE FROM muayene WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query,(muayene_id,))
        self.conn.commit()
        print("Muayene silme islemi basarili")
        
    def close(self):
        self.db.close()        
            