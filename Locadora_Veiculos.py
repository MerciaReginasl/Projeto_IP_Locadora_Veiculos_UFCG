class Motorista:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.veiculo = None

    def atribuir_veiculo(self, veiculo):
        self.veiculo = veiculo

    def __str__(self):
        if self.veiculo:
            return f"Motorista: {self.nome}, Idade: {self.idade}, Veículo: {self.veiculo}"
        else:
            return f"Motorista: {self.nome}, Idade: {self.idade}, Veículo: Nenhum"


class Veiculo:
    def __init__(self, marca, modelo, placa, valor_aluguel):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.valor_aluguel = valor_aluguel

    def __str__(self):
        return f"Veículo: {self.marca} {self.modelo}, Placa: {self.placa}, Valor de Aluguel: R${self.valor_aluguel:.2f}"


class Aluguel:
    def __init__(self, motorista, veiculo, valor):
        self.motorista = motorista
        self.veiculo = veiculo
        self.valor = valor


class GerenciadorFrota:
    def __init__(self):
        self.motoristas = []
        self.veiculos = []
        self.alugueis_diarios = []

    def adicionar_motorista(self, motorista):
        self.motoristas.append(motorista)

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def alugar_veiculo(self, motorista, veiculo):
        if veiculo not in self.veiculos or motorista not in self.motoristas:
            print("Motorista ou veículo não encontrados.")
            return

        aluguel = Aluguel(motorista, veiculo, veiculo.valor_aluguel)
        self.alugueis_diarios.append(aluguel)
        print(f"Veículo alugado por {motorista.nome} - Valor: R${veiculo.valor_aluguel:.2f}")

    def calcular_somatorio_diario(self):
        total = sum(aluguel.valor for aluguel in self.alugueis_diarios)
        print(f"Somatório Diário: R${total:.2f}")

    def exibir_motoristas(self):
        print("Motoristas:")
        for motorista in self.motoristas:
            print(motorista)

    def exibir_veiculos(self):
        print("Veículos:")
        for veiculo in self.veiculos:
            print(veiculo)


# Exemplo de uso:
if __name__ == "__main__":
    # Criando instâncias de motoristas e veículos
    motorista1 = Motorista("João", 30)
    motorista2 = Motorista("Maria", 25)
    veiculo1 = Veiculo("Toyota", "Corolla", "ABC1234", 200)
    veiculo2 = Veiculo("Honda", "Civic", "DEF5678", 250)

    # Criando um gerenciador de frota
    gerenciador = GerenciadorFrota()

    # Adicionando motoristas e veículos ao gerenciador de frota
    gerenciador.adicionar_motorista(motorista1)
    gerenciador.adicionar_motorista(motorista2)
    gerenciador.adicionar_veiculo(veiculo1)
    gerenciador.adicionar_veiculo(veiculo2)

    # Alugando veículos
    gerenciador.alugar_veiculo(motorista1, veiculo1)
    gerenciador.alugar_veiculo(motorista2, veiculo2)

    # Exibindo motoristas e veículos
    gerenciador.exibir_motoristas()
    gerenciador.exibir_veiculos()

    # Calculando o somatório diário
    gerenciador.calcular_somatorio_diario()
