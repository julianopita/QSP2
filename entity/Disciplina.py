class Disciplina:
    preRequisitos = []
    def __init__(self, codigo:str, titulo: str, semestre: int, creditos: int, preRequisitos:list, oferecida: bool):
      
        self.codigo = codigo
        self.titulo = titulo
        self.semestre = semestre
        self.creditos = creditos
        self.oferecida = oferecida 
        self.preRequisitos = preRequisitos   
    
    def addPreRequisito (self, disciplina):
        if isinstance(disciplina, Disciplina):
            self.preRequisitos.append(disciplina)
        else:
            raise ValueError("Pré-requisito precisa ser uma instância de Disciplina")
    
    #def removePreRequisito(self, disciplina):
    #return NotImplemented