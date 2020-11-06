"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Adapted and modified by Ansgar Fehnker, 2019

Use this, but leave it as is, except for function separate_histograms and save_comparison.
See Exercise 1.2.7.1 and 1.2.7.2
"""

import string


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename,encoding="utf8")

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END OF THIS'):
            break

        process_line(line, hist)

    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS'):
            break


def process_line(line, hist):
    """Adds the words in the line to the histogram.

    Modifies hist.

    line: string
    hist: histogram (map from word to frequency)
    """

    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')

    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(string.punctuation + string.whitespace +"“”")
        if word[-2:] == "'s":
            word = word[:-2]
        word = word.lower()
        # update the histogram
        hist[word] = hist.get(word, 0) + 1


def top_words(hist, number=10):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort()
    t.reverse()
    s = []
    for pair in t:
        s.append((pair[1], pair[0]))

    elements = min(number,len(s))
    return s[0:elements]


def separate_histograms(word_hist1, word_hist2):
    pass
    return None


def print_comparison(file1,file2):
    book1 = process_file('books/'+file1, skip_header=True)
    book2 = process_file('books/'+file2, skip_header=True)
    separate_histograms(book1,book2)
    book1_top10 = top_words(book1,20)
    book2_top10 = top_words(book2,20)
    filename1 = file1[0:file1.find(".")]
    filename2 = file2[0:file2.find(".")]

    print('#, '+filename1+', '+filename2)
    for i in range(min(len(book1_top10),len(book1_top10))):
        print("%d, %s, %s " % (i+1,book1_top10[i][0], book2_top10[i][0]))
    return None


def save_comparison(file1,file2):
    pass
    return None


if __name__ == '__main__':
    print_comparison('emma.txt','wotw.txt')





