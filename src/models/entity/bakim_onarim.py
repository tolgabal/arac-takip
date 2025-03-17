class Bakim_Onarim:
    def __init__(self, id=0, arac_id=0, aciklama="", tarih="", kilometre="", tutar=""):
        self.id = id
        self.arac_id = arac_id
        self.aciklama = aciklama
        self.tarih = tarih
        self.kilometre = kilometre
        self.tutar = tutar
        
    def __repr__(self):
        return f"Bakim_Onarim(id={self.id}, arac_id={self.arac_id}, aciklama='{self.aciklama}', tarih='{self.tarih}', kilometre='{self.kilometre}, tutar='{self.tutar}')"
    
    def to_dict(self):
        """Verileri sözlük (dict) formatına çevirir."""
        return{
            "id": self.id,
            "arac_id": self.arac_id,
            "aciklama": self.aciklama,
            "tarih": self.tarih,
            "kilometre": self.kilometre,
            "tutar": self.tutar
            }
    
    @staticmethod
    def from_tuple(data):
        """Veritabanından dönen tuple verisini Bakim_Onarim nesnesine çevirir."""
        if data is None:
            return None
        return Bakim_Onarim(*data)