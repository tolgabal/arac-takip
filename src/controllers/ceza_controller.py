import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..', 'models')))
from models.database import DbConnector
from model.entity.arac import Arac

class CezaRepository:
    def __init__(self):
        self.db = DbConnector()
        self.conn = self.db.connect()
    
    def insert_Ceza(self,arac_id,tarih,tutar,aciklama,odendi_mi):
        query = """
        INSERT INTO ceza (?,?,?,?,?)
        values()
        """
        cursor = self.conn.cursor()
        cursor.execute(query,(arac_id,tarih,tutar,aciklama,odendi_mi))
        self.conn.commit()
        print("ceza ekleme işlemi başarılı")
        
    def get_all_ceza(self):
        query = """
        select * from ceza
        """
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall() 
    
    def get_ceza_by_AracId(self,arac_id):
        query="""
        select * from ceza where arac_id = ?
        """
        cursor = self.conn.cursor()
        cursor.execute(query,(arac_id,))
        return [Arac.from_tuple(row) for row in cursor.fetchall()]
