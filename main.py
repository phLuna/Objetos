from utills import criar_aluno, adicionar_aluno, ler_todos, atualizar_perfil()

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
        print('-' * 15)
        aluno = criar_aluno()
        adicionar_aluno(aluno)
        print("""'Aluno adionado!'
              " * 15""")
    #[2] Ler.
    if operar == '2':
        print('-' * 15)
        ler_todos()
        print('-' * 15)
    #[3] Atualizar.
    if operar == '3':
        print('-' * 15)
        atualizar_perfil()
        print('-' * 15)