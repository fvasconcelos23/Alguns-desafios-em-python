class armazenamentocentral:
    def __init__(self, n):
        self.armazenamento = {i: None for i in range(n)}

    def add_dado(self, x):
        index = x % len(self.armazenamento)
        if self.armazenamento[index] is None:
            self.armazenamento[index] = x
            print(f"E: {index}")
        else:
            for i in range(len(self.armazenamento)):

                novo_index = (index + i) % len(self.armazenamento)
                if self.armazenamento[novo_index] is None:
                    self.armazenamento[novo_index] = x
                    print(f"E: {novo_index}")

                    return
            print("Toda memoria utilizada")

    def search_dado(self, d):
        for i in range(len(self.armazenamento)):
            if self.armazenamento[i] == d:
                print(f"E: {i}")

                return
        print("NE")

    def consultar_dado(self, m):
        if self.armazenamento[m] is None:
            print("D")

        else:
            print(f"A: {self.armazenamento[m]}")


n = int(input())
c = int(input())

a = armazenamentocentral(n)

for i in range(c):
    comando = input().split()
    if comando[0] == "ADD":
        a.add_dado(int(comando[1]))
    elif comando[0] == "SCH":
        a.search_dado(int(comando[1]))
    elif comando[0] == "CAP":
        a.consultar_dado(int(comando[1]))
