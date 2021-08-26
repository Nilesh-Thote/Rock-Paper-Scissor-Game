import random
print("Lets play Rock-Paper-Scissor")
option=["rock","paper","scissor"]
win=0
lose=0
draw=0
while True:
    answer=input("Enter Rock/Paper/Scissor or Q to Quit: ").lower()
    if answer.isalpha:
        if answer=="q":
            print("Thankyou for playing")
            break
        elif answer not in option:
            print("You can only enter Rock/Paper/Scissor or Q to Quit")
            break
    random.shuffle(option)
    computer_option=option[0]
    print("Computer choose: ", computer_option)
    if computer_option=="rock" and answer=="paper":
        print("You Won")
        win+=1
    elif computer_option=="paper" and answer=="scissor":
        print("You Won")
        win+=1
    elif computer_option=="scissor" and answer=="rock":
        print("You Won")
        win+=1
    elif computer_option==answer:
        print("It's a draw")
        draw=0
    else:
        print("You Lose")
        lose+=1
print("Your total wins "+str(win)+"\nYour total losses: "+str(lose)+"\nTotal no of draws: "+str(draw))