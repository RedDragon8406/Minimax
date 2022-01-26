import random
from colorama import Fore
choices = ["rock","paper","scissors"]

done = False

while not done:
    n = input(Fore.CYAN+"r,p,c?: ")
    computer_n = random.choice(choices)
    if n == 'r':
        if computer_n == "rock":
            print(Fore.GREEN+"rock, Tie!")
        elif computer_n == "paper":
            print(Fore.GREEN+"haha paper you lose!")
        else:
            print(Fore.GREEN+"scissors.. lucky boy")
    elif n == 'p':
        if computer_n == "paper":
            print(Fore.GREEN+"paper, Tie!")
        elif computer_n == "scissors":
            print(Fore.GREEN+"haha scissors you lose!")
        else:
            print(Fore.GREEN+"rock.. lucky boy")
    elif n == 'c':
        if computer_n == "scissors":
            print(Fore.GREEN+"scissors, Tie!")
        elif computer_n == "rock":
            print(Fore.GREEN+"haha rock you lose!")
        else:
            print(Fore.GREEN+"paper.. lucky boy")
    else:
        print(Fore.RED+"You're supposed to enter either r or p or c >:(")
        continue
    while not done:
        checkout = input(Fore.CYAN+"Enter yes to continue and no to exit: ")
        if checkout == "yes":
            done = True
            break
        elif checkout == "no":
            break
        else:
            print(Fore.RED+"pls import yes or no...")