# Add suitable imports here (from or import)
# Exercise 1.2.1.1 include foo from mymodule01
# Exercise 1.2.1.2 import the package mymodule02


def module_caller():
    return foo()


def package_caller():
    return exercises.mypackage01.mymodule02.bar()


def remove_duplicates(l):
    """ For any element in the set that is a duplicate remove the duplicates.
    The result should contain all elements, but only once."""

    return None


def update_attempt_451(l):
    l = [4, 5]
    return None


def update_attempt_452(l):
    l.clear()
    l = [4, 5]
    return None


def update_attempt_453(l):
    l.clear()
    l.extend([4, 5])
    return None


def remove_duplicates_with_sets(l):
    return None


def histogram(s):
    d = dict()
    for c in s.lower():
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def letter2words_histogram(s):
    word_dict = dict()
    pass
    return word_dict


def return_swapped_parameters(a, b):
    pass


if __name__ == "__main__":
    print(module_caller())
    print(package_caller())
