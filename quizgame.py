print("THIS GAME WAS DEVELOPED MUWANGUZI CYRUS");
print("WELCOME TO MY CYRUS' QUIZ");
name = input("enter your name ");
print("Hello " +name);
playing = input("Do you want to play? ");
if playing != ('yes'):
    print("sorry you cant continue ")
    exit()
else:
    print("okay lets play")
    import random

# List of Bible trivia questions and answers
questions = [
    {
        "question": "Who was the first man created by God?",
        "choices": ["Abraham", "Moses", "Adam", "David"],
        "answer": "Adam"
    },
    {
        "question": "Where was Jesus born?",
        "choices": ["Nazareth", "Bethlehem", "Jerusalem", "Egypt"],
        "answer": "Bethlehem"
    },
    {
        "question": "Who built the ark?",
        "choices": ["Noah", "Moses", "Abraham", "David"],
        "answer": "Noah"
    },
    {
        "question": "How many days did God take to create the world?",
        "choices": ["5", "6", "7", "8"],
        "answer": "6"
    },
    {
        "question": "Who was swallowed by a great fish?",
        "choices": ["Jonah", "Elijah", "Paul", "John"],
        "answer": "Jonah"
    }
]

def play_bible_trivia():
    score = 0

    # Randomize the question order
    random.shuffle(questions)

    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}: {q['question']}")
        choices = q['choices']
        
        # Display multiple choices
        for idx, choice in enumerate(choices, 1):
            print(f"{idx}. {choice}")
        
        # Get user's answer
        try:
            user_answer = int(input("Your choice (1-4): "))
            if choices[user_answer - 1] == q['answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {q['answer']}")
        except (ValueError, IndexError):
            print(f"Invalid input. The correct answer is: {q['answer']}")

    # Display the final score
    print(f"\nYour final score is {score}/{len(questions)}.")
if __name__ == "__main__":
    play_bible_trivia()

    
   
      
