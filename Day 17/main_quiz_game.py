from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    each_question = item['text']
    each_answer = item['answer']
    question = Question(each_question, each_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print('You have completed the quiz')
print(f"Your final score is: {quiz.score}/{quiz.question_number}")



