class Arac:
    def __init__(self, id=None, plaka="", model_yili="", marka="", model="", kullanici="", renk="", aktiflik = 1):
        self.id = id
        self.plaka = plaka
        self.model_yili = model_yili
        self.marka = marka
        self.model = model
        self.kullanici = kullanici
        self.renk = renk
        self.aktiflik = aktiflik

    def __repr__(self):
        return f"Arac(id={self.id}, plaka='{self.plaka}', model_yili={self.model_yili}, marka='{self.marka}', model='{self.model}', kullanici='{self.kullanici}', renk='{self.renk}', aktiflik={self.aktiflik})"

    def to_dict(self):
        """Verileri sözlük (dict) formatına çevirir."""
        return {
            "id": self.id,
            "plaka": self.plaka,
            "model_yili": self.model_yili,
            "marka": self.marka,
            "model": self.model,
            "kullanici": self.kullanici,
            "renk": self.renk,
            "aktiflik": self.aktiflik
        }

    @staticmethod
    def from_tuple(data):
        """Veritabanından dönen tuple verisini Arac nesnesine çevirir."""
        if data is None:
            return None
        return Arac(*data)
    
