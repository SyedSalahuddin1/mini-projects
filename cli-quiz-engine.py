def get_questions():
    questions = [
        {
            "question": "Who is the first Prime Minister of India? ",
            "options": ["Mahatma Ghandi", "V.P Patil", "Jawaharlal Nehru"],
            "correct": 3
        },
        {
            
          "question": "Who is the current Welterweight Champion of UFC:",
          "options": ["Kumaru Usman", "JDM", "Islam"],
          "correct":3
        },
        {
            "question":"Who is considered the greatest boxer of all-time",
            "options":["Mike Tyson", "Joe Frazier", "Mohammed Ali"],
            "correct":3
        }
    ]
    
    return questions

def ask_question(question):
    
    print(question["question"])
    
    for i, options in enumerate(question["options"], 1):
        print(f"{i}, {options}")
        
    user_choice = int(input("Please select an option: "))
    
    if user_choice == question["correct"]:
        return True
    return False
 

def run_quiz():
    questions = get_questions()
    
    score = 0 
    
    for question in questions:
        if ask_question(question):
            score += 1
    
    return score


def show_result(score, total_questions):
    if score > total_questions / 2:
         expression = "Excellent"
    elif score == total_questions / 2:
        expression = "Average"
    elif score < total_questions / 2:
        expression = "Below Average"
        
    print(f"You scored {score} out of {total_questions}, That was a {expression} score!")

    
def main():
    print("=== Welcome to the Quiz Engine ===")
    
    while True:
        score = run_quiz()
        total_questions = len(get_questions())
        show_result(score, total_questions)
        
        choice = input("\nDo you want to play again? (y/n)").lower()
        
        if choice != "y":
            print("Thank You for playing!")
            break
        
if __name__ == "__main__":
    main()
    
            
