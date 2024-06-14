
from entity.SisPag import encaminhaPagamento
from entity.ListaEspera import ListaEspera
#from entity.Disciplina import Disciplina (somente na implementação final)

from dao.daoDisciplina import getDisciplina
from dao.daoAluno import getAluno, setChoices

class ControladorInscricao:
    #construtor
    def __init__(self, id=1):
        self.id = id
        self.aluno = None
        self.listaEspera = {}
        self.ofertaDisciplina = []
        self.disciplina = []
       
    
    
    #listagemAlunos
    def listaAlunos(self):
        listaGeral = getAluno()        
        return listaGeral
    
    def selecionarAluno(self, aluno):
        self.aluno = aluno      
    
    #verificações de disponibilidade OK
    def checaVagas(self, listaDisciplinas):        
        naoDisponivel = []
        disciplinas = []
        for disc in listaDisciplinas:            
            disc = getDisciplina(0, disc[0])
            disciplinas.append(disc[0])
        
        for disciplina in disciplinas:            
            if disciplina.matriculas >= disciplina.vagas:
                naoDisponivel.append(disciplina)
        return naoDisponivel  
    
    
    def mostrarListaDisciplinas(self):        
        listaGeral = getDisciplina(5, 'True')
                
        #checa pré requisitos OK    
        def checaPrerequisitos(self, listaDisciplinas):   
            alu = getAluno(0, int(self.aluno[0]))
            aluno = alu[0]         
            disciplinas = []
            PreRequisitos = []             

            for disc in listaDisciplinas:                                   
                disc = getDisciplina(0, disc.codigo)                       
                disciplinas.append(disc)                                 

            #verifica e organiza as disciplinas cursadas
            disciplinasCursadas = []
            if aluno.disciplinasCursadas:
                disciplinasCursadas = aluno.disciplinasCursadas.split(',')        

            #checa se aluno já cursou a disciplina ou se preenche os prerequisitos
            for disciplina in disciplinas:
                
                if disciplina[0].preRequisitos:                    
                    preRequisitos = disciplina[0].preRequisitos.split(',')                
                    disciplinasCursadas = aluno.disciplinasCursadas.split(',')
                    
                    if all(item in disciplinasCursadas for item in preRequisitos) and disciplina[0].titulo not in disciplinasCursadas:            
                        PreRequisitos.append(disciplina[0])
                else:
                    PreRequisitos.append(disciplina[0])            
            return PreRequisitos
        
        listaDisponivel = checaPrerequisitos(self, listaGeral)
        return listaDisponivel

     #checa conflito de horário OK   
    def checaHorarios(self, listaDisciplinas):
        conflitoInd = []
        disciplinas = []
        for disc in listaDisciplinas:                        
            disc = getDisciplina(0, disc[0])            
            disciplinas.append(disc[0])
        

        def conflitoHorario(inicio1, fim1, inicio2, fim2):
            return inicio1 < fim2 and inicio2 < fim1        
        
        for i in range(len(disciplinas)):
            for j in range(i+1, len(disciplinas)):
                if disciplinas[i].diaSem == disciplinas[j].diaSem:
                    if conflitoHorario(disciplinas[i].horaIn, disciplinas[i].horaFim, disciplinas[j].horaIn, disciplinas[j].horaFim):
                        conflitoInd.append(disciplinas[i])
                        conflitoInd.append(disciplinas[j])                        
        return conflitoInd
    
    #checa créditos máximos OK
    def checaCreditos (self, listaDisciplinas, creditosMaximos=20):
        disciplinas = []
        for disc in listaDisciplinas:            
            disc = getDisciplina(0, disc[0])
            disciplinas.append(disc)
        creditosTotais = sum(disciplina[0].creditos for disciplina in disciplinas)
        if creditosTotais > 20:
            return (True, creditosTotais)
        return False
           
    def realizarInscricao(self, listaDisciplinas):
        matrDisciplinas=[]
        for disciplina in listaDisciplinas:
            matrDisciplinas.append(disciplina[0])
        print(matrDisciplinas)
        print(encaminhaPagamento())
        setChoices(self.aluno, matrDisciplinas)
               

#TKInter
    def handle_selection(self, selected_courses):
        HD = self.checaHorarios(selected_courses)
        TC = self.checaCreditos(selected_courses)
        ND = self.checaVagas(selected_courses)       
        #NP = self.checaPrerequisitos(selected_courses)

        if HD:
            return False, f"As seguintes disciplinas possuem conflito de horários: {', '.join([disciplina.titulo for disciplina in HD])}.\nPor favor faça nova seleção.", []
        if TC:
            return False, f"O número de créditos ultrapassa o máximo permitido (20). Créditos das disciplinas selecionadas: {TC[1]}.\nPor favor faça nova seleção.", []
        if ND:
            return False, f"As seguintes disciplinas não possuem mais vagas: {', '.join([disciplina.titulo for disciplina in ND])}.\nPor favor faça nova seleção.", ND
        #if NP:
            #return False, f"O aluno já cursou ou não possui os pré requisitos das seguintes disciplinas: {', '.join([disciplina.titulo for disciplina in NP])}.\nPor favor faça nova seleção.", []
        return True, f"A seleção de disciplinas é válida. Total de créditos: {TC}", [] 

    def handle_waitlist(self, waitlist_choices, aluno):
        print(aluno)
        posicaoListaEspera = {}
        for course_name, join_waitlist in waitlist_choices.items():
            if join_waitlist:
                if course_name not in self.listaEspera:
                    self.listaEspera[course_name] = ListaEspera(len(self.listaEspera) +1, course_name)
                position = self.listaEspera[course_name].addAluno(aluno)
                posicaoListaEspera[course_name] = position           
                print(self.listaEspera[course_name])        
        return posicaoListaEspera
    
       