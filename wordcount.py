from sys import argv
from collections import Counter


def count_words(filename):
    """Counts the words in a file"""

    #word_counts = {}
    #word_counts = Counter()

    with open(filename) as text_file:

        # for line in text_file:
        #     words_list = line.split()
        text = text_file.read()
        words_list = text.split()

        for i, word in enumerate(words_list):
            words_list[i] = word.strip(',.?;:!()\'\"_').lower()
        word_counts = Counter(words_list)
            # word_counts[word] = word_counts.get(word, 0) + 1

    word_count_list = word_counts.items()
    word_count_list.sort()
    for word, count in word_count_list:
        print word, count       

    # for word, count in word_counts.iteritems():
    #     print word, count


count_words(argv[1])
