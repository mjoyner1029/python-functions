# Function to ask questions and check answers
def ask_questions(questions, correct_answers):
    score = 0
    for i in range(len(questions)):
        user_answer = input(questions[i] + " ").strip().title()  # Normalize input
        if user_answer == correct_answers[i]:
            print(get_correct_answer_feedback(user_answer))
            score += 1
        else:
            print('That is incorrect')
    return score

# Function to provide feedback based on the correct answer
def get_correct_answer_feedback(answer):
    feedback = {
        'BMW': 'Bayerische Motoren Werke (BMW) is correct',
        'Ferrari': 'Ferrari is correct, they are known for game-changing performance and unparalleled elegance',
        'Porsche': 'Porsche is known for their 911. Many believe it is the greatest sports car ever to be made.'
    }
    return feedback.get(answer, 'Correct answer')

# Main function to execute the quiz
def main_quiz_game():
    questions = [
        'What car company created the M series? ',
        'What super car company is owned by Fiat? ',
        'What car is famous for their 911 car? '
    ]
    correct_answers = ['BMW', 'Ferrari', 'Porsche']
    score = ask_questions(questions, correct_answers)
    print(f'Your final score is: {score}/{len(questions)}')

# Run the quiz game
main_quiz_game()
