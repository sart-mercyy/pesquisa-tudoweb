class Pesquisa:
    def __init__(self, total):
        self.total = total
        self.excelente = 0
        self.ruim = 0

    def coletar_dados(self):
        for i in range(1, self.total + 1):
            print(f"\nEntrevistado {i}")

            nome = input("Nome: ")
            idade = int(input("Idade: "))

            print("Avaliação:")
            print("1 - EXCELENTE")
            print("2 - BOM")
            print("3 - RUIM")

            opiniao = int(input("Opinião: "))

            if opiniao == 1:
                self.excelente += 1
            elif opiniao == 3:
                self.ruim += 1

    def mostrar_resultado(self):
        print("\nRESULTADO FINAL")
        print(f"Quantidade de EXCELENTE: {self.excelente}")
        print(f"Quantidade de RUIM: {self.ruim}")


class TestePesquisa:
    def executar(self):
        dados = [
            ("Ana", 20, 1),
            ("Bruno", 25, 2),
            ("Carlos", 30, 1),
            ("Daniela", 22, 3),
            ("Eduardo", 40, 1),
            ("Fernanda", 35, 2),
            ("Gabriel", 28, 3),
            ("Helena", 19, 1),
            ("Igor", 50, 2),
            ("Juliana", 27, 1),
        ]
        
        pesquisa = Pesquisa(len(dados))

        for nome, idade, opiniao in dados:
            if opiniao == 1:
                pesquisa.excelente += 1
            elif opiniao == 3:
                pesquisa.ruim += 1

        print("\nTESTE COM 10 ENTREVISTADOS")
        pesquisa.mostrar_resultado()


modo = input("Digite 't' para teste ou qualquer tecla para execução normal: ")

if modo.lower() == 't':
    TestePesquisa().executar()
else:
    pesquisa = Pesquisa(50)
    pesquisa.coletar_dados()
    pesquisa.mostrar_resultado()