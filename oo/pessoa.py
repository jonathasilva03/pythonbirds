class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade = 29):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

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

