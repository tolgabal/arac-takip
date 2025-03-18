class BakimOnarim:
    def __init__(self,id,arac_id,aciklama="",tarih="",kilometre="",tutar=""):
        self.id=id
        self.arac_id = arac_id
        self.aciklama = aciklama
        self.tarih = tarih
        self.kilometre = kilometre
        self.tutar = tutar
        
    
    def __repr__(self):
        return f"BakimOnarim(id={self.id},arac_id={self.arac_id},aciklama={self.aciklama},tarih={self.tarih},kilometre={self.kilometre},tutar={self.tutar})"
    
    def to_dict(self):
        """verileri sözlük (dict) formatına çevirir. """
        return{
            "id" : self.id,
            "arac_id" : self.arac_id,
            "aciklama" : self.aciklama,
            "tarih" : self.tarih,
            "kilometre": self.kilometre,
            "tutar" : self.tutar
            }
    
    
    def from_tuple(data):
        """Veritabanından dönen tuple verisini Bakim_Onarim nesnesine çevirir """
        if data is None:
            return None
        
        return BakimOnarim(*data)