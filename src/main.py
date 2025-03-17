import sys
import os

# Bir üst klasöre çık, sonra 'models' klasörüne git
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'controllers')))

from main_controller import AracRepository  # Doğru modül adı ile içe aktar

# Repository nesnesini oluştur
repo = AracRepository()

# Yeni araç ekle
repo.insert_arac("34ABC123", "2022", "BMW", "320i", "Ahmet Yılmaz", "Mavi", 1)
repo.insert_arac("06DEF456", "2020", "Mercedes", "C200", "Mehmet Kaya", "Siyah", 1)

# Tüm araçları getir ve yazdır
araclar = repo.get_all_araclar()
print("Araçlar:", araclar)

# Belirli bir aracı getir
arac = repo.get_arac_by_id(1)
print("Seçilen Araç:", arac)

# Araç bilgilerini güncelle
repo.update_arac(1, "34XYZ789", "2023", "Audi", "A6", "Ali Veli", "Beyaz", 1)

# Güncellenmiş araçları yazdır
araclar = repo.get_all_araclar()
print("Güncellenmiş Araçlar:", araclar)

# Araç sil
repo.delete_arac(2)

# Kalan araçları yazdır
araclar = repo.get_all_araclar()
print("Son Güncellenmiş Araçlar:", araclar)

# Bağlantıyı kapat
repo.close()