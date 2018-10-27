class KeySort:
    # T(N) = 11N+2R+1
    # D(N) = 2N+R
    # Stable?
    __data_list = []
    __R = None

    def set_data(self, data_tup, R):
        # set data like [(0, 1), (index, value^)] value^ should be like (group_key, item_properties)
        # $group-key$ should start from 0 and type of int
        self.__data_list = data_tup
        self.__R = R

    def set_list_data(self, data_list, R):
        # set data like [1, 2, 3, 5, 4, value]
        data_tup = [(x, y) for (x, y) in zip(range(0, len(data_list)), data_list)]
        self.set_data(data_tup, R)

    def get_sorted_tup(self):
        if len(self.__data_list) == 0:
            raise Exception("get_sorted_tup:尚未初始化数据")
        else:
            self.__sort()
            return self.__data_list

    def get_sorted_list(self):
        return [x[1] for x in self.get_sorted_tup()]

    def __sort(self):
        N = len(self.__data_list)
        aux = [None for _ in range(0, N)]
        count = [0 for _ in range(0, self.__R+1)]
        for i in range(0, N):
            count[self.__data_list[i][1][0]+1] += 1
        for i in range(0, self.__R):
            count[i+1] += count[i]
        for i in range(0, N):
            aux[count[self.__data_list[i][1][0]]] = self.__data_list[i]
            count[self.__data_list[i][1][0]] += 1
        self.__data_list = aux[0:N+1]


# There is the demo how to use this alg-class
if __name__ == '__main__':
    # 1. get Instance and set sort-order
    S = KeySort()
    # 2. prepare data
    list_v = [(0, "dai"), (2, "chang"), (3, "li"), (2, "fang"), (1, "lang"), (0, "wang")]
    tup_v = [(x, y) for (x, y) in zip(range(0, len(list_v)), list_v)]
    # 3. feed data to sort-alg
    S.set_list_data(list_v, R=4)  # or S.set_data(tup_v)
    try:
        # 4. get sorted data
        print(S.get_sorted_list())
    except Exception as e:
        # catch Exception for dev-mode
        print(e)
