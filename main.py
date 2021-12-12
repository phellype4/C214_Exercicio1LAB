class Calc:
    def __init__(self, mensagem):
        self.mensagem = mensagem
#soma
    def soma(n1, n2):
        return n1 + n2
#subtraçao
    def sub(n1, n2):
        return n1 - n2
#multiplikaçao
    def mult(n1, n2):
        return n1 * n2
#divisao
    def div(n1, n2):
        return n1 / n2

    def mensagem_designP(self):
        print(self.mensagem)

    def altera_mensagem_designP(self, novam):
        self.mensagem = novam

cal1 = Calc("Mensagem para teste 1")


