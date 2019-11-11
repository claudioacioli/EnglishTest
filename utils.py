from data import TYPE_COMPLETE


def get_correct_answer(type_of_question, question, answer):
    if type_of_question == TYPE_COMPLETE:
        if len(answer) > 0:
            return question.replace(" ___" if answer[0] == "'" else "___", answer)
        else:
            return question.replace("___", answer)
    else:
        return answer


def correct_it(type_of_question, question, your_answer, answers):
    is_correct = False
    if isinstance(answers, list):
        for answer in answers:
            correct_answer = get_correct_answer(type_of_question, question, answer)
            if your_answer == correct_answer:
                is_correct = True
                break
    else:
        is_correct = your_answer == answers

    return is_correct


def rewrite(your_answer, answer):
    return your_answer == answer


def welcome():
    print("Welcome to the Book 1! When you want, press exit to finish this game.")
    print()


def game_over(questions, points):
    print("You make %s of %s" % (str(points), str(questions)))


def right():
    print("Congrats, you win.")
    print()


def get_tip(tip):
    if len(tip):
        print('tip: "%s"' % tip)


def wrong(t, question, answers):
    print("You lose...")
    if isinstance(answers, list):
        print("The correct answers are:")
        for answer in answers:
            print("[%s]" % get_correct_answer(t, question, answer))
    else:
        print("The correct answer is:")
        print("[%s]" % get_correct_answer(t, question, answers))
    print()
