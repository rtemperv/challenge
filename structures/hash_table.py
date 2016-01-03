

class HashTable(object):
    """
    Dynamic hash table implementation
    """
    ratio_theshold = 0.75

    def __init__(self, start_bits=1):
        self._n_bits = start_bits
        self.__table = [None] * (2 ** start_bits)
        self._n_items = 0

    def _get_ratio(self):
        return self._n_items / len(self.__table)

    def _get_bucket(self, key):
        i_hash = hash(key) & ((2 ** self._n_bits) - 1)
        if self.__table[i_hash] is None:
            self.__table[i_hash] = []

        return self.__table[i_hash]

    def __getitem__(self, key):
        bucket = self._get_bucket(key)
        if bucket is not None:

            for item in bucket:
                if item[0] == key:
                    return item[1]

        raise KeyError('Element non existent')

    def __setitem__(self, key, value):
        self._remove(key)

        self._add(key, value)

        self._rebalance()

    def _add(self, key, item):
        bucket = self._get_bucket(key)

        bucket.append((key, item))
        self._n_items += 1

    def _remove(self, key):
        bucket = self._get_bucket(key)

        if bucket:
            for item in bucket:
                if item[0] == key:
                    bucket.remove(item)
                    self._n_items -= 1
                    return

    def _rebalance(self):
        if self._get_ratio() > self.ratio_theshold:
            self._n_bits += 1

            new_table = [None] * (2 ** self._n_bits)

            old_table = self.__table

            self.__table = new_table
            self._n_items = 0

            for i in old_table:
                if i:
                    for j in i:
                        self.__setitem__(*j)


