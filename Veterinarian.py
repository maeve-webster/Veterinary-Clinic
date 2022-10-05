import secrets # Cryptographically more secure random number generator
import string
import datetime
from dateutil import parser

class Vet:

    clinic = "Guppies To Puppies Veterinarian Clinic"
    
    def __init__(self, name, specialty):
        id = ''.join([secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(10)])
        self.id = id
        self.name = "Dr. " + name.strip()
        self.specialty = specialty
        self.apt_book = [] #Each apt to be 1hr long


    def new_appointment(self, pet, date, time):
        time = time.lower().strip()
        if ":" not in time:
            print("Invalid formatted time entry. Example --> 3:00pm")
            return
        t, day_time = str(time[0:-3]), 
        hours, minutes = t.split(":")
        hours = int(hours)
        minutes = int(minutes)
        if hours > 12 or hours < 1:
            print("Invalid Time: 12 Hour Time entry used here. Enter hours between 1 and 12.")
            return
        if minutes < 0 or minutes > 59:
            print("Invalid Time: Enter minutes between 00 and 59")
            return
        if 'pm' in time:
            hours = hours + 12
    
        holidays = holidays.US()
        d = parser.parse(date)
        d = d + datetime.timedelta(hours=hours, minutes=minutes)
        if (datetime.weekday(d) > 5) or (d in holidays):
            print(date, "is a weekend or holiday. Please choose a time when the clinic is open.")
            return
        # Check if collision of apts for that doctor 

        # else add apt to doctor's apt_book