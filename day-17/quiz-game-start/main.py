from question_model import Question
from data import question_data, trivia_data
from quiz_brain import QuizBrain

question_bank = []

for question in trivia_data:
    question_bank.append(Question(question['text'], question['answer']))

qb = QuizBrain(question_bank)
while qb.still_has_question():
    qb.next_question()

print(f"You've completed the quiz")
print(f"Your final score was: {qb.score}/{qb.question_number}")