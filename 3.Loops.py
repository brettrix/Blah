#Definite = We know how many times we want it to run
#Indfinite = We don't know how many tmes it will run

#for counter in range(5): #Definite
#    print(counter)

#for counter in range(100, 105): #Definite
#    print(counter)

#for counter in range(100, 106, 2): #Definite
#    print(counter)

#for i in range(0, 101, 5):
#    print(i)

#for i in range(100, -1, -5):
#    print(i)



#Indefinite (You can always keep it going.)
#age = int(input("How old are you?"))
#print(age)

#while age < 0:
#    print("You can't be negative years old!")
#    age = int(input("How old are you?"))


#age = int(input("How old are you?"))

#while age < 0:
    #print("You can't be negative years old!")
    #age = int(input("How old are you?"))

    #if (age == -16):
        #break #Will stop the loop because it says -16 is some form of exception

    #if (age == 15):
        #continue #Will not stop the loop because 15 is now not included


#Day 1, Appointment 1
#Day 1, Appointment 2
#...
#Day 1, Appointment 5
#Day 2, Appointment 1

for i in range(1, 4):
    for j in range(1,6):
        print(f"Day {i}, Appointment {j}")