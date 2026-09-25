marks = [12,34,65,32,78,99,12,47]

# index = 0
# for mark in marks:
#     print(mark)
#     if index == 5:
#         print("Utkarsh!!")
#     index += 1


for index, mark in enumerate(marks):
    print(index, mark)
    if index == 5:
        print("Utkarsh!!")
   