class MovimentoFolha():

    def __init__(self, colaborador, descricao, valor, tipomovimento):
        self._colaborador = colaborador
        self._descricao = descricao
        self._valor = valor
        self._tipomovimento = tipomovimento
        
    def getColaborador(self):
        return self._colaborador

    def getDescricao(self):
        return self._descricao

    def getValor(self):
        return self._valor

    def getTipomovimento(self):
        return self._tipomovimento

    def setColaborador(self, colaborador):
        self._colaborador = colaborador

    def setDescricao(self, desc):
        self._descricao = desc

    def setValor(self, valor):
        self._valor = valor

    def setTipoMovimento(self, tipo):
        self._tipomovimento = tipo