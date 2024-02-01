from services.file_services import get_last_id
from models.add_new_contact import AddUser

first_name = input("Upisite vase ime: ")
last_name = input("Upisite vase prezime: ")
phone = input("Upisite vas broj telefona: ")

new_user = AddUser(get_last_id(),
                   first_name,
                   last_name,
                   phone)
print(f"\nUnesen je novi kontakt sa sljedecim informacijama:\n{new_user}")
print()
new_user.add_new_user()
