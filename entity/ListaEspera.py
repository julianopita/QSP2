from entity.Aluno import Aluno
from entity.OfertaDisciplina import OfertaDisciplina

class ListaEspera:
    def __init__(self, disciplina: OfertaDisciplina, id: str):
        self.id = id
        self.disciplina = disciplina
        self.alunos = []

    def addAluno(self, aluno):
        self.alunos.append(aluno)
        return len(self.alunos) #retorna a posição do aluno na lista

    def removeAluno(self, aluno: Aluno):
        #NOT IMPLEMENTED - removes aluno from list.
        return NotImplemented