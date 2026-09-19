time = int(input("Enter the current time: "))
if(time>=0 and time<12):
    print("Good 'morning' Sir")
elif(time>=12 and time<17):
    print("Good 'afternoon' Sir")
elif(time>=17 and time<20):
    print("Good 'evening' Sir")
elif(time>=20 and time<24):
    print("Good 'night' sir")

else :
    print("Invalid time")