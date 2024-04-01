# 1. City Infrastructure Management Systemclass Vehicle:
# Task 1: Vehicle Registration System
print("-------------------- Task 1 --------------------\n")
class Vehicle:
    def __init__(self, reg_num, type_, owner):
        self.list = [owner, reg_num, type_]
        self.registration_number = reg_num
        self.type = type_
        self.owner = owner
    
    def update_owner(self, owner):
        self.list[0] = owner
        self.owner = owner

Alpha_Romeo = Vehicle(17745, "Guilia", "Haya")
Acura = Vehicle(11425, "TL", "Adam")
Ford = Vehicle(44635, "F-150", "Kevin")

print(Alpha_Romeo.owner)
print(Alpha_Romeo.list)
Alpha_Romeo.update_owner("Morgan")
print(Alpha_Romeo.list)
print(Alpha_Romeo.owner)


print("\n-------------------- Task 2 --------------------\n")
# Task 2: Event Management System Enhancement
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.count = 0

    def add_participant(self, new_participants = 1):
        self.count += new_participants
    
    def participant_count(self):
        return self.count

Valorant = Event("VCT FINALSSSSSSSSS", "FOREVERRR AND EVERRRR AND EVERRRRRR")
print(f"{Valorant.name}: {Valorant.date}")
Valorant.add_participant()
print(Valorant.participant_count())
Valorant.add_participant(9999)
print(Valorant.participant_count())

