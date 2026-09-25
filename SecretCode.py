# write a python program to translate a msg into secret code language 

# coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end
# else :
# simply reverse the string

# decoding :
# if the word contains less than 3 characters, reverse it
# else :
# remove 3 random characters from start to end. Now remove the last letter and append it to the begining
# your program shouls ask you want to code or decode

# import random
# import string

# msg = input("Enter your message: ")
# choice = input("Do you want to code or decode? ")

# words = msg.split()
# result = []

# if choice == "code":

#     for word in words:

#         if len(word) < 3:
#             word = word[::-1]
#             result.append(word)

#         else:
#             # Remove first character and put it at the end
#             word = word[1:] + word[0]

#             # Generate 3 random characters
#             random_chars = ''.join(
#                 random.choice(string.ascii_letters)
#                 for _ in range(3)
#             )

#             # Add random characters at beginning and end
#             word = random_chars + word + random_chars

#             result.append(word)

# elif choice == "decode":

#     for word in words:

#         if len(word) < 3:
#             word = word[::-1]
#             result.append(word)

#         else:
#             # Remove first 3 and last 3 characters
#             word = word[3:-3]

#             # Move last character to the beginning
#             word = word[-1] + word[:-1]

#             result.append(word)

# else:
#     print("Invalid choice!")

# if result:
#     print("Result:", " ".join(result))


import random 
import string

msg = input("Enter your message : ")
words = msg.split(" ")
coding = input("1 for Coding or 0 for Decoding : ")
coding = True if (coding == "1") else False
print (coding)
if(coding):
    neword = []
    for word in words:
        if(len(word)>=3):
            r1 = ''.join(random.choices(string.ascii_letters, k=3))
            r2 = ''.join(random.choices(string.ascii_letters, k=3))
            secret = r1 + word[1:] + word[0] + r2  # starts from index 1 and goes to the end and then append char at index 1
            neword.append(secret)
        else:
            neword.append(word[::-1])
    print(" ".join(neword))
            
else :
    neword = []
    for word in words:
        if(len(word)>=3):
            secret = word[3:-3]
            secret = secret[-1] + secret[:-1]
            neword.append(secret)
        else:
            neword.append(word[::-1])
    print(" ".join(neword))