# Task 1

# Initialize score
score = 0

# Questions and answers
questions = [
    'What car company created the M series? ',
    'What super car company is owned by Fiat? ',
    'What car is famous for their 911 car? '
]

# Correct answers
correct_answers = ['BMW', 'Ferrari', 'Porsche']

# Ask questions and check answers
for i in range(len(questions)):
    user_answer = input(questions[i] + " ").strip().title()  # Normalize input
    if user_answer == correct_answers[i]:
        if user_answer == 'BMW':
            print('Bayerische Motoren Werke (BMW) is correct')
        elif user_answer == 'Ferrari':
            print('Ferrari is correct, they are known for game-changing performance and unparalleled elegance')
        elif user_answer == 'Porsche':
            print('Porsche is known for their 911. Many believe it is the greatest sports car ever to be made.')
        score += 1
    else:
        print('That is incorrect')

# Print final score
print(f'Your final score is {score}/{len(questions)}.')
