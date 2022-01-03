import random
import unittest

from Punct import Punct
from utils.sorters import MergeSorter


class Teste(unittest.TestCase):
    def test_all(self):
        sorter = MergeSorter()
        self.__test_sorter_list(sorter)
        self.__test_sorter_list_class(sorter)
        self.__test_puncte()

    def __test_sorter_list(self, sorter):
        vector = [0,1,2,3,4,5,6,7,8,9]
        random.shuffle(vector)
        sorter.sort(vector)
        self.assertEqual(vector, [0,1,2,3,4,5,6,7,8,9])
        random.shuffle(vector)
        sorter.sort(vector, reverse=True)
        self.assertEqual(vector, [9,8,7,6,5,4,3,2,1])
        random.shuffle(vector)
        sorter.sort(vector, key=lambda x,y:x>y)
        self.assertEqual(vector, [9, 8, 7, 6, 5, 4, 3, 2, 1])

    def __test_sorter_list_class(self, sorter):
        vector = [Punct(0,2),Punct(9,2),Punct(3,2), Punct(4,2), Punct(8,2),Punct(7,2),Punct(6,2),Punct(1,2),Punct(2,2),Punct(5,2)]
        sorter.sort(vector, key=lambda x,y:x<y)
        result = [x.get_x() for x in vector]
        self.assertEqual(result, [0,1,2,3,4,5,6,7,8,9])

    def __test_puncte(self):
        punct0 = Punct(0,0)
        punct1 = Punct(0,2)
        punct2 = Punct(3,0)
        self.assertEqual(Punct.distanta_minima_3(punct0,punct1,punct2),9)
