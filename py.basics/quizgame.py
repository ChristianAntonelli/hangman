questions = (
    "Qual è la capitale dell'Australia?",
    "Quanti pianeti ci sono nel Sistema Solare?",
    "Chi ha dipinto la Gioconda?",
    "Qual è il simbolo chimico dell'oro?"
)

options = (
    ("A. Sydney", "B. Canberra", "C. Melbourne", "D. Perth"),
    ("A. 7", "B. 9", "C. 8", "D. 10"),
    ("A. Michelangelo", "B. Raffaello", "C. Caravaggio", "D. Leonardo da Vinci"),
    ("A. Ag", "B. Au", "C. Fe", "D. Or")
)

answers = ("B", "C", "D", "B")
guesses = []

print("-"*10)
print("QuizGame. Answer the questions and try to get the highest score!")
print("You will get 10 points for each correct answer. Start!")
print()

for question, option in zip(questions,options):
    print(f"- Question:\n{question}")
    print("- Options: ")
    for x in option:
        print(x)
    guess = input("Type here your guess: ").upper().strip()
    guesses.append(guess)
    print()

total = 0

right_answers = []

print("Your guesses were: ")
for guess,answer in zip(guesses,answers):
    print(guess)
    if guess == answer.upper().strip():
        total += 10
        right_answers.append(guess)

print()
print(f"You got {len(right_answers)} right answers. Your final score is {total}.")

















    

   
