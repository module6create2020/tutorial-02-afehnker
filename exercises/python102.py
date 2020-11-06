from exercises.mymodule01 import foo
import exercises.mypackage01.mymodule02


def module_caller():
    return foo()


def package_caller():
    return exercises.mypackage01.mymodule02.bar()


def remove_duplicates(l):
    """ For any element in the set that is a duplicate remove the duplicates.
    The result should contain all elements, but only once."""

    unique_elements = list()

    for x in l[:]:
        if x not in unique_elements:
            unique_elements.append(x)
        else:
            l.remove(x)
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
    l_set=set(l)
    l.clear()
    l.extend(l_set)
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
    for w in s.lower().split():
        for l in w:
            if l in word_dict:
                word_dict[l].add(w)
            else:
                word_dict[l] = {w}
    return word_dict


def return_swapped_parameters(a,b):
    return b, a


if __name__ == "__main__":
    print(module_caller())
    print(package_caller())
