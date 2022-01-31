class Pessoa:
    def __init__(self, nome=None, idade = 29):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Antonio')
    print(id(p))
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    p.nome = 'Jonatha'
    print(p.nome)
    print(p.idade)
