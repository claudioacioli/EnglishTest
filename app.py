from random import randrange
from utils import correct_it, game_over, right, wrong, welcome, get_tip
import data

points = 0
asks = 0
total_types = len(data.exercises)

if __name__ == '__main__':
    welcome()
    while True:
        collection = data.exercises[randrange(total_types)]
        questions = collection["questions"]
        type_of_collection = collection["type"]
        question, answers = questions[randrange(len(questions))]

        print(question)
        get_tip(collection["tip"])
        your_answer = input()

        if your_answer == "exit":
            break

        asks += 1
        if correct_it(type_of_collection, question, your_answer, answers):
            right()
            points += 1
        else:
            wrong(type_of_collection, question, answers)

    game_over(asks, points)
