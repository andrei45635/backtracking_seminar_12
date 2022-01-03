import math

from Punct import Punct
from utils.sorters import MergeSorter

if __name__ == '__main__':

    def merge(aux, lista, st, mij, dr):
        i = st
        j = mij + 1
        k = st
        aux = [None] * len(lista)
        while i <= mij and j <= dr:
            if lista[i].get_y() <lista[j].get_y():
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

    def solve_closest_points_r(puncte,puncte_y,st,dr):
        if dr - st == 1:
            if puncte[st].get_y() < puncte[dr].get_y():
                puncte_y[st] = puncte[st]
                puncte_y[dr] = puncte[dr]
            else:
                puncte_y[dr] = puncte[st]
                puncte_y[st] = puncte[dr]
            return Punct.distanta_minima_2(puncte[st], puncte[dr])
        if dr - st == 2:
            pcts = [puncte[st],puncte[st+1],puncte[dr]]
            pcts.sort(key=lambda x:x.get_x())
            puncte_y[st] = pcts[0]
            puncte_y[st+1] = pcts[1]
            puncte_y[dr] = pcts[2]
            return Punct.distanta_minima_3(puncte[st],puncte[st+1],puncte[dr])
        else:
            mij = st + (dr-st)//2
            median = puncte[mij]
            ds = solve_closest_points_r(puncte,puncte_y,st,mij)
            dd = solve_closest_points_r(puncte,puncte_y,mij+1,dr)
            merge(puncte, puncte_y, st, mij, dr)
            d = min(ds, dd)
            candidati = []
            for i in range(st,dr+1):
                if abs(puncte_y[i].get_x()-median.get_x()) < d:
                    candidati.append(puncte_y[i])
            for i in range(1, len(candidati)-8):
                for j in range(0,7):
                    nd = Punct.distanta_minima_2(candidati[i], candidati[i+j])
                    if nd < d:
                        d = nd
            return d

    puncte = [Punct(0,2),Punct(9,4),Punct(3,1), Punct(4,9), Punct(8,0),Punct(7,8),Punct(6,3),Punct(1,5),Punct(2,7),Punct(5,6)]
    puncte_y = [None]*len(puncte)
    sorter = MergeSorter()
    sorter.sort(puncte, key=lambda x:x.get_x())
    solve_closest_points_r(puncte,puncte_y,0,len(puncte)-1)
    print(math.sqrt(d))
    for punct in puncte_y:
        print(punct)