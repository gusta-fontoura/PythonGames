from game_data import data
import random


def format_data(account):
    accountName = account["name"]
    accountDescription = account["description"]
    accountCountry = account["country"]
    return f"{accountName}, a {accountDescription}, From {accountCountry}"


def check_awnser(guess, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"


score = 0
game_should_continue = True
account_b = random.choice(data)

print("Bem-vindo ao jogo 'Quem é o maior!'")

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print("\nQuem tem mais seguidores.\n ")

    print(f"Compare A:{format_data(account_a)}")
    print(f"Compare B:{format_data(account_b)}")

    guess = input("\nQuem tem mais seguidores? Digite 'A' ou 'B'.").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_awnser(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"Você acertou! Placar é {score}!")
    else:
        game_should_continue = False
        print(f"Você errou! Placar Final foi {score}!")
