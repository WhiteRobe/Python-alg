class Quick3WaySort:
    # T(N) = N~NlogN
    # D(N) = logN
    # Unstable
    __data_list = []
    __order = 1

    def set_data(self, data_tup):
        # set data like [(0, 1), (index, value)]
        self.__data_list = data_tup

    def set_list_data(self, data_list):
        # set data like [1, 2, 3, 5, 4, value]
        data_tup = [(x, y) for (x, y) in zip(range(0, len(data_list)), data_list)]
        self.__data_list = data_tup

    def get_sorted_tup(self):
        if len(self.__data_list) == 0:
            raise Exception("get_sorted_tup:尚未初始化数据")
        else:
            self.__sort(0, len(self.__data_list) - 1)
            return self.__data_list

    def get_sorted_list(self):
        return [x[1] for x in self.get_sorted_tup()]

    def set_order(self, is_asc=True):
        self.__order = 1 if is_asc else -1

    def __sort(self, lo, hi):
        d_list = self.__data_list
        if hi <= lo:
            return
        lt, i, gt = (lo, lo + 1, hi)
        value = d_list[lo][1]
        while i <= gt:
            cmp = self.__compare(d_list[i][1], value)
            if cmp < 0:
                self.__exch(lt, i)
                lt += 1
                i += 1
            elif cmp > 0:
                self.__exch(i, gt)
                gt -= 1
            else:
                i += 1
        self.__sort(lo, lt - 1)  # lt point at the min_value
        self.__sort(gt + 1, hi)  # gt point at the max_value

    def __compare(self, a, b):
        # if you want get an result by DECS, feel free to exchange value [-1 1]
        if a == b:
            return 0
        else:
            return (1 * self.__order) if a > b else (-1 * self.__order)

    def __exch(self, i, j):
        temp = self.__data_list[i]
        self.__data_list[i] = self.__data_list[j]
        self.__data_list[j] = temp


# There is the demo how to use this alg-class
if __name__ == '__main__':
    # 1. get Instance and set sort-order
    S = Quick3WaySort()
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

