import random

print('Bem vindo ao jogo de adivinhar o número.')
print('\nEu estou pensando em um número de 1 a 100...')
print("\nEscolha a sua dificuldade: Difícil(d) ou Fácil(f)")
dificuldade = input()
segredo = random.randint(1, 100)

if dificuldade == 'd':
    x = 5
    while (x > 0 ):
        print(f'Você possui {x} tentativas para acertar o número.')
        fill = int(input("Digite o número:"))
        x -= 1
        if fill < segredo:
            print('\nO número é maior! Escolha novamente.')
        elif fill > segredo:
            print('\nO número é menor! Escolha novamente!')
        else:
            print('\nParabens, você acertou o número!')
            break
        if x == 0:
            print('\nAcabou as tentativas! Você é burro.\n O número correto é:', segredo)
if dificuldade == 'f':
    x = 10
    while (x > 0):
        print(f'Você possui {x} tentativas para acertar o número.')
        fill = int(input("Digite o número: "))
        x -= 1
        if fill < segredo:
            print('\nO número é maior! Escolha novamente.')
            x -= 1
        elif fill > segredo:
            print('\nO número é menor! Escolha novamente!')
            x -= 1
            print(x)
        else:
            print('\nParabens, você acertou o número!')
            break
        if x == 0:
            print('\nAcabou as tentativas! Você é burro.\n O número correto é:', segredo)
        



