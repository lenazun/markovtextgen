#!/usr/bin/env python

import sys
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_dict = {}

    for i in range(len(corpus) - 2):
        markov_dict.setdefault((corpus[i], corpus[i + 1]), []).append(corpus[i + 2])

    return markov_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    w, rez = random.choice(chains.items())
    print w[0], w[1], rez
    
    return 

def remove_punc(word):
    word = word.strip("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    return word

def main():
    args = sys.argv

    # Change this to read input_text from a file
    input_text = args[1]

    text = open(input_text)
    passage = text.read()
    corpus = passage.split()

    for i in range(len(corpus)):
        corpus[i] = remove_punc(corpus[i])

    #print corpus[0:30]

    chain_dict = make_chains(corpus)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()
