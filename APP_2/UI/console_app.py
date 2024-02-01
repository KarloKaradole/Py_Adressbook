from UI.components.console_components.main_menu import main_menu
from UI.components.console_components.create_company_form import create_company_form

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
            case 0:
                return
        
    """
    1. Prikazi menu
    2. Omoguci izbor iz menija ovisno o izboru pokreni funkciju
    3. omoguci izlaz it aplikacije
    """