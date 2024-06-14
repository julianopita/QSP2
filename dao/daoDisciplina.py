from entity.OfertaDisciplina import OfertaDisciplina
from dao.dao import getData

def getDisciplina(searchAttribute = None, searchString = None):
    valIter = getData("OfertaDisciplina", searchAttribute, searchString)
    listDisc = []
    i=0
    for val in valIter:       
       discNome = "disc" + str(i)
       discNome = OfertaDisciplina(val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7], val[8], val[9], val[10], val[11], val[12], val[13])
       i = i+1
       listDisc.append(discNome)
    return listDisc