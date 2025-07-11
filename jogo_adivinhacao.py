import random

'''
Objetivo: O computador escolhe um número secreto entre 1 e 100. O jogador tem 5 tentativas para adivinhar. Após cada tentativa, o jogo deve indicar se o palpite foi muito alto, muito baixo ou correto.
'''

def main():
    print(numero_secreto())

def numero_secreto():
    numero_secreto = random.randint(1,100)
    return numero_secreto

main()