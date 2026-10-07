numbers = [1, 2, 3, 4, 5]

#def is_odd (numero):
#    odd = True
#
#    if numero % 2 == 0:
#        odd = False
#    if numero % 2 != 0: # <-- Don't really need this
#        odd = True
#
#    return odd

#is_odd = lambda numero: numero % 2 != 0 #<-- same as lines 3 - 11

from n10_2_CustomFunctions import is_odd #<-- you can pull functions from other files

#for num in numbers:
#    if num % 2 == 0:
#        print("Even")
#    else: #if num % 2 != 0: <-- you can use this to give you an error instead of just defaulting to odd
#        print("Odd")

for num in numbers:
    if is_odd (num): # <-- Call function instead of using the above
        print(f"{num} is odd.")
    else:
        print(f"{num} is even.")

#print(odd) <-- Can't see odd. It's scope is too limited