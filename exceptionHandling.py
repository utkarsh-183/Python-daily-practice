# try:
#     n = int(input("Enter the number: "))

#     print(f"Multiplication table of {n} is:")

#     for i in range(1, 11):
#         print(f"{n} x {i} = {n * i}")

# except Exception as e:
#     print("Error:", e)

# print("Some imp lines")
# print("End of code")


# Exception handling is a mechanism used to handle errors that occur while a program is running, so that the program does not terminate suddenly.

# --------------------------- finally keyword in python-------------------------

try:
    l = [1,3,5,4,8]
    i = int(input("Enter the number : "))
    print(l[i])
except:
    print("some error occured")
finally:
    print("I am always executed")