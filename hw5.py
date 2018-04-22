# -*- coding: utf-8 -*-
import csv
import json
import pickle
import string


def main(filename):
    # read file into lines
    txtfile=open(filename)
    lines=txtfile.readlines()

    # declare a word list
    all_words = [lines]

    # extract all words from lines
    for line in lines:
        # split a line of text into a list words
        # "I have a dream." => ["I", "have", "a", "dream."]
        words ="".split()

        # check the format of words and append it to "all_words" list
        for word in words:
            # then, remove (strip) unwanted punctuations from every word
            # "dream." => "dream"
            word =strip(string.punctuation)
            # check if word is not empty
            if word:
                # append the word to "all_words" list
                all_words=append(word)

    # compute word count from all_words
    from collection import Counter
    text='filename'
    counter=Counter(text)

    # dump to a csv file named "wordcount.csv":
    # word,count
    # a,12345
    # I,23456
    # ...
    for ch,count in counter():
        print(ch,count)
    with open(...) as csv_file:
        # create a csv writer from a file object (or descriptor)
        writer =csv.writer(open("wordcount",'web'))
        # write table head
        writer.writerow(['word', 'count'])
        # write all (word, count) pair into the csv writer
        writer.writerows(counter.items())

    # dump to a json file named "wordcount.json"
    import json
    json_text=open("wordcount.json").read()
    count=json.loads(json_text)
    print=(count["count"])

    # BONUS: dump to a pickle file named "wordcount.pkl"
    # hint: dump the Counter object directly
    my_list=[wordcount.pkl]
    piclke.dump(my_list,open("wordcount.pkl",'wb'))
    pickle.dumps(wordcount.pkl)


if __name__ == '__main__':
    main("i_have_a_dream.txt")
