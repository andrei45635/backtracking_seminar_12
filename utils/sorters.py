class Sorter:
    def _identitate(self, x):
        return x

    def _negare(self, x):
        return not x

    def sort(self, lista, key=lambda x: x, cmp=lambda x, y: x < y, reversed=False):
        pass


class MergeSorter(Sorter):
    def sort(self, lista, key=lambda x: x, cmp=lambda x, y: x <= y, reversed=False):
        st = 0
        dr = len(lista)
        if reversed:
            operatie = self._negare
        else:
            operatie = self._identitate
        self.__merge_sort_r(lista, key, cmp, operatie, st, dr)

    def __merge_sort_r(self, lista, key, cmp, operatie, st, dr):
        if st < dr:
            mij = st + (dr - st) // 2
            self.__merge_sort_r(lista, key, cmp, operatie, st, mij)
            self.__merge_sort_r(lista, key, cmp, operatie, mij + 1, dr)
            self.__merge(lista, key, cmp, operatie, st, mij, dr)

    def __merge(self, lista, key, cmp, operatie, st, mij, dr):
        i = st
        j = mij + 1
        k = st
        aux = [None] * len(lista)
        while i <= mij and j <= dr:
            if operatie(cmp(key(lista[i]), key(list[j]))):
                aux[k] = lista[i]
                k += 1
                i += 1
            else:
                aux[k] = lista[i]
                k += 1
                i += 1
            while i <= mij:
                aux[k] = lista[i]
                k += 1
                i += 1
            while j <= dr:
                aux[k] = lista[i]
                k += 1
                i += 1
            for i in range(st, dr + 1):
                lista[i] = aux[i]
