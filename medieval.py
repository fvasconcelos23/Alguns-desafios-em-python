class heapBinary:
    def __init__(self):
        self.nos = 0
        self.heap = []

    def adiciona_no(self, u):
        self.heap.append(u)
        self.nos += 1
        f = self.nos

        while True:
            if f == 1:
                break
            p = f // 2

            if self.heap[p-1] >= self.heap[f-1]:
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
                f = p

    def remove_no(self):
        x = self.heap[0]
        self.heap[0] = self.heap[self.nos - 1]
        self.heap.pop()
        self.nos -= 1

        p = 1

        while True:
            f = 2 * p
            if f > self.nos:
                break
            if f+1 <= self.nos:
                if self.heap[f] > self.heap[f-1]:
                    f += 1
            if self.heap[p-1] >= self.heap[f-1]:
                break
            else:
                self.heap[f-1], self.heap[p-1] = self.heap[p-1], self.heap[f-1]
                p = f
        return x

    def maior_elemento(self):
        if self.nos != 0:
            return self.heap[0]
        return

    def left_son(self, i):
        if self.nos >= 2*i:
            return self.heap[2*i - 1]
        return

    def right_son(self, i):
        if self.nos >= 2*i+1:
            return self.heap[2*i]
        return

    def get_min(self):
        if len(self.heap) == 0:
            return None

        min_val = float('inf')
        for item in self.heap:
            if item < min_val:
                min_val = item

        return min_val

    def jogo_medieval(self, const):
        rounds = 0
        while True:

            size = len(self.heap)
            if size == 0:
                break

            maxi = self.maior_elemento()
            mini = self.get_min()

            self.remove_no()

            if maxi and mini:
                k = maxi - abs(mini * const)
                if k > 0:
                    self.adiciona_no(k)
            rounds += 1
        return rounds


seq = list(map(int, input().split()))
const = int(input())

heap = heapBinary()

for i in seq:
    heap.adiciona_no(i)

rounds = heap.jogo_medieval(const)

print(f"{rounds} rodadas, partindo para a próxima!")
