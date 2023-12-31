import random
def deal_card():
    cards = [2,3,4,5,6,7,8,9,10,11,10,10,10]
    player1 =random.choice(cards)
    return player1
user_cards = []
comp_cards = []
for _ in range(2):
    user_cards.append(deal_card())
    comp_cards.append(deal_card)

def blackjack():
    money = input("Place the money from the stash")
    o = input("Do you want more cards")
    x=sum(user_cards)
    y=sum(comp_cards)
    win = False
    if x > 21:
        print(f"You lose the betted money {money}")
    elif y > 21:
        print(f"You won {money}")
    if x or y <=21:
        while  win:
            if o == "y":
                user_cards.append(deal_card())
                comp_cards.append(deal_card())
         
            
        else:
            s= 21-x
            j= 21-y

        


    

print(blackjack())