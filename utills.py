from alunos import Aluno

##Transformar em String.
def transformar_str(obj) -> str:
    """Esta função recebe um objeto, e retorna os mesmos itens como uma única string."""
    response = f'{obj.indice}, {obj.nome},{obj.nascimento},{obj.faixa}'
    return response

#Transformar em Objeto.
def transformar_obj(str):
    """Recebe uma string, e retorna a mesma como um objeto."""
    response = Aluno(str)
    return response

#Criar aluno.
def criar_aluno():
    nome = input('Insira o nome: ')
    nascimento = input('Insira o ano de nascimento: ')
    faixa = input('Insira a faixa: ')
    aluno = Aluno(nome, nascimento, faixa)
    return aluno

#Adicionar ao arquivo.
def adicionar_aluno(aluno):
    with open('perfis.txt', 'a') as arquivo:
        for key in range(0,3), aluno:
            arquivo.write(str(key))

#Ler perfis.
def ler_todos():
    with open('perfis.txt', 'r') as arquivo:
        for item in arquivo:
            print(item)

def atualizar_perfil(index_perfil):
    """Recebe o index do perfil a ser atualizado."""