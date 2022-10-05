import secrets # Cryptographically more secure random number generator
import string
import datetime
from dateutil import parser
from Patient import Patient

class Dog(Patient): #The Pets will inherit their owner

    clinic = "Guppies To Puppies Veterinarian Clinic"
    patient_type = "pet"
    
    def __init__(self, pet_name, breed_type):
        id = ''.join([secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(10)])
        self.id = id
        self.name = pet_name.strip().capitalize()
        self.breed_type = breed_type.strip().capitalize()
        self.owner = Patient.id
        Patient.add_pet(id)
        # self.pets =  IDs of each of this owner's pets