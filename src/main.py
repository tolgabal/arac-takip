import sys
import os

# Bir üst klasöre çık, sonra 'models' klasörüne git
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'controllers')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..', 'models')))


from controllers.arac_controller import AracRepository  # Doğru modül adı ile içe aktar
from controllers.bakim_onarim_controller import BakimOnarimRepository
from models.entity.arac import Arac
from models.entity.bakim_onarim import BakimOnarim

# arac_repository nesnesini oluştur
arac_repo = AracRepository()
bakim_onarim_repo = BakimOnarimRepository()

# Yeni araç ekle
araba = Arac(0,"20APP98", "2025", "Porsche", "911", "Yussy", "Siyah", 1)
#arac_repo.insert_arac("34ABC123", "2022", "BMW", "320i", "Ahmet Yılmaz", "Mavi", 1)
#arac_repo.insert_arac("06DEF456", "2020", "Mercedes", "C200", "Mehmet Kaya", "Siyah", 1)
arac_repo.insert_arac(araba)
"""
# Tüm araçları getir ve yazdır
araclar = arac_repo.get_all_araclar()
print("Araçlar:", araclar)

# Belirli bir aracı getir
arac = arac_repo.get_arac_by_id(1)
print("Seçilen Araç:", arac)

# Araç bilgilerini güncelle
#arac_repo.update_arac(1, "34XYZ789", "2023", "Audi", "A6", "Ali Veli", "Beyaz", 1)

# Güncellenmiş araçları yazdır
araclar = arac_repo.get_all_araclar()
print("Güncellenmiş Araçlar:", araclar)

# Araç sil
arac_repo.delete_arac(2)

# Kalan araçları yazdır
araclar = arac_repo.get_all_araclar()
print("Son Güncellenmiş Araçlar:", araclar)
"""
#Yeni Bakim Onarim Ekle 
bakim_onarim = BakimOnarim(0,31,"Yag Degisimi", "10.03.2025", "123", "250")
bakim_onarim_repo.insert_Bakim_Onarim(bakim_onarim)
#Tüm Bakim Onarimi Listeleme

#Arac id ile bakim-onarim getirme

#Bakim Guncelleme

#Bakim Silme

# Bağlantıyı kapat
arac_repo.close()