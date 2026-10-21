class Pet:
    
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.hunger = 0
        self.happiness = 50
        self.bond = 0

    def hunger_change(self, cravings, satisfaction):
        self.hunger -= cravings
        self.hunger += satisfaction

    def happiness_change(self, joy, misery):
        self.happiness -= misery
        self.happiness += joy

    def bond_change(self, accept, reject):
        self.bond -= reject
        self.bond += accept