
cont = 0
informacoes = ()
printe('\033[1;34m***Cadastro de alunos da Ultima School***\n')

while (cont < 2):
    nome = input('Digite o seu nome: ')
    informacao.append(cont)
    cont+=1

print("\033[1;35m\n\n**Você conseguiu finalizar o desafio**\n")

for nome in informacoes:
    print(f'Parabens {nome}')
