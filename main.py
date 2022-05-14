import random

def play():
    user = input(" 'r' para pedra, 'p' para papel ou 't' para tesoura\n")
    computer = random.choice(['r', 'p', 't'])

    if user == computer:
        return 'empate'

    if ganhar(user, computer):
        return 'Você Ganhou!'
    
    else:
        return 'Você Perdeu'

def ganhar(player, opponent):
    #return true se o jogador ganhar
    # r > t,  t > p,  p > r
    if (player == 'r' and opponent == 't') or (player == 't' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())