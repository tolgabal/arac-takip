import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..', 'models')))

from models.database import DbConnector
from models.entity.kilometre import Kilometre

class KilometreRepository:
    def __init__(self):
        self.db = DbConnector()
        self.conn = self.db.coonect()
        
    """Yeni bir kilometre bilgisi ekler"""
    def insert_Kilometre(self, kilometre: Kilometre):
        query = """
        INSERT INTO kilometre (arac_id, tarih, kilometre, kilometre_raporu)
        VALUES(?, ?, ?, ?)
        """

        cursor = self.conn.cursor()
        cursor.execute(query,(kilometre.arac_id, kilometre.tarih, kilometre.kilometre, kilometre.kilometre_raporu))
        self.conn.commit()
        kilometre.id = cursor.lastrowid
        print("Kilometre ekleme islemi basarili.", kilometre)   
        
    """Kilometre listeleme"""
    def get_All_Kilometre(self):
        query = "SELECT * FROM kilometre"
        cursor = self.conn.cursor()
        cursor.execute(query)
        return[Kilometre.from_tuple(row) for row in cursor.fetchall()]
    
    """Arac Id ile kilometre bilgisi getirme"""
    def get_Kilometre_By_AracId(self, arac_id: int):
        query = "SELECT * FROM kilometre WHERE arac_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query,(arac_id,))
        return Kilometre.from_tuple(cursor.fetchall())
    
    """Kilometre bilgisi güncelleme"""
    def update_Kilometre(self, kilometre : Kilometre):
        if kilometre.id is None:
            raise ValueError("Güncellenecek kilometre bilgisinin Id'si olmali.")
        
        query = """
              UPDATE kilometre SET arac_id = ?, tarih = ?, kilometre = ?, kilometre_raporu = ?
              WHERE id = ?
        """
        cursor = self.conn.cursor()
        cursor.execute(query,(kilometre.arac_id, kilometre.tarih, kilometre.kilometre, kilometre.kilometre_raporu))
        self.conn.commit()
        print("Kilometre bilgisi guncelleme islemi basarili", kilometre)
        
    """Kilometre Silme"""
    def delete_Kilometre(self, kilometre_id: int):
        query = "DELETE FROM kilometre WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query,(kilometre_id,))
        self.conn.commit()
        print("Kilometre silme islemi basarili...")

    def close(self):
        self.db.close()        
            
