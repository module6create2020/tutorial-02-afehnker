import pytest
from exercises.python102 import remove_duplicates, letter2words_histogram, return_swapped_parameters
from exercises.word_play import separate_histograms


class TestExercise1_2_4_1:

    @pytest.mark.parametrize("a,b",
                             [([2, 3, 1, 3, 5, 1], [2, 3, 5, 1]),
                              ([[4, 5, 2], [3, 4], [4, 5, 2], [1, 2]], [[3, 4], [4, 5, 2], [1, 2]])
                              ])
    def test_remove_duplicate(self, a, b):
        a_copy = a[:]
        remove_duplicates(a_copy)
        for x in b:
            a_copy.remove(x)
        if not a_copy == []:
            pytest.fail("The method 'remove_duplicates' failed with argument {}.\n"
                        "The result should have been {}, it was {}".format(a, b, a_copy))

    def test_none(self):
        assert remove_duplicates([1, 2, 3]) == None, "Function remove_duplicates should return None"


class TestExercise1_2_5_1:

    @pytest.mark.parametrize("a,b",
                             [
                                 ("house",
                                  {'h': {'house'}, 'o': {'house'}, 'u': {'house'}, 's': {'house'}, 'e': {'house'}}
                                  ),
                                 ("it is", {'i': {'is', 'it'}, 't': {'it'}, 's': {'is'}})
                             ])
    def test_letter_2_word(self, a, b):
        result = letter2words_histogram(a)
        if not result == b:
            pytest.fail("The method 'letter2words_histogram' failed with argument '{}'.\n"
                        "The result should have been '{}', it was '{}'".format(a, b, result))


class TestExercise1_2_6_1:

    @pytest.mark.parametrize("a,b",
                             [
                                 ((2, 3), (3, 2)),
                                 (([2, 3], "mouse"), ("mouse", [2, 3]))
                             ])
    def test_swap(self, a, b):
        result = return_swapped_parameters(a[0], a[1])
        if not result == b:
            pytest.fail("The method 'return_swapped_parameters' failed with argument '{}'.\n"
                        "The result should have been '{}', but was '{}'".format(a, b, result))


class TestExercise1_2_7_1:

    @pytest.mark.parametrize("a, b, c, d",
                             [
                                 ({'a': 1, 'n': 3, 'o': 1, 'y': 1, 'i': 1, 'g': 1},
                                  {'r': 1, 'a': 1, 'i': 1, 'n': 1, 'y': 1},
                                  {'o': 1, 'g': 1}, {'r': 1})
                             ])
    def test_letter_2_word(self,a, b, c, d):
        a_copy = a.copy()
        b_copy = b.copy()
        separate_histograms(a, b)
        if not a == c or not b == d:
            pytest.fail("The method 'separate_histograms' failed with argument '{}' and '{}'.\n"
                        "The result should have been '{}', and '{}'\n"
                        "It was '{}'and '{}".format(a, b, c, d,a_copy,b_copy))
