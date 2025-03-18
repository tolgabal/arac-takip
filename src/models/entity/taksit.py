class Taksit:
    
    def __init__(self, id = None, sigorta_id = 0, taksit1_tarih = "", taksit2_tarih = "", taksit3_tarih = "", taksit4_tarih = "", taksit5_tarih = "", taksit6_tarih = "", 
                 taksit7_tarih = "", taksit8_tarih = "", taksit9_tarih = "", taksit10_tarih = "", taksit11_tarih = "", taksit12_tarih = "", ):
        self.id = id
        self.sigorta_id = sigorta_id
        self.taksit1_tarih = taksit1_tarih
        self.taksit2_tarih = taksit2_tarih
        self.taksit3_tarih = taksit3_tarih
        self.taksit4_tarih = taksit4_tarih
        self.taksit5_tarih = taksit5_tarih
        self.taksit6_tarih = taksit6_tarih
        self.taksit7_tarih = taksit7_tarih
        self.taksit8_tarih = taksit8_tarih
        self.taksit9_tarih = taksit9_tarih
        self.taksit10_tarih = taksit10_tarih
        self.taksit11_tarih = taksit11_tarih
        self.taksit12_tarih = taksit12_tarih
        
    def __ref__(self):
        
        return f"Taksit(id = {self.id}, sigorta_id = {self.sigorta_id}, taksit1_tarih = '{self.taksit1_tarih}', taksit2_tarih = '{self.taksit2_tarih}', taksit3_tarih = '{self.taksit3_tarih}', taksit4_tarih = '{self.taksit4_tarih}', taksit5_tarih = '{self.taksit5_tarih}', taksit6_tarih = '{self.taksit6_tarih}', taksit7_tarih = '{self.taksit7_tarih}', taksit8_tarih = '{self.taksit8_tarih}', taksit9_tarih = '{self.taksit9_tarih}', taksit10_tarih = '{self.taksit10_tarih}', taksit11_tarih = '{self.taksit11_tarih}', taksit12_tarih = '{self.taksit12_tarih}')"
    
    def to_dict(self):
        return{
            "id": self.id,
            "sigorta_id": self.id,
            "taksit1_tarih": self.taksit1_tarih,
            "taksit2_tarih": self.taksit2_tarih,
            "taksit3_tarih": self.taksit3_tarih,
            "taksit4_tarih": self.taksit4_tarih,
            "taksit5_tarih": self.taksit5_tarih,
            "taksit6_tarih": self.taksit6_tarih,
            "taksit7_tarih": self.taksit7_tarih,
            "taksit8_tarih": self.taksit8_tarih,
            "taksit9_tarih": self.taksit9_tarih,
            "taksit10_tarih": self.taksit10_tarih,
            "taksit11_tarih": self.taksit11_tarih,
            "taksit12_tarih": self.taksit12_tarih,
            }
    
    @staticmethod
    def from_tuple(data):
        if data is None:
            return None
        return Taksit(*data)