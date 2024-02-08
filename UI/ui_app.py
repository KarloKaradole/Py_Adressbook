from UI.components.console_components.main_menu import main_menu
from UI.components.console_components.create_company_form import create_company_form
from services.contact_services.contact_managers import ContactManager
from UI.components.console_components.select_contact_id_form import select_contact_id

def start_app(): 
    while True:
        main_menu()
        
        choice = int(input("Upisite broj iz izbornika: "))
        
        match choice:
            case 1:
                print("Izabrali smo izbor JEDAN")
                create_company_form()
                
            case 2:
                print("Izabrali smo izbor DVA")
                
            case 3:
                print("Izabrali smo izbor TRI")
                contact_manager = ContactManager()
                contacts = contact_manager.get_all()
                print(contacts)
                input("\nZa nastavak pritisnuti tipku ENTER")
                
            case 4:
                print("Izabrali smo izbor ČETIRI")
                #input ili forma za unos ID kontakta
                contact_id = select_contact_id()
                contact_manager = ContactManager()
                contacts = contact_manager.get_contact(contact_id)
                if contacts != []:
                    print(contacts)
                else:
                    print("Nema trazenih informacija u bazi ili se dogodila greška!")
                    
                input("\nZa nastavak pritisnuti tipku ENTER")
                
            case 0:
                return
        
    """
    1. Prikazi menu
    2. Omoguci izbor iz menija ovisno o izboru pokreni funkciju
    3. omoguci izlaz it aplikacije
    """