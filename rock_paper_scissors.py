import random

def get_choices():
    
    options=['rock','paper','scissors']
    player_choice=input("Enter a choice(rock,paper or scissors)\n")
    computer_choice=random.choice(options)
    
    choices={'player':player_choice,'computer':computer_choice}
    return choices

def check_win(player,computer):
    print(f"You chose {player} and the computer chose {computer}\n")

    if player==computer:
        return "Its a tie!!!"
    
    elif player=='rock':
        if computer=='paper':
            return "Paper covers rock, you lose!!"
        else:
            return "Rock smashes scissors , you win!!"
        
    elif player=='paper':
        if computer=='scissors':
            return "Scissors cuts papers, you lose!!"
        else:
            return "Paper covers rock, you win!!"
    
    else:
        if computer=='paper':
            return "Scissors cuts paper, you win!!"
        else:
            return "Rock smashes scissors , you lose!!"


choices=get_choices()
result=check_win(choices['player'],choices['computer'])
print(result)

        
        




