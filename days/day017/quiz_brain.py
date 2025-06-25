class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions = q_list
        self.score = 0

    def next_question(self):
        answer = input((f"Q.{self.question_number + 1}: "
                        f"{self.questions[self.question_number].text} (True/False)?: "))
        self.check_answer(answer, self.questions[self.question_number].correct_answer)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.questions)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got the question right!")
        else:
            print(f"You got the question wrong!")

        print(f"Your current score is {self.score}/{self.question_number + 1}.")
