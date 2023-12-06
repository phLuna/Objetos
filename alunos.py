from datetime import datetime

class Aluno:
    def __init__(self, nome, nascimento, faixa) -> None:
        self.nome = nome
        self.nascimento = nascimento
        self.faixa = faixa

    def idade(self):
        hoje = datetime.now()
        ano = hoje.year

        idade = ano - self.nascimento
        return idade
    
    def subir_faixa(self):
        Aluno.faixa = input('Insira a nova faixa: ')
        if Aluno.faixa == 'Branca':
            Aluno.Faixa == 'Cinza'
        elif Aluno.faixa == 'Cinza':
            Aluno.Faixa == 'Amarela'
        elif Aluno.faixa == 'Amarela':
            Aluno.Faixa == 'Laranja'
        elif Aluno.faixa == 'Laranja':
            Aluno.Faixa == 'Verde'
        elif Aluno.faixa == 'Verde':
            Aluno.Faixa == 'Azul'
        elif Aluno.faixa == 'Azul':
            Aluno.Faixa == 'Roxa'
        elif Aluno.faixa == 'Roxa':
            Aluno.Faixa == 'Marrom'
        elif Aluno.faixa == 'Marrom':
            Aluno.Faixa == 'Preta'
        elif Aluno.faixa == 'Preta':
            Aluno.Faixa == 'Coral'
        elif Aluno.faixa == 'Coral':
            Aluno.Faixa == 'Vermelha'