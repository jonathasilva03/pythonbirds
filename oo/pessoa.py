class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade = 29):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_statico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    Jonatha = Pessoa(nome='Jonatha')
    Benicio = Pessoa(Jonatha, nome='Benicio')
    print(id(Benicio))
    print(Pessoa.cumprimentar(Benicio))
    print(Benicio.cumprimentar())
    print(Benicio.nome)
    print(Benicio.idade)
    for filho in Benicio.filhos:
        print(filho.nome)
    Benicio.sobrenome = 'Lima'
    del Benicio.filhos
    print(Benicio.__dict__)
    print(Jonatha.__dict__)
    print(Pessoa.olhos)
    print(Jonatha.olhos)
    print(Benicio.olhos)
    print(Pessoa.metodo_statico(), Jonatha.metodo_statico())
    print(Pessoa.nome_e_atributo_de_classe(), Jonatha.nome_e_atributo_de_classe())

