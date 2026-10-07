import random

nome = input('Digite seu nome: ')
quem = ['meu cachorro', 'meu gato', 'o wi-fi', 'meu primo', 'meu professor de matematica']
acao = ['comeu', 'apagou', 'escondeu', 'hackeou', 'derrubou café', 'instalou arch linux no']
alvo = ['meu caderno', ' meu notebook', 'minha tarefa', 'meu pen drive']

sorteio_quem = random.choice(quem)
sorteio_acao = random.choice(acao)
sorteio_alvo = random.choice(alvo)

print(f'Professor, desculpa! {sorteio_quem.capitalize()} {sorteio_acao} {sorteio_alvo}.')
print(f'Assinado: {nome}')