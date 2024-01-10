import random
def guess():
    guess_word = random.randint(0,100)
    difficulty = str(input("Choose between easy or hard "))
    diff_map = {"easy":10,"hard":5}
    for i in diff_map:
        if difficulty == i:
            total_attempts = diff_map[i]
            print(total_attempts)
    attempts_taken = 0
    while(attempts_taken < total_attempts):
        take_guess = int(input("Take a guess ! "))
        if take_guess == guess_word:
            return f"You won the correct word is {guess_word}"
        elif take_guess > guess_word:
            print("Too high !")
        elif take_guess < guess_word:
            print("Too low !")
        attempts_taken +=1
    return f"You ran out of your luck, the corret word was {guess_word}"
        

print(guess())
