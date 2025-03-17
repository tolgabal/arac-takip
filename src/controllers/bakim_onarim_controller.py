import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..', 'models')))

from models.database import DbConnector

class BakimOnarimRepository:
    def __init__(self):
        self.db = DbConnector()
        self.conn = self.db.connect()
    
    """ Yeni Bakım Onarım ekleme"""
    def insert_Bakim_Onarim(self,arac_id, aciklama, tarih, kilometre, tutar):
        query = """
        INSERT INTO bakim_onarim (arac_id, aciklama, tarih, kilometre, tutar)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor = self.conn.cursor()
        cursor.execute(query,(arac_id, aciklama, tarih, kilometre, tutar))
        self.conn.commit()
        print("Bakim Onarim Ekleme Işlemi basarili...")
        
    """Bakim Onarım Listeleme"""
    def get_All_Bakim_Onarim(self):
        query = "SELECT * FROM bakim_onarim"
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
    """Arac id Ile Bakim Onarim Getirme"""
    def get_Bakim_Onarim_By_AracId(self, arac_id):
        query = "SELECT * FROM bakim_onarim WHERE arac_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query,(arac_id,))
        return cursor.fetchall()
    
    """Bakim Onarim Guncelleme"""
    def update_Bakim_Onarim(self,bakim_id,arac_id, aciklama, tarih, kilometre, tutar):
        query = """
            UPDATE bakim_onarim SET arac_id = ?, aciklama = ?, tarih = ?, kilometre = ?, tutar = ?
            WHERE id = ?
        """
        cursor = self.conn.cursor()
        cursor.execute(query,(arac_id, aciklama, tarih, kilometre, tutar, bakim_id))
        self.conn.commit()
        print("Bakim Onarim Guncelleme Islemi Basarili...")
        
        
    """Bakim Onarim Silme"""
    def delete_Bakim_Onarim(self,bakim_id):
        query = "DELETE FROM bakim_onarim WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (bakim_id,))
        self.conn.commit()
        print("Bakim Onarim Silme Islemi Basarili...")
        
    
    def close(self):
        self.db.close()
        