x = input("input first number ")
y = input("input second number ")

x = int(x)
y = int(y)

print("1. addition")
print("2. subtraction")
print("3. subtraction")
print("4. division")

choice = input("select operation ")
choice = int(choice)

if choice == 1 :
    print(x, "+", y)
    print(x+y)
    
   
elif choice == 2 :
    print(x, "-", y)
    print(x-y)

elif choice == 3 :
    print(x, "*", y)
    print(x*y)

elif choice == 4 :
    print(x, "/", y)
    print(x/y)

else :
    print("invalid choice")


    # functionalities to be added -
'''
--> read use case of elif
-> use if , else, elif
-> if choice is not [1,2,3,4] , print( " invalid choice ")
'''