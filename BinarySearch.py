from QuickSort import Quick3WaySort

class BinarySearch:
    # need ordered array (ASC)
    __data_list = None
    __key = None

    def set_data(self, data_tup):
        # set data like [(0, 1), (index, value)]
        self.__data_list = data_tup

    def set_list_data(self, data_list):
        # set data like [1, 2, 3, 5, 4, value]
        data_tup = [(x, y) for (x, y) in zip(range(0, len(data_list)), data_list)]
        self.__data_list = data_tup

    def search(self, key):
        if len(self.__data_list) == 0:
            raise Exception("get_sorted_tup:尚未初始化数据")
        self.__key = key
        return self.__rank(0, len(self.__data_list)-1)

    def __rank(self, lo, hi):
        if hi < lo:
            return
        mid = lo + (hi - lo) // 2
        mid_value = self.find(mid)
        cmp = self.__compare(self.__key[1], mid_value[1])
        if cmp < 0:
            return self.__rank(lo, mid-1)
        elif cmp > 0:
            return self.__rank(mid+1, hi)
        else:
            return mid

    def find(self, index):
        return self.__data_list[index]

    def __compare(self, a, b):
        # if you want get an result by DECS, feel free to exchange value [-1 1]
        if a == b:
            return 0
        else:
            return 1 if a > b else -1


# There is the demo how to use this alg-class
if __name__ == '__main__':
    # 1. get Instance
    Sort = Quick3WaySort()
    Sort.set_order(is_asc=True)
    # 2. prepare data
    list_v = [9, 8, 7, 4, 8, 5, 18, 5, 3, 2, 5, 6, 2, 0, -5, 2, -3, 0, 2.2]
    tup_v = [(x, y) for (x, y) in zip(range(0, len(list_v)), list_v)]
    # 3. feed data to sort-alg
    Sort.set_data(tup_v)  # or S.set_list_data(tup_v)
    try:
        # 4. get sorted result
        sorted_result = Sort.get_sorted_tup()
        # 5. get instance
        S = BinarySearch()
        # 6. feed data to searching-alg
        S.set_data(sorted_result)
        # 7. set searching target
        index = 2
        target = sorted_result[index]
        # 8. get searching result
        print("Tuple:{0} in {1}, should be {2}."
              .format(target, S.search(target), index))
    except Exception as e:
        # catch Exception for dev-mode
        print(e)
