#! python3

import random

#The random quiz generator

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
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#Generate 35 quiz files and answer key files
for quizNum in range(35):
    quizFile = open('quizfile%s.txt' % (quizNum + 1), 'w')
    quizFileAnswers = open('quizfileanswer%s.txt' % (quizNum + 1), 'w')    
#Create the header for quiz file
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write(' ' * 20 + 'State Capitals Quiz (Form%s)' % (quizNum + 1))  
#Create the random list of keys
    states = list(capitals.keys())
    random.shuffle(states)
#Generate wrong answers with one correct answer and shuffle them
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        allAnswers = wrongAnswers + [correctAnswer]
        random.shuffle(allAnswers)
#TODO: Write 50 questions to a file and 50 key answers to another file
        quizFile.write('%s. What is capital of %s?' % (questionNum + 1), states[questionNum])
        for i in range(4):
            quizFile.write('ABCD'[i] + ': ' + allAnswers[i])

















