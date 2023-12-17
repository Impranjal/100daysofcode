import random
word_list = ["baboon","hero","wild"]
word = random.choice(word_list)
correct_word = []
for i in range(len(word)):
    correct_word += "-"
end_of_game =False
lives = 0
while end_of_game ==False:
    guess = input("Guess the word -> ").lower()
    for i in range(len(word)):
       if guess == word[i]:
            correct_word[i] = guess
            print(correct_word[i])
    print(correct_word)    
    if guess not in word:
        lives = lives+1
        if lives == 6:
            end_of_game =True
            print("You lose")
    if "-" not in correct_word:
        end_of_game =True
        print("You win")




    

