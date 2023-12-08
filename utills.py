from alunos import Aluno

##Transformar em String.
def transformar_str(obj) -> str:
    """Esta função recebe um objeto, e retorna os mesmos itens como uma única string."""
    response = f'{obj.indice}, {obj.nome},{obj.nascimento},{obj.faixa}'
    return response

#Transformar em Objeto.
def transformar_obj(str):
    """Recebe uma string, e retorna a mesma como um objeto."""
    response = Aluno(str[1], str[2], str[3], str[4],)
    return response

##ARRUMAR.
#Criar aluno.
def criar_aluno():
    with open('perfis.txt', 'r') as arquivo:
        perfis = []
        textao = arquivo.read()
        str(textao)
        textao1 = arquivo.split('\n')
        for i in textao1:
            perfis.append(i)
        arquivo.close()
    indice = perfis[-1][0]
    nome = input('Insira o nome: ')
    nascimento = input('Insira o ano de nascimento: ')
    faixa = input('Insira a faixa: ')
    aluno = Aluno(indice, nome, nascimento, faixa)
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

    #Esta parte abre o arquivo, extrai o texto e seleciona o perfil.
    with open('perfis.txt', 'r') as arquivo:
        textao = arquivo.read()
        textao1 = textao.split('\n')
        a = transformar_obj(textao1[index_perfil])
        arquivo.close()

    #Esta parte atualiza o objeto.
    update = input('O que deseja alterar? [Nome] [Nascimento] [Faixa] ').upper()
    if update == 'NOME':
        a.nome = input('Insira o novo nome: ')
    elif update == 'Nascimento':
        a.nascimento = input('Insira a nova data de nascimento: ')
    elif update == 'Faixa':
        a.subir_faixa()
        print('Faixa atualizada!')
    b = transformar_str(a)

    ##ARRUMAR.
    #Esta parte junta ambos.
    textao1[index_perfil].replace(b)

    #Esta parte importa o arquivo.
    with open('perfis.txt', 'w'):
        arquivo.write(textao1)
        print('Sucesso!')