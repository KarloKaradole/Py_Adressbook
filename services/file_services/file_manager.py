import json
from models.companies.companies import Company


class FileManager:
    def __init__(self, file_type: str = "json",
                 file_path: str = "APP_2/files/companies.json") -> None:
        self.file_type = file_type
        self.file_path = file_path
        
        
    @classmethod    
    def insert_company(self, title, vat_id):
        print(f"Tvrtka {title} je uspjesno kreirana")
        print(f"Pripadajuci OIB je {vat_id}")
        input("\n Pritisnite ENTER za povratak.")
        
        company = Company(self, title, vat_id)
        
        try:
            with open(self.file_path, "a") as file_writer:
                json.dump(company, file_writer)
                
        except Exception as ex:
            print(f"{ex}")
            