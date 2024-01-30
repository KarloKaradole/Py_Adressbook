"""from services.file_services import get_last_id

class AddUser():
        while True:
            last_id=get_last_id() + 1
            first_name = input("Upisite vase ime: ")
            last_name = input("Upisite vase prezime: ")
            phone = input("Upisite vas broj telefona: ")
            
            entry = f"{last_id};{first_name};{last_name};{phone}\n"
            
            try:  
                with open("files/addressbook.txt","a") as file_writer:
                    file_writer.write(entry)
            except Exception as ex:
                print(f"Dogodila se greska: {ex}")
            
            if input("Zelite li unijeti jos jedan kontakt? (Da/Ne): ").lower() != "da":  
                break
    
        def __str__(self) -> str:
             return "Hvala"
        
"""