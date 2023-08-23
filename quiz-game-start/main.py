from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []

for question in question_data:
    new_q = Question(question["text"], question["answer"])
    questionBank.append(new_q)

quiz = QuizBrain(questionBank)

quiz.next_question()
