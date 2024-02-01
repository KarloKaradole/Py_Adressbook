from services.file_services.file_manager import FileManager

def create_company_form():
    title = input("Upisite naziv tvrtke: ")
    vat_id = input("Upisite OIB tvrtke: ")
    
    FileManager.insert_company(title, vat_id)
    
    
    """
    header
    
    forma za unos podataka - input()-i
    
    poziv funkcije iz servisa za pohranu podataka
    """