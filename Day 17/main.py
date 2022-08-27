from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    questions.append(new_question)

# print(questions[0].answer)

quiz = QuizBrain(questions)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the quiz\nYour final score was: {quiz.score}/{quiz.question_number}")
