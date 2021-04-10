class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {question.text} True or False? ")
        self.check_answer(answer, question.answer)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Well done! You got it right!")
            self.score += 1
        else:
            print("Wrong answer! That's too bad :/")

        print(f"Your current score is: {self.score}/{len(self.question_list)}\n")
