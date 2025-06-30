from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import Quiz_UI
import html

question_bank = []
for question in question_data:
    question_text = html.unescape(question["question"])
    question_answer = html.unescape(question["correct_answer"])
    print(question_answer)
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.start_quiz()
quiz_ui = Quiz_UI(quiz)


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
