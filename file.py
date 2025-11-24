import random

def sps():
    list =  ["stone", "paper", "scissors"] 

    system_choice =  random.choice(list)
    print(list)
    player_input =input("It's your turn make your choice from above : ").lower()

    if player_input not in list:
        print("invalid input try from above")
        return
        
    if system_choice == player_input :
        print(f"OHH its draw, you and computer both were thinking of, {player_input}")
        return

    if system_choice == "stone":
        if player_input == "paper":
            print("Woahh what a luck you won!!")
            print("computer choosed stone ")
        elif player_input == "scissors":
            print("oopss!!, Computer took game")
            print("computer choosed stone")

    elif system_choice == "paper":
        if player_input == "stone" :
            print("oopss!!, Computer took game")
            print("computer choosed paper")

        elif player_input == "scissors":
            print("Woahh what a luck you won!!")
            print("computer choosed paper ")

    elif system_choice == "scissors" :
        if player_input == "stone":
            print("Woahh what a luck you won!!")
            print("computer choosed scissors ")

        elif player_input == "paper":
            print("oopss!!, Computer took game")
            print("computer choosed scissors")
sps()