number = int(input("Enter the number: "))
if(number<0):
    print("The number is negative")
elif(number>0):
    if(number<=10):
        print ("Number is between 0-10")
    elif(number<=100):
        print("Number is between 11-100")
    elif(number<=200):
        print("Number is between 101-200")
    else:
        print("Number is greater than 200")
else:
    print("The number is 0")