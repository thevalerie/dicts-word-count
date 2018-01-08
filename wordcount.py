from sys import argv


def count_words(filename):
    """Counts the words in a file"""

    word_counts = {}

    with open(filename) as text_file:

        for line in text_file:
            words_list = line.split()

            for word in words_list:
                word = word.strip(',.?;:!()\'\"_').lower()
                word_counts[word] = word_counts.get(word, 0) + 1

    for word, count in word_counts.iteritems():
        print word, count


count_words(argv[1])
