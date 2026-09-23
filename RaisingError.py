a = int(input("Enter number between 10 and 20 : "))

if(a<10 or a>20):
    raise ValueError("Value should be b/w 10 and 20")