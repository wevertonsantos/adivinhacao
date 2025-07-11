import random

def main():
    numero_secreto = gerar_numero_secreto()
    tentativas = 0
    while tentativas < 5:
        numero_usuario = recebe_numero_usuario()
        if verificar_adivinhacao(numero_secreto,numero_usuario):
            print("Você acertou o número secreto")
            break
        tentativas += 1
        if tentativas == 5:
            print(f"Esgotou as tentativas! O número secreto era: {numero_secreto}")

def gerar_numero_secreto():
    numero_secreto = random.randint(1,50)
    return numero_secreto

def recebe_numero_usuario():
    while True:
        try:
            numero_usuario = int(input("Adivinhe o número 0 a 50: "))
            return numero_usuario
        except ValueError:
            print("Você digitou algo errado.")

def verificar_adivinhacao(numero_secreto,numero_usuario):
    if numero_usuario > numero_secreto:
        print("O número foi mais alto que o número secreto")
        return False
    elif numero_usuario < numero_secreto:
        print("O número foi abaixo do número secreto")
        return False
    elif numero_usuario == numero_secreto:
        return True

main()