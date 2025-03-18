class Ceza:
    def __init__(self,id=None, arac_id=0, tarih="",tutar="",aciklama="",odendi_mi=""):
        self.id = id
        self.arac_id = arac_id
        self.tarih = tarih
        self.tutar = tutar
        self.aciklama = aciklama
        self.odendi_mi = odendi_mi

    def __repr__(self):
        return f"Ceza(id={self.id},arac_id={self.arac_id},tarih={self.tarih},tutar={self.tutar},aciklama={self.aciklama},odendi_mi={self.odendi_mi})"
    
    def to_dict(self):
        """Verileri sözlük (dict) formatına çevirir."""
        return{
            "id":self.id,
            "arac_id":self.arac_id,
            "tarih" :self.tarih,
            "tutar":self.tutar,
            "aciklama":self.aciklama,
            "odendi_mi":self.odendi_mi
            }
    
    @staticmethod()
    def from_tuple(data):
        """Veritabanından dönen tuple verisini ceza nesnesine çevirir"""
        if data is None:
            return None
        return Ceza(*data)