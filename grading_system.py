marks = input("enter your marks here\n")
marks = int(marks)


if 90 < marks <= 100 :
    print("Your grade is " + 'A1')
    print("PASS")

elif 80 < marks <=90 :
    print("Your grade is " + 'A2')
    print("PASS")

elif 70 < marks <=80 :
    print("Your grade is " + 'B1')
    print("PASS")

elif 60 < marks <= 70 :
    print("Your grade is " + 'B2')
    print("PASS")

elif 50 < marks <=60 :
    print("Your grade is " + 'C1')
    print("PASS")

elif 40 < marks <=50 :
    print("Your grade is " + 'C2')
    print("PASS")

elif 32 < marks <= 40 :
    print("Your grade is " + 'D')
    print("PASS")
else :
    print("FAIL")