# nome = input('Digite seu nome: ')
# curso = input('Digite seu curso: ')
# print(f'Meu nome é {nome} e estou cursando {curso}.')
# -------------------------------------------------------
# n1 = int(input('Digite o primeiro numero: '))
# n2 = int(input('Digite o segundo numero: '))
# soma = n1 + n2
# subtracao = n1 - n2
# multiplicacao = n1 * n2
# divisao = n1 / n2
# exponenciacao = n1 ** n2
# resto = n1 % n2
# divisao_inteira = n1 // n2
# print(f'A soma é: {soma}')
# print(f'A subtração é: {subtracao}')
# print(f'A multiplicação é: {multiplicacao}')
# print(f'A divisão é: {divisao}')
# print(f'A exponenciação é: {exponenciacao}')
# print(f'O resto da divisão é: {resto}')
# print(f'A divisão inteira é: {divisao_inteira}')
# -------------------------------------------------------
# numerosecreto = 46
# chute = int(input('Digite um número entre 1 e 100: '))
# if chute == numerosecreto:
#          chute = int(input('Digite um número entre 1 e 100: '))
#          print('Parabéns! Você acertou o número secreto!')
         
# else:
#         print('Errou')
# --------------------------------------------------------
numerosecreto = 46
tentativas = 5

while tentativas > 0:
    chute = int(input(f'Digite um número entre 1 e 100 (Tentativas restantes: {tentativas}): '))
    
    if chute == numerosecreto:
        print('Parabéns! Você acertou o número secreto!')
        break
    elif chute < numerosecreto:
        print('O número secreto é maior. Tente novamente!')
    else:
        print('O número secreto é menor. Tente novamente!')
        
    tentativas -= 1

if tentativas == 0:
    print(f'\nVocê perdeu! O número secreto era: {numerosecreto} ')
