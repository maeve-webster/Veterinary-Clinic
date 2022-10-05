import secrets # Cryptographically more secure random number generator
import string
import datetime
from dateutil import parser

class Patient(): #Owners of the pets. The Pets will inherit their owner

    clinic = "Guppies To Puppies Veterinarian Clinic"
    patient_type = "owner"
    
    def __init__(self, full_name, pets):
        id = ''.join([secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(10)])
        self.id = id
        self.first_name = full_name.split(" ")[0].strip().capitalize()
        self.last_name = full_name.split(" ")[1].strip().capitalize()
        self.pets =  [] #IDs of each of this owner's pets

    def add_pet(self, pet_id):
        self.pets.append(pet_id)
    
    def add_pets(self, pet_id_lst):
        if isinstance(pet_id_lst, str):
            self.add_pet(pet_id_lst)
        for pet_id in pet_id_lst:
            self.add_pets(pet_id)