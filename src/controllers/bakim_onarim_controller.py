import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..', 'models')))
from models.database import DbConnector
from models.entity.bakim_onarim import BakimOnarim

class BakimOnarimRepository:
    def __init__(self):
        self.db = DbConnector()
        self.conn = self.db.connect()
    
    def insert_Bakim_Onarim(self ,bakimonarim : BakimOnarim):
       query = """
       INSERT INTO bakim_onarim(arac_id,aciklama,tarih,kilometre,tutar)
       values(?,?,?,?,?)
       """
       
       cursor = self.conn.cursor()
       cursor.execute(query,(bakimonarim.arac_id,bakimonarim.aciklama,bakimonarim.tarih,bakimonarim.kilometre,bakimonarim.tutar))
       bakimonarim.id = cursor.lastrowid
       print("Bakim Onarim Ekleme Islemi basarili...",bakimonarim)
       
       
       """Tüm bakım onarım tablounu getir"""
    def get_All_Bakim_Onarim(self):
        query="""
        select * from bakim_onarim
        """
        cursor = self.conn.cursor()
        cursor.execute(query)
        return [BakimOnarim.from_tuple(row) for row in cursor.fetchAll()]
    
    
        """Id ye göre bakım onarım listesi getirme"""
    def get_Bakim_Onarim_By_AracId(self, arac_id: int):
        query="""select * from bakim_onarim where arac_id =?"""
        cursor = self.conn.cursor()
        cursor.execute(query,(arac_id,))
        return BakimOnarim.from_tuple(cursor.fetchone())
    
    """Bakim onarım güncelleme"""
    def update_Bakim_Onarim(self, bakimonarim : BakimOnarim):
        if bakimonarim.id is None:
            raise ValueError("Güncellenecek bakım onarımın ID'si olmalı.")
        query ="""
        update bakim_onarim set arac_id = ?, aciklama =?, tarih=?, kilometre=?,tutar = ?
        where id = ?
        """
        cursor = self.conn.cursor()
        cursor.execute(query,(bakimonarim.arac_id, bakimonarim.aciklama, bakimonarim.tarih, bakimonarim.kilometre, bakimonarim.tutar, bakimonarim.id))
        self.conn.commit()
        print("Bakim Onarim Guncelleme Islemi Basarili...",bakimonarim)
        
        
    """Bakım onarım silme"""
    def delete_Bakim_Onarim(self , araba_id : int):
        query = """delete from bakim_onarim where arac_id = ?"""
        cursor = self.conn.cursor()
        cursor.execute(query,(araba_id,))
        deleted_rows = cursor.rowcount  # Silinen satır sayısını al

        if deleted_rows == 0:
            return f"Uyarı: arac_id={araba_id} bulunamadı, silme işlemi başarısız!"
    
        self.conn.commit()  # Değişiklikleri kaydet
        return f"{deleted_rows} satır başarıyla silindi."
    
    
    def close(self):
        self.db.close()
    
        
    
    