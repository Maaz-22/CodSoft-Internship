# Task 5
import random

# Cricket quiz questions and answers
cricket_questions = [
    {
        "question": "Who is known as the 'Little Master' in cricket?",
        "choices": ["A) Sachin Tendulkar", "B) Virat Kohli", "C) Ricky Ponting", "D) Brian Lara"],
        "correct_answer": "A) Sachin Tendulkar"
    },
    {
        "question": "Which country has won the most ICC Cricket World Cups?",
        "choices": ["A) Australia", "B) India", "C) England", "D) West Indies"],
        "correct_answer": "A) Australia"
    },
    {
        "question": "How many players are there in a standard cricket team?",
        "choices": ["A) 10", "B) 11", "C) 12", "D) 9"],
        "correct_answer": "B) 11"
    },
    {
        "question": "What is the highest individual score by a batsman in a Test match?",
        "choices": ["A) 375", "B) 400", "C) 501", "D) 294"],
        "correct_answer": "B) 400"
    },
    {
        "question": "Who is the highest run-scorer in the history of One Day Internationals (ODIs)?",
        "choices": ["A) Virat Kohli", "B) Ricky Ponting", "C) Sachin Tendulkar", "D) Kumar Sangakkara"],
        "correct_answer": "C) Sachin Tendulkar"
    },
    {
        "question": "Which cricketer is known as the 'Sultan of Swing'?",
        "choices": ["A) Dale Steyn", "B) Brett Lee", "C) Wasim Akram", "D) James Anderson"],
        "correct_answer": "C) Wasim Akram"
    },
    {
        "question": "In cricket, what does LBW stand for?",
        "choices": ["A) Leg Before Wicket", "B) Long Ball Wicket", "C) Leg Ball Wicket", "D) Leg Behind Wicket"],
        "correct_answer": "A) Leg Before Wicket"
    },
    {
        "question": "Which cricket format is also known as 'T20'?",
        "choices": ["A) Test cricket", "B) One Day Internationals (ODIs)", "C) Twenty20", "D) T10"],
        "correct_answer": "C) Twenty20"
    },
    {
        "question": "Who was the first bowler to take 10 wickets in a Test match innings?",
        "choices": ["A) Jim Laker", "B) Shane Warne", "C) Muttiah Muralitharan", "D) Anil Kumble"],
        "correct_answer": "A) Jim Laker"
    },
    {
        "question": "Which country hosted the first-ever Cricket World Cup in 1975?",
        "choices": ["A) India", "B) England", "C) Australia", "D) West Indies"],
        "correct_answer": "B) England"
    }
]


def run_cricket_quiz():
    score = 0
    total_questions = len(cricket_questions)

    print("Welcome to the Quiz Game!")
    print("Game Rules:")
    print("You will be presented with {} multiple-choice questions regrading cricket.".format(total_questions))
    print("Choose the correct option by typing the corresponding letter (e.g., 'A').\n")

    random.shuffle(cricket_questions)

    for i, question_data in enumerate(cricket_questions, 1):
        print("Question {}: {}".format(i, question_data["question"]))
        for choice in question_data["choices"]:
            print(choice)

        user_answer = input("Your answer: ").strip().upper()
        correct_answer = question_data["correct_answer"].split(")")[0].strip()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect. The correct answer is: {}\n".format(question_data["correct_answer"]))

    print("Quiz completed!")
    print("Your score: {}/{}".format(score, total_questions))

    if score == total_questions:
        print("Congratulations! You got a perfect score!")
    elif score >= total_questions * 0.7:
        print("Great job! You performed well.")
    else:
        print("You can do better. Keep practicing!")

    play_again = input("Would you like to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        run_cricket_quiz()
    else:
        print("Thank you for playing!")


if __name__ == "__main__":
    run_cricket_quiz()
