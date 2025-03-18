import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..', 'models')))

from models.entity.vehicle import Arac
from models.database import DbConnector

 # Yeni oluşturduğumuz entity sınıfını içe aktardık


class AracRepository:
     def _init_(self):
         self.db = DbConnector()
         self.conn = self.db.connect()

     def insert_arac(self, arac: Arac):
         
         """Yeni bir araç ekler."""
         query = """
             INSERT INTO arac (plaka, model_yili, marka, model, kullanici, renk, aktiflik)
             VALUES (?, ?, ?, ?, ?, ?, ?)
          """
         cursor = self.conn.cursor()
         cursor.execute(query, (arac.plaka, arac.model_yili, arac.marka,arac.model, arac.kullanici, arac.renk, arac.aktiflik))
         self.conn.commit()
         arac.id = cursor.lastrowid
         # Yeni eklenen aracın ID'sini al
         print("Araç başarıyla eklendi:", arac)

     def get_all_araclar(self):
        
        """Tüm araçları getirir ve Arac nesnelerine dönüştürür."""
        query = "SELECT * FROM arac"
        cursor = self.conn.cursor()
        cursor.execute(query)       
        return [Arac.from_tuple(row) for row in cursor.fetchall()]


     def get_arac_by_id(self, arac_id: int):
        """Belirtilen ID'ye sahip aracı getirir."""
        query = "SELECT * FROM arac WHERE id = ?"
        cursor = self.conn.cursor()        
        cursor.execute(query, (arac_id,)) 
        return Arac.from_tuple(cursor.fetchone())

     def update_arac(self, arac: Arac):
        """Belirtilen ID'ye sahip aracı günceller."""
        if arac.id is None:
            raise ValueError("Güncellenecek aracın ID'si olmalı.")
        query = """        
        UPDATE arac         
        SET plaka = ?, model_yili = ?, marka = ?, model = ?, kullanici = ?, renk = ?, aktiflik = ?
        WHERE id = ? 
        """        
        cursor = self.conn.cursor()
        cursor.execute(query, (arac.plaka, arac.model_yili, arac.marka, arac.model, arac.kullanici, arac.renk, arac.aktiflik, arac.id))
        self.conn.commit()
        print("Araç bilgileri güncellendi:", arac)
        
        
     def delete_arac(self, arac_id: int): 
         
         """Belirtilen ID'ye sahip aracı siler.""" 
         query = "DELETE FROM arac WHERE id = ?"  
         cursor = self.conn.cursor()    
         cursor.execute(query, (arac_id,))  
         self.conn.commit()  
         print(f"Araç (ID: {arac_id}) silindi.") 
        
     def close(self): 
         """Veritabanı bağlantısını kapatır.""" 
         self.db.close()