from PriorityQueue import PriorityQueue  # need PriorityQueue.py


class HeapSort:
    # T(N) = NlogN
    # D(N) = 1
    # unstable
    __data_list = []
    __pq = PriorityQueue()

    def set_data(self, data_tup):
        # set data like [(0, 1), (index, value)]
        self.__data_list = data_tup
        self.__pq = PriorityQueue()

    def set_list_data(self, data_list):
        # set data like [1, 2, 3, 5, 4, value]
        data_tup = [(x, y) for (x, y) in zip(range(0, len(data_list)), data_list)]
        self.__data_list = data_tup

    def get_sorted_tup(self):
        if len(self.__data_list) == 0:
            raise Exception("get_sorted_tup:尚未初始化数据")
        else:
            self.__sort()
            return self.__data_list

    def get_sorted_list(self):
        return [x[1] for x in self.get_sorted_tup()]

    def set_order(self, is_asc=True):
        self.__pq.set_order(is_asc)

    def __sort(self):
        for i in self.__data_list:
            self.__pq.insert(i)
        for i in range(0, len(self.__data_list)):
            self.__data_list[i] = self.__pq.pop()


# There is the demo how to use this alg-class
if __name__ == '__main__':
    # 1. get Instance and set sort-order
    S = HeapSort()
    S.set_order(is_asc=False)
    # 2. prepare data
    list_v = [9, 8, 7, 4, 8, 5, 18, 5, 3, 2, 5, 6, 2, 0, -5, 2, -3, 0, 2.2]
    tup_v = [(x, y) for (x, y) in zip(range(0, len(list_v)), list_v)]
    # 3. feed data to sort-alg
    S.set_list_data(list_v)  # or S.set_data(tup_v)
    try:
        # 4. get sorted data
        print(S.get_sorted_tup())
    except Exception as e:
        # catch Exception for dev-mode
        print(e)
