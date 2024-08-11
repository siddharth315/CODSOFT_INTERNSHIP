# TASK-3) ROCK-PAPER-SCISSORS GAME --->
import random

def game(user,system):
    if user==system:
        return "Tie!"
    elif user=='rock' and system=='scissors':
        return "You won!"
    elif user=='paper' and system=='rock':
        return "You won!"
    elif user=='scissors' and system=='paper':
        return "You won!"
    else:
        return "You lose!"

def main():
    user_score=0
    system_score=0
    
    while True:
        print("Welcome to the Rock-Paper-Scissors Game!")
        user=input("Choose your weapon(Rock/Paper/Scissors): ").lower()
    
        if user not in ['rock','paper','scissors']:
            print("Invalid Choice!")
            continue
    
        system=random.choice(['rock','paper','scissors'])
    
        print("You chose:",user)
        print("Computer chose:",system)
    
        result=game(user,system)
        print(result)
    
        if 'won' in result:
            user_score+=1
        elif 'lose' in result:
            system_score+=1
    
        print(f"SCOREBOARD => You:{user_score}, Computer:{system_score}")
    
        play_again=input("Do you want to play another round? (yes/no): ").lower()
        if play_again=='yes':
            main()
        else:
            print("Thank you for playing!")
            break
main()
