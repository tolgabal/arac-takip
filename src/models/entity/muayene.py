
class Muayene:
    def __init__(self,id=None,arac_id=0,baslangic_tarihi="",bitis_tarihi="",masraf=0):
        self.id=id,
        self.arac_id=arac_id,
        self.baslangic_tarihi=baslangic_tarihi,
        self.bitis_tarihi_bitis_tarihi,
        self.masraf=masraf
    
    def __repr__(self):
        return f"Muayene(id={self.id},arac_id={self.arac_id},baslangic_tarihi={self.baslangic_tarihi},bitis_tarihi={self.bitis_tarihi},masraf={self.masraf})"
    
    def to_dict(self):
        """Verileri sözlük (dict) formatına çevirir."""
        return{
            "id":self.id,
            "arac_id":self.arac_id,
            "baslangic_tarihi":self.baslangic_tarihi,
            "bitis_tarihi":self.bitis_tarihi,
            "masraf":self.masraf
            }
    @staticmethod()
    def from_tuple(data):
        """Veritabanından dönen tuple verisini muayene nesnesine çevirir"""
        if data is None:
            return None
        return Muayene(*data)
