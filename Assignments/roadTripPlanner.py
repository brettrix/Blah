#Author: Brett Rix
#Create a Python program that estimates the cost of a road trip. 
#Your program will ask the user for trip information, perform 
#calculations, and display a personalized trip-cost summary.


#Your program should ask the user for:
#• User’s name
user_name = input("Please input user's name: ")

#• Destination
destination = input("Please input destination: ")

#• One-way distance in miles
one_way_destination = float(input("Please input the one way distance in miles: "))

#• Vehicle miles per gallon
miles_per_gallon = float(input("Please input your vehicle's miles per gallon: "))

#• Gas price per gallon
price_per_gallon = float(input("Please input the gas price per gallon: "))

#• Number of travelers
number_of_travelers = int(input("Please input number of travelers: "))


#Your program should calculate:
#• Total miles for the round trip
total_miles = one_way_destination * 2

#• Gallons of gas needed
total_gallons_needed = total_miles / miles_per_gallon

#• Estimated gas cost
gas_cost = total_gallons_needed * price_per_gallon

#• Estimated cost per traveler
cost_per_traveler = gas_cost / number_of_travelers


#Display a readable trip summary that includes:
#• The traveler’s name
print(f"Hello, {user_name}!")

#• The destination
print(f"I hope you enjoy your trip to {destination}!")

#• The total estimated cost
print(f"The total cost for your trip will be ${gas_cost:,.2f},")

#• The estimated cost per traveler
print(f"and the cost per traveler will be ${cost_per_traveler:,.2f}.")

print("Have fun, be safe!")