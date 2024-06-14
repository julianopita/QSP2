from dao.dao import getData

class Aluno:
    def __init__(self, matricula: int, nome: str, curso: str, disciplinasCursadas: list):
        self.matricula = matricula 
        self.nome = nome
        self.curso = curso
        self.disciplinasCursadas = disciplinasCursadas
        self.disciplinasMatriculads = []

    def getAluno(matricula): #tratar erro
        alunoUnico = getData("Aluno", 0, matricula)
        return alunoUnico   
    