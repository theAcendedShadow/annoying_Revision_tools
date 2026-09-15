#obnoxious filetype library
#this library handles the creation and use of .obxn questionfiles for
#the format used by obnoxious revision tools made by Lazlo Miodownik

def dump(name, question, answer, fake1, fake2):
    name = name.split('.', 1)[0]
    print(name)
    with open(f"{name}.obxn", 'a+') as obxn:
        obxn.writelines(f"{question},{answer},{fake1},{fake2}*")
    obxn.close()


    return None

def load(name):
    name = name.split('.', 1)[0]
    with open(f"{name}.obxn", 'r') as obxn:
        questions =[]
        answers = []
        falseanswer1 = []
        falseanswer2 = []
        line = obxn.readline()
        lines = line.split('*')
        for line in lines:
            line = line.strip()
            if line:
                line = line.split(',')
                if len(line) >= 4:
                    print(len(line))
                    questions.append(line[0])
                    answers.append(line[1])
                    falseanswer1.append(line[2])
                    falseanswer2.append(line[3])

        obxn.close()
    return questions, answers, falseanswer1, falseanswer2


