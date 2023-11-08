import random
random_float = random.random()
print(random_float)
love_score =random.randint(1,100)
print("your love score is ",love_score)
rand_int =random.randint(0,1)
if rand_int ==1:
    print("You have got heads")
else:
    print("You have got tails")

#Python List

first_list = ["up","bihar","mp","tn","hp"]
# print(first_list[-1])
first_list.extend(["assam","kerala"])
print(first_list)

### Code Challenge

finance_guys = ["angela","ben","jimmy","michael","chole"]
len_list = len(finance_guys)
ind = random.randint(0,len_list-1)
print(finance_guys[ind],"is going to pay bills")

d_list = [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
print("enter the column and row")
c_r = input()
c= c_r.split()
col = int(c_r[0])
row = int(c_r[1])
print(row,col)
d_list[row-1][col-1] = "x"
print(f"{d_list}")


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_list = [rock,paper,scissors]
print("enter the choices to play the game")
c = int(input())
print(f"{game_list[c]}")
get_c = random.randint(0,len(game_list)-1)




