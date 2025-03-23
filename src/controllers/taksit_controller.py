import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..', 'models')))

from models.database import DbConnector
from models.entity.taksit import Taksit

class TaksitRepository:
    def __init__(self):
        self.db = DbConnector()
        self.conn = self.db.connect()
        
        
    """Yeni bir taksit bilgisi ekler"""
    def insert_Taksit(self, taksit: Taksit):
        query = """
        INSERT INTO taksit (sigorta_id, taksit1_tarih, taksit2_tarih, taksit3_tarih, taksit4_tarih, taksit5_tarih, taksit6_tarih, taksit7_tarih, taksit8_tarih, taksit9_tarih, taksit10_tarih, taksit11_tarih, taksit12_tarih)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        cursor = self.conn.cursor()
        cursor.execute(query,(taksit.sigorta_id,taksit.taksit1_tarih, taksit.taksit2_tarih, taksit.taksit3_tarih, taksit.taksit4_tarih, taksit.taksit5_tarih, taksit.taksit6_tarih, taksit.taksit7_tarih, taksit.taksit8_tarih, taksit.taksit9_tarih, taksit.taksit10_tarih, taksit.taksit11_tarih, taksit.taksit12_tarih))
        self.conn.commit()
        taksit.id = cursor.lastrowid
        print("Taksit ekleme islemi basarili", taksit)
        
    """Taksit listeleme"""
    def get_All_Taksit(self):
        query = "SELECT * FROM taksit"
        cursor = self.conn.cursor()
        cursor.execute(query)
        return[Taksit.from_tuple(row) for row in cursor.fetchall()]
    
    """Arac Id ile taksit getirme"""
    def get_Taksit_By_AracId(self, arac_id: int):
        query = "SELECT * FROM taksit WHERE arac_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query,(arac_id,))
        return Taksit.from_tuple(cursor.fetchall())
    
    """Taksit bilgisi guncelleme"""
    def update_Taksit(self, taksit: Taksit):
        if taksit.id is None:
            raise ValueError("Guncellenecek taksit bilgisinin Id'si olmalı.")
            
        query = """
              UPDATE taksit SET sigorta_id = ?, taksit1_tarih = ?, taksit2_tarih = ?, taksit3_tarih = ?, taksit4_tarih = ?, taksit5_tarih = ?, taksit6_tarih = ?, taksit7_tarih = ?, taksit8_tarih = ?, taksit9_tarih = ?, taksit10_tarih = ?, taksit11_tarih = ?, taksit12_tarih = ?
              WHERE id = ?
        """
        cursor = self.conn.cursor()
        cursor.execute(query,(taksit.sigorta_id, taksit.taksit1_tarih, taksit.taksit2_tarih, taksit.taksit3_tarih, taksit.taksit4_tarih, taksit.taksit5_tarih,taksit.taksit6_tarih,taksit.taksit7_tarih,taksit.taksit8_tarih,taksit.taksit9_tarih,taksit.taksit10_tarih,taksit.taksit11_tarih,taksit.taksit12_tarih))
        self.conn.commit()
        print("Taksit guncelleme islemi basarili.", taksit)
        
    """Taksit silme"""
    def delete_Taksit(self, taksit_id: int):
        query = "DELETE FROM taksit WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query,(taksit_id,))
        self.conn.commit()
        print("Taksit silme islemi basarili")
        
    def close(self):
        self.db.close()