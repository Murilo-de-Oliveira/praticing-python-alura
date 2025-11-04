import random

def verify_result(player_choice: str, machine_choice: str) -> str:
    if player_choice == machine_choice:
        return "Empate!"
    
    # item escolhido: de quem ganha
    interactions = {
        "pedra": "tesoura",
        "papel": "pedra",
        "tesoura": "papel"
    }
    
    if interactions.get(player_choice) == machine_choice:
        return "Você venceu!"
    
    return "Você perdeu!"

options = ["pedra", "papel", "tesoura"]    

while True:
    player_choice = input("Escolha: pedra, papel ou tesoura? ")
    
    if player_choice.lower() not in options:
        print("Escolha uma opção válida!")
    else:
        break

machine_choice = random.choice(options)
print(f"Computador escolheu: {machine_choice}")
result = verify_result(player_choice, machine_choice)
print(result)
