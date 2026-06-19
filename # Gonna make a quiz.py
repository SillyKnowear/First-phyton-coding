# Gonna make a quiz

print('Welcome to the quiz!')
print("Answer the following questions:")

questions = [
    'What is the capital of United States?',
    'What is the largest animal in the world?',
    'What is the smallest country in the world?',
    'How many days are in a year?',
    'What is the capital of France?',
    'What is the largest ocean in the world?'

]

answers = [
    'Washington, D.C.',
    'Blue whale',
    'Vatican City',
    '365',
    'Paris',
    'Pacific Ocean'
]

score = 0

for i in range(len(questions)):
    print(questions[i])
    user_answer = input('Your answer: ')
    if user_answer == answers[i]:
        print('Correct!')
        score += 1
    else:
        print('Incorrect! The correct answer is: ' + answers[i])

        print('Quiz done! Your score is', score, 'out of 6')