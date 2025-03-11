###  Quiz Game (Control Flow)

def quiz_game():
    score = 0
    questions = {"What is 2+2?": "4", "What is the capital of France?": "Paris"}
    for q, a in questions.items():
        ans = input(q + " ")
        if ans.lower() == a.lower():
            score += 1
    print(f"Your score: {score}/{len(questions)}")

quiz_game()