#Make a function that can be called
numbers = [14,2,3,45,5]


def is_odd(numero):
    odd = True

    if numero % 2 == 0:
        odd = False
    else:
        odd = True

    return odd


#Main program
#for num in numbers:
#   if num % 2 == 0:
#       print("Even")
#   else:
#       print("Odd")

#Main program using the defined function instead
for num in numbers:
    if is_odd(num):
        print(f"{num} is odd")
    else:
        print(f"{num} is even")