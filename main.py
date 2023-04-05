#Iterator

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list

    def __iter__(self):
        self.counter_1 = 0
        self.counter_2 = 0
        return self

    def __next__(self):
        if self.counter_1 == len(self.list_of_lists):
            raise StopIteration
        item = self.list_of_lists[self.counter_1][self.counter_2]
        if self.counter_2 < len(self.list_of_lists[self.counter_1])-1:
            self.counter_2 += 1
        elif self.counter_2 == len(self.list_of_lists[self.counter_1])-1:
            self.counter_2 = 0
            self.counter_1 += 1
        return item

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

#Generator

import types


def flat_generator(list_of_lists):
    counter_1 = 0
    counter_2 = 0
    while counter_1 != len(list_of_lists):
        item = list_of_lists[counter_1][counter_2]
        if counter_2 < len(list_of_lists[counter_1]) - 1:
            counter_2 += 1
        elif counter_2 == len(list_of_lists[counter_1]) - 1:
            counter_2 = 0
            counter_1 += 1
        yield item


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()