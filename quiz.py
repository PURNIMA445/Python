print("Welcome to the quiz panel!!")
count = 0

# Infinite loop for quiz interaction
while True:
    question = input("In which topic are you interested?\nHistory\nTech\n(Type 'exit' to quit)\n")
    
    # Exit condition for the loop
    if question.lower() == "exit":
        print("Thank you for visiting the quiz panel. Byeee! 👋")
        break
    
    # History quiz section
    elif question == "History":
        # Dictionary for storing history questions and answers
        quiz = {
            'quest': [
                "Who was the first prime minister of Nepal?",
                "Who was the first king of unified Nepal?",
                "Who was the last king of Nepal?",
                "Who founded the Pashupatinath temple in Kathmandu?",
                "Who built the Swayambhunath stupa in Kathmandu?"
            ],
            'answer': [
                "Bhimsen Thapa",
                "Prithvi Narayan Shah",
                "Gyanendra Bir Bikram Shah",
                "Jayasthiti Malla",
                "Jaya Prakash Malla"
            ]
        }
        
        # Loop through questions and answers using zip
        for q, a in zip(quiz["quest"], quiz["answer"]):
            print(f"\n{q}")  # Display question
            ans = input()  # Get user answer
            # Check if the user's answer is correct (case-insensitive)
            if ans.lower() == a.lower():
                print("Congratulationsssss!!!! 🎉")
                count += 1  # Increment score for correct answer
            else:
                print(f"The correct answer is {a}")
        # Display total score after History quiz
        print(f"You got {count} points out of 5.")
    
    # Tech quiz section
    elif question == "Tech":
        # Dictionary for storing tech questions and answers
        quiz_tech = {
            'quest': [
                "Who invented the first computer?",
                "What does CPU stand for?",
                "Which language is mainly used for web development?",
                "What is the full form of HTML?",
                "What is the main function of an operating system?"
            ],
            'answer': [
                "Charles Babbage",
                "Central Processing Unit",
                "JavaScript",
                "HyperText Markup Language",
                "Manage hardware and software resources"
            ]
        }
        
        # Loop through questions and answers using zip
        for q, a in zip(quiz_tech["quest"], quiz_tech["answer"]):
            print(f"\n{q}")  # Display question
            ans = input()  # Get user answer
            # Check if the user's answer is correct (case-insensitive)
            if ans.lower() == a.lower():
                print("Congratulationsssss!!!! 🎉")
                count += 1  # Increment score for correct answer
            else:
                print(f"The correct answer is {a}")
        # Display total score after Tech quiz
        print(f"You got {count} points out of 5.")
    
    # Handle invalid input (if user enters neither 'History' nor 'Tech')
    else:
        print("Sorry, we only have 'History' and 'Tech' quizzes for now! 😅")
