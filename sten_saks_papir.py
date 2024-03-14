from difflib import IS_LINE_JUNK
from gc import is_finalized
import random

def play():
    user = input("(r) for rock, (p) for paper, (s) for scissors\n") 
    computer = random.choice(['r', 's', 'p'])
    print(user, computer)

    if user == computer: 
        return "`tie´"
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        return "you won!"
    
    return " you lost"
     
def is_win(player, opponent):
        # return true if player wins
    # r > s, s > p, p > r
    if (player == ("r") and opponent == ("s")) or (player == ("s") and opponent == ("p")) or (player == ("p") and opponent == ("r")):
        return True
    
#if __name__ == '__main__':
#    result = play()
#    print(result)