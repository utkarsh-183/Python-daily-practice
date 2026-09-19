# age = int(input("Enter your age : "))
# print("Your age is : ", age)

# conditional Operator >,<, >=, <=, ==, !=
# print(age>18)
# print(age<18)
# print(age>=18)
# print(age<=18)
# print(age==18)
# print(age!=18)

# if(age>18):
#     print("You can vote")
# else:
#     print("you cannot vote")
# print("This is out of if-else statment")

applePrice = int(input("Enter apple price: "))

budget = int(input("Enter your budget: "))

if(budget - applePrice > 160):
    print("Add 1 kg apple to cart")
elif(budget - applePrice > 80):
    print("You can buy")
else:
    print("Out out budget")

print("??")
