from question_model import Question
from question_data import questions
from quiz_brain import QuizBrain


question_bank =[]
for question in questions:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions:
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")