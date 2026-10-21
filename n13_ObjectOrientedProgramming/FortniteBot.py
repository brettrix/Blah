class FortniteBot: #class

    max_health = 100

    def __init__(self, bot_name, start_position): #constructor -- runs once every time the class is used
        self.name = bot_name
        self.health = 100 #attribute

    def take_damage(self, amount): #method
        self.health -= amount