def quiz_game(questions):
    score = 0
    for q, options, ans in questions:
        print(f"\n{q}")
        for i, opt in enumerate(options):
            print(f"{i+1}. {opt}")
        if input("Your answer in (number): ") == str(options.index(ans) + 1):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct was: {ans}")
    print(f"\nQuiz Over! You got {score}/{len(questions)} correct answers.")
    

# Define your questions: (question, [options], correct_answer)
questions = [
    ("Who wrote Romeo and Juliet?", ["William Wordsworth","Charles Dickens","William Shakespeare","Jane Austen"],"William Shakespeare"),
    ("What is the chemical symbol for gold?",[ "Gd","Au","Ag","Go"],"Au"),
    ("Which ocean is the largest?", ["Atlantic", "Indian", "Arctic","Pacific"], "Pacific"),
    ("In which year did the Titanic sink?",["1912","1920","1905","1915"],"1912"),
    ("What is the hardest natural substance on Earth?",["Gold","Iron","Diamond","Quartz"],"Diamond"),
    ("Which gas do plants absorb from the atmosphere?",["Oxygen","Hydrogen","Carbon dioxide","Nitrogen"],"Carbon dioxide"),
    ("What is the smallest prime number?",["0","1","2","3"],"2"),
    ("Who discovered penicillin?",["Isaac Newton","Albert Einstein","Alexander Fleming","Louis Pasteur"],"Alexander Fleming"),
    ("Which country is home to the kangaroo?",["India","South Africa","Australia","Brazil"],"Australia"),
    ("What is the boiling point of water at sea level in Celsius?",["90°C","100°C","110°C","120°C"],"100°C")

    
 ]

quiz_game(questions)