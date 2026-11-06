'''The rules

Rock beats scissors
Scissors beats paper
Paper beats rock
Same choice = tie'''

# i need to undertsand in games involving a computer, the only outcome user aniticipates is them winning, so conditions shld be made only on them winning, cause rest of the moves would make them loose.

import random
conditions = ['rock', 'paper', 'scissors']

# comp = random.choice(conditions)
# the computer picks once and keeps the same choice every round. If it picked “rock”, you can just keep trying until you hit “paper” and win. That’s not really a game.
count = 0
while True:
    
    comp = random.choice(conditions)
    human = input("Enter : ").lower()
    
    if human not in conditions :
        print("Not a valid condition")
        continue
        '''With continue:

Invalid input: print message → continue jumps straight back to the top of the loop. Nothing below runs.
Valid input: the if is false, so it skips that block and keeps going down. Now count += 1 runs only for valid input, written once instead of three times.
        '''
    count += 1  
    if comp == human :
        print("It's a tie!!")
        
    elif (human == 'rock' and comp == 'scissors') or (human == 'scissors' and comp == 'paper') or (human == 'paper' and comp == 'rock'):
        print(f"Hurray! You win in {count} attempts")
        break
    
    else :
        print("Nope! Go for it again")