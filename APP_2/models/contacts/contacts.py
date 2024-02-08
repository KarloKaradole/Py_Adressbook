class Contact:
    def __init__(self,
                 id: int,
                 first_name: str,
                 last_name: str,
                 phone: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        
    def __str__(self) -> str:
        contact_card = f"\nIme: {self.first_name}\n"
        contact_card += f"Prezime: {self.last_name}\n"
        contact_card += f"Telefon: {self.phone}"
        return contact_card
    