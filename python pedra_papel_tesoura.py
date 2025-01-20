import random

def pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]

    while True:
        computador = random.choice(opcoes)
        jogador = input("Escolha pedra, papel ou tesoura: ").lower()

        if jogador not in opcoes:
            print("Entrada inválida. Por favor, escolha entre pedra, papel ou tesoura.")
            continue

        if jogador == computador:
            print(f"Empate! Ambos escolheram {jogador}.")
        elif (jogador == "pedra" and computador == "tesoura") or \
             (jogador == "papel" and computador == "pedra") or \
             (jogador == "tesoura" and computador == "papel"):
            print(f"Você ganhou! {jogador} vence {computador}.")
        else:
            print(f"Você perdeu! {computador} vence {jogador}.")

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            break

pedra_papel_tesoura()