import random

'''
Objetivo: O computador escolhe um número secreto entre 1 e 100. O jogador tem 5 tentativas para adivinhar. Após cada tentativa, o jogo deve indicar se o palpite foi muito alto, muito baixo ou correto.
'''

def main():
    numero_secreto = gerar_numero_secreto()
    numero_usuario = recebe_numero_usuario()
    verificar_adivinhacao(numero_secreto,numero_usuario)

def gerar_numero_secreto():
    numero_secreto = random.randint(1,100)
    return numero_secreto

def recebe_numero_usuario():
    try:
        numero_usuario = int(input("Adivinhe o número: "))
        return numero_usuario
    except ValueError:
        print("Você digitou algo errado.")

def verificar_adivinhacao(numero_secreto,numero_usuario):
    if numero_usuario > numero_secreto:
        print("O número foi mais alto que o número secreto")
        return False
    elif numero_usuario < numero_secreto:
        print("O número foi a baixo do número secreto")
        return False
    elif numero_usuario == numero_secreto:
        print("Você acertou o número secreto")
        return True

def tentativas():
    ...

main()