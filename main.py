
class Produto:
    def __init__(self,codigo, nome, descricao, categoria, preco,estoque,perecivel):
        if type(codigo) != int or codigo > 0: 
            raise ValueError("Codigo invalido!")
        if type(nome) != str or len(nome) == 0:
            raise ValueError("Nome ")
        if type(descricao) != str or len(nome) == 0:
            raise ValueError("Descricao muito curta")

        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.categoria = categoria
        self.estoque = estoque
        self.preco = preco
        self.perecivel = perecivel
    def reajustar_preco(self, percentual):
        self.preco = self.preco * (1 + percentual/100)
        