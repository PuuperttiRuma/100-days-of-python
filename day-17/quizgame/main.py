from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(question_bank)
while quiz.has_questions_left():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your current score is: {quiz.score}/{len(question_bank)}")