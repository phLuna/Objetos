from utills import criar_aluno

espaco_de_menu1 = '=' * 15
espaco_de_menu2 = '=-=' * 10

#Menu.
print(f'''{espaco_de_menu2}
Bem-vindo(a) ao sistema da Python Gym Upgrade!
O que pretende fazer por agora?''')
while True:
    operar = input('''[1] - Criar,
[2] - Ler.
[3] - Atualizar.
[4] - Excluir.
[0] - Sair.

F: ''').upper()
    while operar not in '01234':
        operar = input('Erro! Tente novamente: ')
    #[1] Criar.
    if operar == '1':
        nome = input('Insira o nome: ')
        nascimento = input('Insira o ano de nascimento: ')
        faixa = input('Insira a faixa: ')
        aluno = criar_aluno(nome, nascimento, faixa)