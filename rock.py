import random
#intro
print("\033[1;36m----------------------------------------------------------\033[0m")
print("\033[1;32m# \033[1;34mWelcome Players To \033[1;33mRock,\033[1;31mScissors,\033[1;32mPaper \033[1;31m/ \033[1;34m(\033[1;33mo,\033[1;31m-<,\033[1;32m|=|)    #\033[0m")
print("\033[1;36m----------------------------------------------------------\033[0m")
print("\033[1;32m| \033[1;33mR0CK        \033[1;34m|        \033[1;31m$C1$$0R$        \033[1;34m|        \033[1;32mP@P3R    \033[1;32m|\033[0m")
print("\033[1;36m----------------------------------------------------------\033[0m")
print("\033[1;33m|~~~~~~|\033[1;34m      |                        |    \033[1;32m|===========| \033[1;32m")
print("\033[1;33m|oooooo|\033[1;34m      |     \033[1;31m--------->>>>>>\033[1;34m    |    \033[1;32m|===========| \033[1;32m")
print("\033[1;33m|oooooo|\033[1;34m      |                        |    \033[1;32m|===========| \033[1;32m")
print("\033[1;33m|______|\033[1;34m      |                        |    \033[1;32m|===========| \033[1;32m")
print("\033[1;36m----------------------------------------------------------\033[0m")
#choose your class
def main_gate():
    a = input("Enter your class:(\033[1;33mRock,\033[1;31mScissors,\033[1;32mPaper,\033[1;35mShuffle\033[0m)\n").lower()
    if "rock" in a:
        print("The Player choose:\n\033[1;33mR0CK = o\033[0m")
    elif "scissors" in a:
        print("The Player choose:\n\033[1;31m$C1$$0R$ = -<\033[0m")
    elif "paper" in a:
        print("The Player choose:\n\033[1;32mP@P3R = |=|\033[0m")
    else:
        print("The Player choose:\n\033[1;35mshuffle\033[0m")
        choices = ['rock', 'paper', 'scissors']
        a = random.choice(choices)
    return a
#choose your player
def load_game():
    print("Press(1) To Start game with \033[1;34mThe Computer\033[0m")
    print("Press(2) To Start game with \033[1;35mAnother Player\033[0m")
    b = int(input("\n"))
    if b == 1:
        print("You choose to play with \033[1;34mThe Computer\033[0m")
        choices = ['rock', 'paper', 'scissors']
        c = random.choice(choices)
        if c == "rock":
            print("\033[1;34mThe Computer\033[0m choose:\n\033[1;33mR0CK = o\033[0m")
        elif c == "paper":
            print("\033[1;34mThe Computer\033[0m choose:\n\033[1;32mP@P3R = |=|\033[0m")
        elif c == "scissors":
            print("\033[1;34mThe Computer\033[0m choose:\n\033[1;31m$C1$$0R$ = -<\033[0m")
        else:
            print("Erorr")
    else:
        print("You choose to play with \033[1;35mSecond Player\033[0m")
        c = main_gate()
    return c, b


#The result of the game
def start_game(a,c,b,f,you,computer,second,tie):
     if a == c:
        print(f"The {f} Round is a \033[1;31mTie\033[0m")
        tie += 1
     elif a != c:
         if a == "paper" and c == "rock":
             print(f"\033[1;32mFirst Player\033[0m Won The {f} Round")
             you += 1
         elif a == "rock" and c == "scissors":
             print(f"\033[1;32mFirst Player\033[0m Won The {f} Round")
             you += 1
         elif a == "scissors" and c == "paper":
             print(f"\033[1;32mFirst Player\033[0m Won The {f} Round")
             you += 1
         else:
             if b == 1:
               print(f"\033[1;34mThe Computer\033[0m Won The {f} Round")
               computer += 1
             else:
                 print(f"\033[1;35mSecond Player\033[0m Won This Round({f})")
                 second += 1
     return f,you,computer,second,tie
you = 0
computer = 0
second = 0
tie = 0
f = 1
#loop for the game
while True:
    a = main_gate()
    c, b = load_game()
    f,you,computer,second,tie = start_game(a, c, b, f,you,computer,second,tie)
    play_again = input("Do you want to play again? (\033[1;32myes\033[0m/\033[1;31mno\033[0m):\n ").lower()
    if play_again == 'yes':
        f += 1
    if play_again != 'yes':
     print("\033[1;33mThanks for playing!\033[0m\n")
     break
#The sum of the wins
print(f"\033[1;32mFirst Player\033[0m Won {you} Rounds")
print(f"\033[1;34mThe Computer\033[0m Won {computer} Rounds")
print(f"\033[1;35mSecond Player\033[0m Won {second} Rounds")
print(f"\033[1;31mThere was Tie\033[0m {tie} Rounds\n")
if you > computer and you > second:
    print("\033[1;33m$The Winner of the game is \033[1;32mFirst Player$\033[0m\n \033[1;33m$Congratulations$ \033[0m")
elif computer > you and computer > second:
    print("\033[1;33m$The Winner of the game is \033[1;34mThe Computer$\033[0m\n \033[1;33m$Congratulations$ \033[0m")
elif second > you and second > computer:
    print("\033[1;33m$The Winner of the game is \033[1;35mSecond Player$\033[0m\n \033[1;33m$Congratulations$ \033[0m")
else:
    print("\033[1;31m!The game is a tie between the players!\033[0m")