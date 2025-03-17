class Kilometre:
    def __init__(self, id=0, arac_id=0, tarih="", kilometre="", kilometre_raporu=""):
        self.id = id
        self.arac_id = arac_id
        self.tarih = tarih
        self.kilometre = kilometre
        self.kilometre_raporu = kilometre_raporu
        
    def __repr__(self):
        return f"Kilometre(id={self.id}, arac_id={self.arac_id}, tarih='{self.tarih}', kilometre='{self.kilometre}', kilometre_raporu='{self.kilometre_raporu}')"
    
    def to_dict(self):
        """Verileri sözlük (dict) formatına çevirir."""
        return{
            "id": self.id,
            "arac_id": self.arac_id,
            "tarih": self.tarih,
            "kilometre": self.kilometre,
            "kilometre_raporu": self.kilometre_raporu
            }
    
    @staticmethod
    def from_tuple(data):
        """Veritabanından dönen tuple verisini Kilometre nesnesine çevirir."""
        if data is None:
            return None
        return Kilometre(*data)