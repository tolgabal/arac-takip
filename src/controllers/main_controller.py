import sys
import os

# Bir üst klasöre çık, sonra 'models' klasörüne git
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..', 'models')))

from database import DbConnector  # Doğru modül adı ile içe aktar

class AracRepository:
    def __init__(self):
        self.db = DbConnector()
        self.conn = self.db.connect()

    def insert_arac(self, plaka, model_yili, marka, model, kullanici, renk, aktiflik):
        """Yeni bir araç ekler."""
        query = """
        INSERT INTO arac (plaka, model_yili, marka, model, kullanici, renk, aktiflik) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor = self.conn.cursor()
        cursor.execute(query, (plaka, model_yili, marka, model, kullanici, renk, aktiflik))
        self.conn.commit()
        print("Araç başarıyla eklendi.")

    def get_all_araclar(self):
        """Tüm araçları getirir."""
        query = "SELECT * FROM arac"
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def get_arac_by_id(self, arac_id):
        """Belirtilen ID'ye sahip aracı getirir."""
        query = "SELECT * FROM arac WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (arac_id,))
        return cursor.fetchone()

    def update_arac(self, arac_id, plaka, model_yili, marka, model, kullanici, renk, aktiflik):
        """Belirtilen ID'ye sahip aracı günceller."""
        query = """
        UPDATE arac 
        SET plaka = ?, model_yili = ?, marka = ?, model = ?, kullanici = ?, renk = ?, aktiflik = ?
        WHERE id = ?
        """
        cursor = self.conn.cursor()
        cursor.execute(query, (plaka, model_yili, marka, model, kullanici, renk, aktiflik, arac_id))
        self.conn.commit()
        print("Araç bilgileri güncellendi.")

    def delete_arac(self, arac_id):
        """Belirtilen ID'ye sahip aracı siler."""
        query = "DELETE FROM arac WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (arac_id,))
        self.conn.commit()
        print("Araç silindi.")

    def close(self):
        """Veritabanı bağlantısını kapatır."""
        self.db.close()