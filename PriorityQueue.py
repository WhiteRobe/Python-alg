class PriorityQueue:
    __pq = []
    __Min = 1

    def insert(self, tup):
        # tup should be data like (key,value)
        self.__pq.append(tup)
        self.__swim(len(self.__pq)-1)

    def size(self):
        return len(self.__pq)

    def set_order(self, is_min=True):
        self.__Min = 1 if is_min else -1

    def pop(self):
        if len(self.__pq) <= 0:
            raise Exception("优先队列已空")
        else:
            last_index = len(self.__pq) - 1
            self.__exch(0, last_index)
            value = self.__pq.pop(last_index)
            self.__sink(0)
        return value

    def find(self, index):
        return self.__pq[index]

    def get_pq(self):
        return self.__pq

    def change(self, index, new_tup):
        # $new_tup shape should like (index, value)
        for (tup, i) in zip(self.__pq, range(0, self.size())):
            if index == tup[0]:
                self.__pq[i] = new_tup

    def contains(self, index):
        for tup in self.__pq:
            if index == tup[0]:
                return True
        return False

    def __swim(self, index):
        father = (index - 1) // 2
        value = self.find(index)
        while father >= 0:
            if self.__compare(self.__pq[father][1], value[1]) > 0:
                self.__pq[index] = self.__pq[father]
                index = father
                father = (index - 1) // 2
            else:
                break
        self.__pq[index] = value

    def __sink(self, index):
        if len(self.__pq) <= 0:
            return
        value = self.find(index)
        lc = index * 2 + 1
        list_len = len(self.__pq)
        heap_deep = list_len // 2 - 1
        while index <= heap_deep:
            if lc + 1 > list_len - 1:
                pass
            else:
                lcv = self.find(lc)[1]
                rcv = self.find(lc + 1)[1]
                lc = lc if (self.__compare(lcv, rcv) < 0) else (lc + 1)
            if self.__compare(self.find(lc)[1], value[1]) <= 0:
                self.__pq[index] = self.__pq[lc]
                index = lc
                lc = index * 2 + 1
            else:
                break
        self.__pq[index] = value

    def __exch(self, i, j):
        temp = self.__pq[i]
        self.__pq[i] = self.__pq[j]
        self.__pq[j] = temp

    def __compare(self, a, b):
        # if you want get an result by DECS, feel free to exchange value [-1 1]
        if a == b:
            return 0
        else:
            return (1*self.__Min) if a > b else (-1*self.__Min)


# There is the demo how to use this alg-class
if __name__ == '__main__':
    # 1. get Instance and set priority-order
    S = PriorityQueue()
    S.set_order(is_min=False)
    # 2. prepare data
    list_v = [9, 8, 7, 4, 8, 5, 18, 5, 3, 2, 5, 6, 2, 0, -5, 2, -3, 0, 2.2]
    tup_v = [(x, y) for (x, y) in zip(range(0, len(list_v)), list_v)]
    # 3. feed data to queue
    for v in tup_v:
        S.insert(v)
    for _ in range(0, len(tup_v)):
        try:
            # 4. get sorted data
            print(S.pop())
        except Exception as e:
            # catch Exception for dev-mode
            print(e)
