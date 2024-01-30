from services.file_services import (get_last_id,
                                    get_contact)
#from models.add_new_contact import AddUser
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



"""
if get_last_id() != -1:
    id = get_last_id() + 1
else:
    id = 1

id_contact = 3
contact = get_contact(id_contact)

if contact != None:
    print(contact)
else:
    print(f'Ne postoji trazeni kontakt s ID-jem: {id_contact} u bazi!')
   
"""