# Classe exemplo
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

pessoa1 = Pessoa("Josias", 28)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa("Maria", 30)
mensagem = pessoa2.saudacao()
print(mensagem)

# Herança
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso) -> None:
        super().__init__(nome, idade)
        self.curso = curso

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu sou estudante do curso {self.curso}."


estudante1 = Estudante("Pedro", 25, "Engenharia de Software")
mensagem = estudante1.saudacao()
print(mensagem)

