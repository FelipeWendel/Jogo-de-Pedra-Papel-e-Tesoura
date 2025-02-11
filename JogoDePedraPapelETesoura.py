import random

def jogo():
    while True:
        usuario = input("Digite sua escolha (pedra, papel ou tesoura): ").lower()
        while usuario not in ["pedra", "papel", "tesoura"]:
            usuario = input("Escolha inválida. Digite sua escolha (pedra, papel ou tesoura): ").lower()

        computador = random.choice(["pedra", "papel", "tesoura"])

        print(f"\nVocê escolheu {usuario}, o computador escolheu {computador}.\n")

        if usuario == computador:
            print(f"Empate!")
        elif usuario == "pedra":
            if computador == "tesoura":
                print("Pedra esmaga tesoura! Você venceu!")
            else:
                print("Papel cobre pedra! Você perdeu!")
        elif usuario == "papel":
            if computador == "pedra":
                print("Papel cobre pedra! Você venceu!")
            else:
                print("Tesoura corta papel! Você perdeu!")
        elif usuario == "tesoura":
            if computador == "papel":
                print("Tesoura corta papel! Você venceu!")
            else:
                print("Pedra esmaga tesoura! Você perdeu!")

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        while jogar_novamente not in ["s", "n"]:
            jogar_novamente = input("Escolha inválida. Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente == "n":
            break

jogo()