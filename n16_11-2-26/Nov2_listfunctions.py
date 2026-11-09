numbers = [20, 2, 7, 6, 20, 13, 6, 2]

print(f"the duplicates are {numbers}")

some_rando_list = []

some_rando_list.append("blah")
#Works one at a time

print(some_rando_list)


some_rando_list.extend(["yadda", "hello", "ahoy", "blah", "yadda"])
#Does the same thing as append, you can just do multiple things at once

print(some_rando_list)


print(some_rando_list[2])
#will print "hello"

print(some_rando_list[-1])
#this will go to the back of the list. This will print "ahoy". [-2] would print "hello"


print(some_rando_list)

some_rando_list.pop()
#will remove the last one in the list

print(some_rando_list)

some_rando_list.pop(1)
#will remove "yadda" from the list


some_rando_list.remove("blah")
#Have to pass it the actual value, not the position in the list, and then it removes the first instance of that value


print(some_rando_list.count("blah"))
#will tell you how many times the given value is in the list


#the 'in' function will see if the value is in the list and return a Boolean
if "yadda" in some_rando_list:
    print("Found the word")
else:
    print("Word not there")

if "larping" in some_rando_list:
    print("Found the word")
else:
    print("Word not there")


some_rando_list.sort()
#This will sort the list into alphabetic order, always the default for string

print(some_rando_list)

#Dictionary
student_info = {
    "name": "Zendaya",
    "age": 30,
    "graduated": False
}