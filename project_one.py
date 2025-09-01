
import random 


def roll(): 
    min_value = 1
    max_value = 6
    return  random.randint(min_value, max_value)





while True: 
    player = input("Enter the number of player (1-4): ") 

    if player.isdigit(): 
        player = int(player)
        if 2 <=  player <= 4: 
            break 
        else: 
            print("number must be bet ween 2 and 4")
    else:
        print("INVALID NUMBER!")

Max_score = 50 
playerScore = [0 for _ in range(player)] 



while max(playerScore) < Max_score: 

    for player_idx in range(player): 
        current_score = 0
        print(f"\n player number {player_idx + 1}, turn just started \n") 
        while True:
            should_roll = input("Would you like to roll? ('y')")

            if should_roll.lower() != "y": 
                break 
            value = roll()
            if value == 1: 
                print(f"you role {value}  trun done") 
                current_score = 0
                break 
            else: 
                current_score += value 
                print(f"you role {value}") 
                break
        print(f"your score is {current_score}") 

    playerScore[player_idx] += current_score 
    print(f"Your total score is, {playerScore[player_idx]}")


