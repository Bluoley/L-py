from questionBrain import QuizBrain
from questionModel import Question
from data import questionData

questionBank = []
for question in questionData:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    questionBank.append(new_question)


quiz = QuizBrain(questionBank)

while quiz.still_has_questions():
    quiz.next_question()
