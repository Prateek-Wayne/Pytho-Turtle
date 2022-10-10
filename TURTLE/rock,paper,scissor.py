import random
def Play():
    user=input("what's your choice ??/n 'r' for rock; 'p' for paper ; 's' for scissor :->")
    computer=random.choice(['r','p','s'])
    if user==computer:
        return "It's a Tie"
    elif is_won(user,computer):
        return "you won!!!"

    return "you lost-_-"
def is_won(player,AI):
    if (player=='r' and AI=='s')or(player=='p' and AI=='r')or(player=='s' and AI=='p'):
        return True
        # r>s,p>r,s>p
        # return true if user won

# print(Play())