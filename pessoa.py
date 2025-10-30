class Pessoa:

    def __init__(self, nome: str, idade: int, altura: float):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def andar(self, distancia: float) -> str:
        print(f"{self.nome} andou {distancia} metros!")

    def cumprimentar(self) -> str:
        print(f"Olá! Meu nome é {self.nome}, tenho {self.idade} anos e {self.altura} de altura!")

    def bocejar(self) -> str:
        print("Bocejei!")
    
    def comer(self, comida: str) -> str:
        print(f"{self.nome} acabou de comer {comida}!")


primeira_pessoa = Pessoa("Maria", 15, 1.54)
primeira_pessoa.andar(40.5)
primeira_pessoa.cumprimentar()

segunda_pessoa = Pessoa("João", 24, 1.78)
segunda_pessoa.cumprimentar()
