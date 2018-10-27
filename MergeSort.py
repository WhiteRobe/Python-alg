class MergeSort:
    # T(N) = NlogN
    # D(N) = N
    # Stable
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
        if lo >= hi:
            return
        mid = lo + (hi - lo) // 2
        self.__sort(lo, mid)
        self.__sort(mid + 1, hi)
        self.__merge(lo, mid, hi)

    def __merge(self, lo, mid, hi):
        i, j = (lo, mid + 1)
        aux = self.__data_list[lo:hi+1]

        for k in range(lo, hi+1):
            if i > mid and j <= hi:
                self.__data_list[k] = aux[j-lo]
                j += 1
            elif j > hi and i <= mid:
                self.__data_list[k] = aux[i-lo]
                i += 1
            elif self.__compare(aux[i-lo][1], aux[j-lo][1]) > 0:
                self.__data_list[k] = aux[j-lo]
                j += 1
            else:
                self.__data_list[k] = aux[i-lo]
                i += 1

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
    S = MergeSort()
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
