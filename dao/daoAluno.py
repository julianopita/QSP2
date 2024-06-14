from entity.Aluno import Aluno
from dao.dao import getData, setData

def getAluno(searchAttribute = None, searchString = None):
    valIter = getData("Aluno", searchAttribute, searchString)
    listAluno = []
    i=0
    for val in valIter:       
       alunoNome = "aluno" + str(i)
       alunoNome = Aluno(val[0], val[1], val[2], val[3])
       i = i+1
       listAluno.append(alunoNome)
    return listAluno

def setChoices(aluno, disciplinas):
    setData("Aluno", 0, aluno[0], 4, disciplinas)
    