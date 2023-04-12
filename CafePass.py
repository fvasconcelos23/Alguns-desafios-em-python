class HashTable:
    def __init__(self, size):
        self.size = size
        self.values = [None] * self.size
        self.free_space = self.size

    def add(self, value):
        add_index = value % self.size

        while self.values[add_index] != None:
            add_index = (add_index+1) % self.size

        self.values[add_index] = value
        self.free_space -= 1

        return add_index

    def search(self, value):
        index = value % self.size
        for j in range(self.size):
            if self.values[index] == None:
                break
            if self.values[index] == value:
                return index
            index = (index + 1) % self.size
        return None


class CafePass:
    def __init__(self):
        pass

    def authorize(self, cpf, magic_number):
        magic_number = int(magic_number)

        if magic_number % 10 != 0:
            print("NOT Permission")
            return

        magic_number = magic_number//10

        used_digits = [None] * 10

        for d in list(cpf):
            d = int(d)
            if used_digits[d] == None:
                used_digits[d] = d
            else:
                used_digits[d] += d

        hash_table = HashTable(10)
        for j in used_digits:
            if j == None:
                continue
            pair_number = magic_number - j
            if pair_number >= 0 and hash_table.search(pair_number) != None:
                print("UP Permission")
                break
            hash_table.add(j)
        else:
            print("NOT Permission")


for x in range(int(input())):
    cpf, magic_number = input().split()
    CafePass().authorize(cpf, magic_number)
