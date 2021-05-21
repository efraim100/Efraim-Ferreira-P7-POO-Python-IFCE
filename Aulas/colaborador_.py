     def __init__(self, codigo, nome, endereco, telefone, bairro, cep, cpf, salario_atual):
        self._codigo = codigo
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._bairro = bairro
        self._cep = cep
        self._cpf = cpf
        self._totalProventos = 0.0
        self._totalDescontos = 0.0
        self._salario_atual = salario_atual
        self.movimentos = []

     def inserirMovimento (self, movimentos):
        self.movimentos.append(movimentos)

     def calcularSalario(self):
        valorLiquido = 0.0
        for x in self.movimentos:
            if x.getTipomovimento() == 'P':
                self._totalProventos += x.getValor()
                valorLiquido += x.getValor()
            elif x.getTipomovimento() == 'D':
                self._totalDescontos += x.getValor()
                valorLiquido -= x.getValor()
            else:
                print(f'WARNING: ALGUM MOVIMENTO CRIADO TEM UM TIPO INVÁLIDO')

        return f'\nTotal de Salários:  {self.getTotalSalarios()}\
                 \nTotal de Proventos: {self.getTotalProventos()}\
                 \nTotal de Descontos: {self.getTotalDescontos()}\
                 \nTotal a Pagar:      {self.getTotalSalarios() + self.getTotalProventos() - self.getTotalDescontos()}\n'

     def getProventos(self):
        return self._totalProventos

     def getDescontos(self):
        return self._totalDescontos
    
     def getCodigo(self):
        return self._codigo

     def getNome(self):
        return self._nome

     def getEndereco(self):
        return self._endereco

     def getTelefone(self):
        return self._telefone

     def getBairro(self):
        return self._bairro

     def getCep(self):
        return self._cep

     def getCpf(self):
        return self._cpf
        
     def getSalario(self):
        return self._salario_atual