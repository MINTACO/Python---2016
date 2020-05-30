#! python3
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ex8_randomQuizGenerator.py
@Time    :   2020/05/30 16:16:22
@Author  :   Darren 
@Version :   1.0
@Contact :   734876157@qq.com
@License :   (C)Copyright 2020, Darren
@Desc    :   Creates quizzes with questions and answers in random order, along with the answer key.
'''

# here put the import lib
import random
import os 

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# 判断是否存在quizFile和answerFile文件夹
if os.path.exists('.\\quizFile'):
    pass
else:
    os.makedirs('.\\quizFile')

if os.path.exists('.\\answerFile'):
    pass
else:
    os.makedirs('.\\answerFile')

# 生成35份试卷文件
for quizNum in range(35):
    # Create the quiz and answer key files.
    quizFile = open('.\\quizFile\\capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('.\\answerFile\\capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write('%s.What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')
        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()

totalSize = 0
for fileName in os.listdir('.\\'):
    totalSize += os.path.getsize(os.path.join('.', fileName))

print('总大小：' + str(round(totalSize/1024**2, 2)) + ' Mb')
        

    

