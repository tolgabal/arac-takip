import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..', 'models')))

from models.database import DbConnector
from models.entity.sigorta_kasko import SigortaKasko

class SigortaKaskoRepository:
    def __init__(self):
        self.db = DbConnector()
        self.conn = self.db.connect()
        
    """Yeni sigorta-kasko ekleme"""
    def insert_Sigorta_Kasko(self, sigorta_kasko: SigortaKasko):
        query = """
        INSERT INTO sigorta_kasko (arac_id, baslangic_tarihi, baslangic_saati, police_turu, aciklama, odeme_turu, tutar, odeme_tarihi)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor = self.conn.cursor()
        cursor.execute(query,(sigorta_kasko.arac_id, sigorta_kasko.baslangic_tarihi, sigorta_kasko.baslangic_saati, sigorta_kasko.police_turu, sigorta_kasko.aciklama, sigorta_kasko.odeme_turu, sigorta_kasko.tutar, sigorta_kasko.odeme_tarihi))
        self.conn.commit()
        sigorta_kasko.id = cursor.lastrowid
        print("Sigorta Kasko Ekleme Işlemi basarili...",sigorta_kasko)

    """Sigorta kasko listeleme"""
    def get_All_Sigorta_Kasko(self):
        query = "SELECT * FROM sigorta_kasko"
        cursor = self.conn.cursor()
        cursor.execute(query)
        return [SigortaKasko.from_tuple(row) for row in cursor.fetchall()]
    
    """Arac Id ile sigorta kasko getirme"""
    def get_Sigorta_Kasko_By_AracId(self, arac_id: int):
        query = "SELECT * FROM sigorta_kasko WHERE arac_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query,(arac_id,))
        return SigortaKasko.from_tuple(cursor.fetchall())
    
    """Sigorta Kasko Guncelleme"""
    def update_Sigorta_Kasko(self,sigorta_kasko : SigortaKasko):
        
        if sigorta_kasko.id is None:
            raise ValueError("Güncellenecek sigorta kasko ID'si olmalı.")
       
        query = """
            UPDATE sigorta_kasko SET arac_id = ?, baslangic_tarihi = ?, baslangic_saati = ?, police_turu = ?, aciklama = ?, odeme_turu = ?, tutar = ?, odeme_tarihi = ?
            WHERE id = ?
        """
        cursor = self.conn.cursor()
        cursor.execute(query,(sigorta_kasko.arac_id, sigorta_kasko.baslangic_tarihi, sigorta_kasko.baslangic_saati, sigorta_kasko.police_turu, sigorta_kasko.aciklama, sigorta_kasko.odeme_turu, sigorta_kasko.tutar, sigorta_kasko.odeme_tarihi))
        self.conn.commit()
        print("Sigorta Kasko Guncelleme Islemi Basarili...",sigorta_kasko)
        
    """Sigorta Kasko Silme"""
    def delete_Sigorta_Kasko(self, sigorta_id : int):
        query = "DELETE FROM sigorta_kasko WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (sigorta_id,))
        self.conn.commit()
        print("Sigorta Kasko Silme Islemi Basarili...")     
        
    def close(self):
        self.db.close()
        
            