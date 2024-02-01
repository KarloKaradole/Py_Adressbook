from services.file_services import get_last_id
from models.contacts import Contact

class AddUser(Contact):
    def __init__(self,
                 last_id: int,
                 first_name: str,
                 last_name: str,
                 phone: str):
        self.last_id = last_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        
    def add_new_user(self):
        while True:
            last_id=get_last_id() + 1       
            entry = f"{last_id};{self.first_name};{self.last_name};{self.phone}\n"
            
            try:  
                with open("APP_1/files/addressbook.txt","a") as file_writer:
                    file_writer.write(entry)
            except Exception as ex:
                print(f"Dogodila se greska: {ex}")
                
            if input("Zelite li unijeti jos jedan kontakt? (Da/Ne): ").lower() == "da":  
                print()
                self.first_name = input("Upisite vase ime: ")
                self.last_name = input("Upisite vase prezime: ")
                self.phone = input("Upisite vas broj telefona: ")
                print(f"\nUnesen je novi kontakt sa sljedecim informacijama:\n\nIme: {self.first_name}\nPrezime: {self.last_name}\nTelefon: {self.phone}")
                print()
            else:
                break
        
        def __str__(self) -> str:
            return "Hvala"
        
