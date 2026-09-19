# time = int(input("Enter the current time: "))
# if(time>=0 and time<12):
#     print("Good 'morning' Sir")
# elif(time>=12 and time<17):
#     print("Good 'afternoon' Sir")
# elif(time>=17 and time<20):
#     print("Good 'evening' Sir")
# elif(time>=20 and time<24):
#     print("Good 'night' sir")

# else :
#     print("Invalid time")

# Not taking any input from user altough we take input actual time using datetime module
from datetime import datetime

current_time = datetime.now().hour

if current_time < 12:
    print("Good morning, Sir")

elif current_time < 17:
    print("Good afternoon, Sir")

elif current_time < 20:
    print("Good evening, Sir")

else:
    print("Good night, Sir")