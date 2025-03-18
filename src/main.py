import sys
import os

# Bir üst klasöre çık, sonra 'models' klasörüne git
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'controllers')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..', 'models')))


from controllers.arac_controller import AracRepository  # Doğru modül adı ile içe aktar
from controllers.bakim_onarim_controller import BakimOnarimRepository
from models.entity.arac import Arac

# arac_repository nesnesini oluştur
arac_repo = AracRepository()
bakim_onarim_repo = BakimOnarimRepository()

# Yeni araç ekle
araba = Arac("20APP98", "2025", "Porsche", "911", "Yussy", "Siyah", 1)
#arac_repo.insert_arac("34ABC123", "2022", "BMW", "320i", "Ahmet Yılmaz", "Mavi", 1)
#arac_repo.insert_arac("06DEF456", "2020", "Mercedes", "C200", "Mehmet Kaya", "Siyah", 1)
arac_repo.insert_arac(araba)

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

#Yeni Bakim Onarim Ekle 
bakim_onarim_repo.insert_Bakim_Onarim(6, "Yag degisimi", "17.03.2025", "1234", "1250.40")
bakim_onarim_repo.insert_Bakim_Onarim(5, "Kilometre Sifirlama", "14.03.2025", "200000", "200")

#Tüm Bakim Onarimi Listeleme
bakim_onarimlar = bakim_onarim_repo.get_All_Bakim_Onarim()
print("Bakim-Onarimlar: ",bakim_onarimlar)

#Arac id ile bakim-onarim getirme
bakim = bakim_onarim_repo.get_Bakim_Onarim_By_AracId(5)
print("Bakim Olmus mu: ",bakim)

#Bakim Guncelleme
guncel_bakim = bakim_onarim_repo.update_Bakim_Onarim(1, 6, "Yanlis yag", "18.03.2025", "1234", "0")

#Bakim Silme
bakim_onarim_repo.delete_Bakim_Onarim(1)

# Bağlantıyı kapat
arac_repo.close()