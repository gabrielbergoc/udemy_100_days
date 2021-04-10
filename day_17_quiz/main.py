import requests
import json
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ascii_art import ascii_art

def main():

    response = requests.get("https://opentdb.com/api.php?amount=50&type=boolean")
    openTriviaDB = json.loads(response.text)

    print("\n", ascii_art, "\nWelcome to The Quiz!")

    num_questions = int(input("How many questions do you want? (0-50) "))

    question_bank = [Question(openTriviaDB["results"][i]["question"], openTriviaDB["results"][i]["correct_answer"]) for i in range(num_questions)]
    quiz = QuizBrain(question_bank)

    print()

    while quiz.still_has_questions():
        quiz.next_question()

    print(f"You've completed the quiz!\n Your final score was {quiz.score}/{len(question_bank)}")

    option = input("Do you want to play again? y/n ")

    if option == 'y':
        main()
    else:
        exit()

if __name__ == "__main__":
    main()