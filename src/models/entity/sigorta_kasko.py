class Sigorta_Kasko:
    def __init__(self, id=0, arac_id=0, baslangic_tarihi="", baslangic_saati="", police_turu="", aciklama="", odeme_turu="", tutar="", odeme_tarihi=""):
        self.id = id
        self.arac_id = arac_id
        self.baslangic_tarihi = baslangic_tarihi
        self.baslangic_saati = baslangic_Saati
        self.police_turu = police_turu
        self.aciklama = aciklama
        self.odeme_turu = odeme_turu
        self.tutar = tutar
        self.odeme_tarihi = odeme_tarihi
        
    def __repr__(self):
        return f"Sigorta_Kasko(id={self.id}, arac_id={self.arac_id}, baslangic_tarihi='{self.baslangic_tarihi}', baslangic_saati='{self.baslangic_saati}', police_turu='{self.police_turu}', aciklama='{self.aciklama}', odeme_turu='{self.odeme_turu}', tutar='{self.tutar}', odeme_tarihi='{self.odeme_tarihi}')"
    
    def to_dict(self):
        """Verileri sözlük (dict) formatına çevirir."""
        return{
            "id": self.id,
            "arac_id": self.arac_id,
            "baslangic_tarihi": self.baslnagic_tarihi,
            "baslangic_saati": self.baslangic_saati,
            "police_turu": self.police_turu,
            "aciklama": self.aciklama,
            "odeme_turu": self.odeme_turu,
            "tutar": self.tutar,
            "odeme_tarihi": self.odeme_tarihi
            }
    
    @staticmethod
    def from_tuple(data):
        """Veritabanından dönen tuple verisini Sigorta_Kasko nesnesine çevirir."""
        if data is None:
            return None
        return Sigorta_Kasko(*data)