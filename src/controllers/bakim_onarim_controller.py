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
       cursor.execute(query,(bakimonaarim.arac_id,bakimonarim.aciklama,bakimonaarim.tarih,bakimonaarim.kilometre,bakimonaarim.tutar))
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
        return BakimOnarim.from_tuple(cursor.fetchAll())
    
    """Bakim onarım güncelleme"""