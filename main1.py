# reading the contents of a file
# f = open('myfile.txt', 'r')
# text = f.read()
# print(text)
# f.close()

# writing a file
f = open('myfile2.txt', 'a')
f.write('Hello, World!')
f.close()


with open('myfile2.txt', 'a') as f:
    f.write("Hey I am inside with")