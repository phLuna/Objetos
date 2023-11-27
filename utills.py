from alunos import Aluno

#Criar aluno.
def criar_aluno(nome, nascimento, faixa):
    aluno = Aluno(nome, nascimento, faixa)
    return aluno