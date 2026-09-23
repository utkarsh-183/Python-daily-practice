questions = [
    ["Which language is used for making the structure of website?",
     "HTML", "CSS", "Java Script", "C++", "A", 1000],

    ["Iostream header file is used in which language?",
     "Java", "Python", "Java Script", "C++", "D", 2000],

    ["What is the capital of Uttar Pradesh?",
     "Kanpur", "Lucknow", "Varanasi", "Prayagraj", "B", 5000],

    ["In which year IPL started?",
     "2006", "2007", "2008", "2005", "C", 10000],

    ["Why is the color of mud red?",
     "Iron", "Lead", "Barium", "Arsenic", "A", 20000],
]

amount = 0

for i in questions:

    print("\nQ)", i[0])
    print("A)", i[1])
    print("B)", i[2])
    print("C)", i[3])
    print("D)", i[4])

    correct_answer = i[5]

    user_answer = input("Enter your answer (A/B/C/D): ")

    if user_answer.upper() == correct_answer:
        amount = i[6]
        print("Correct!! 🎉")
        print("You Won ₹", amount)
    else:
        print("Wrong answer!!")
        print("Correct answer was:", correct_answer)
        break

print("The total amount won is:", amount)