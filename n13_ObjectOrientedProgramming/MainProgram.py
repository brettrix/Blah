from FortniteBot import FortniteBot

bot1 = FortniteBot("Chat", 89)
bot2 = FortniteBot("R2-D2", 22)
bot3 = FortniteBot("AM", 1)

bot1.take_damage(5)
bot2.take_damage(20)

print(bot1.name)
print(bot1.health)

print(bot1.name)
print(bot2.health)

print(bot1.name)
print(bot3.health)

print("Before")
print(bot1.max_health)
print(bot2.max_health)
print(bot3.max_health)

bot1.max_health = 200 #Will change the class level variable for one instance
FortniteBot.max_health = 200 #Will change the class level variable for all instances

print("After")
print(bot1.max_health)
print(bot2.max_health)
print(bot3.max_health)