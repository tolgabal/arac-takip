import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..', 'models')))

from models.database import DbConnector
from models.entity.bakim_onarim import BakimOnarim

class BakimOnarimRepository:
    def __init__(self):
        self.db = DbConnector()
        self.conn = self.db.connect()
    
    """ Yeni Bakım Onarım ekleme"""
    def insert_Bakim_Onarim(self, bakim_onarim: BakimOnarim):
        query = """
        INSERT INTO bakim_onarim (arac_id, aciklama, tarih, kilometre, tutar)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor = self.conn.cursor()
        cursor.execute(query,(bakim_onarim.arac_id, bakim_onarim.aciklama, bakim_onarim.tarih, bakim_onarim.kilometre, bakim_onarim.tutar))
        self.conn.commit()
        bakim_onarim.id = cursor.lastrowid
        print("Bakim Onarim Ekleme Işlemi basarili...",bakim_onarim)
        
    """Bakim Onarım Listeleme"""
    def get_All_Bakim_Onarim(self):
        query = "SELECT * FROM bakim_onarim"
        cursor = self.conn.cursor()
        cursor.execute(query)
        return [BakimOnarim.from_tuple(row) for row in cursor.fetchall()]
    
    """Arac id Ile Bakim Onarim Getirme"""
    def get_Bakim_Onarim_By_AracId(self, arac_id: int):
        query = "SELECT * FROM bakim_onarim WHERE arac_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query,(arac_id,))
        return BakimOnarim.from_tuple(cursor.fetchall())
    
    """Bakim Onarim Guncelleme"""
    def update_Bakim_Onarim(self,bakim_onarim : BakimOnarim):
        
        if bakim_onarim.id is None:
            raise ValueError("Güncellenecek bakım onarımın ID'si olmalı.")
       
        query = """
            UPDATE bakim_onarim SET arac_id = ?, aciklama = ?, tarih = ?, kilometre = ?, tutar = ?
            WHERE id = ?
        """
        cursor = self.conn.cursor()
        cursor.execute(query,(bakim_onarim.arac_id, bakim_onarim.aciklama, bakim_onarim.tarih, bakim_onarim.kilometre, bakim_onarim.tutar, bakim_onarim.bakim_id))
        self.conn.commit()
        print("Bakim Onarim Guncelleme Islemi Basarili...",bakim_onarim)
        
        
    """Bakim Onarim Silme"""
    def delete_Bakim_Onarim(self, bakim_id : int):
        query = "DELETE FROM bakim_onarim WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (bakim_id,))
        self.conn.commit()
        print("Bakim Onarim Silme Islemi Basarili...")
        
    
    def close(self):
        self.db.close()
        