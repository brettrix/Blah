#Author: Brett Rix
#Write a program that prompts the user for a first name, 
#last name, street address, city, state, and the birth year 
#of the individual. Calculate the age of the individual. 
#Print the concatenated full name all in upper case separated 
#by a space. Print the address on a separate line. Print the 
#city and state on another separate line separated by a tab. 
#Make sure the state is all upper case. Print the calculated 
#age in years on another separate line concatenated with "In 
#2020 ZZ was XX years old" - where ZZ is the first name and 
#XX is the calculated age in years.

first_name = input("Please input first name: ").upper()
last_name = input("Please input last name: ").upper()
street_address = input("Please input street address: ")
city = input("Please input city: ")
state = input("Please input state: ").upper()
birth_year = input("Please input birth year: ")

age = 2020 - int(birth_year)

print(first_name + " " + last_name)
print(street_address)
print(city, end="\t")
print(state)
print(f"In 2020 {first_name} was {age} years old")