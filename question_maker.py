questions = []
answers =[]
falseanswer1 = []
falseanswer2 = []
cont = ''
while cont == '':
    questions.append(str(input("Enter a question ")))
    answers.append(str(input("Enter a correct answer ")))
    falseanswer1.append(str(input("Enter a false answer ")))
    falseanswer1.append(str(input("Enter a false answer ")))
    cont = str(input())

with open('answers.txt', 'w') as f:
    f.write(questions)
    f.write(answers)
    f.write(falseanswer1)
    f.write(falseanswer2)
f.close()