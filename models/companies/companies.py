from models.addresses.addresses import Address

class Company:
    def __init__(self,
                 title: str,
                 vat_id: str,
                 hq_address: str,
                 phone: str,
                 email: str) -> None:   
        self.title = title
        self.vat_id = vat_id
        self.hq_address = hq_address
        self.phone = phone
        self.email = email
        
    def __str__(self) -> str:
        return (f"Naziv: {self.title}\n"
                f"OIB: {self.vat_id}\n"
                f"Sjedište: {self.hq_address}\n"
                f"Telefon: {self.phone}\n"
                f"Email: {self.email}\n")
        
        
        