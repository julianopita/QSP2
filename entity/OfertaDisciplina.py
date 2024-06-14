class OfertaDisciplina:
    #atributos mesclando aula, professor, turma e sala. Na implementação final isso seria obtido através da interação com outras classes, conforme arquitetura
    def __init__(self, codigo:str, titulo: str, semestre: int, creditos: int, preRequisitos:list, oferecida: bool, idTurma: str, vagas: int, matriculas:int, diaSem: str, horaIn:int, horaFim: int, professorNome:str, salaNumero:int):
        
        self.codigo = codigo
        self.titulo = titulo
        self.semestre = semestre
        self.creditos = creditos
        self.preRequisitos = preRequisitos
        self.oferecida = oferecida        
        self.idTurma = idTurma
        self.vagas = vagas
        self.matriculas = matriculas
        self.diaSem = diaSem
        self.horaIn = horaIn
        self.horaFim = horaFim
        self.professorNome = professorNome
        self.salaNumero = salaNumero     
    
    

   
    