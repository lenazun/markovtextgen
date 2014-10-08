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

    first_words, third_word = random.choice(chains.items())
    sentence = [first_words[0], first_words[1], third_word[0]]
    
    how_long = 0

    while how_long <= 120:
        key = (sentence[-2], sentence[-1])
        random_next_word = random.choice(chains[key])
        sentence.append(random_next_word)
        how_long += len(random_next_word)
        if sentence[-1][-1:] in '.!?':
            break
    
    return sentence 

def print_nicely(sentence):
    final = ''
    for i in sentence:
        if i == "I":
            final += i + ' '
        else:
            final += i.lower() + ' '

    print final[0].upper() + final[1:]



def remove_punc(word):
    word = word.strip("\"#$%&'()*+-/:;<=>@[\\]^_`{|}~1234567890")
    return word

def main():
    args = sys.argv

    input_text = args[1]

    text = open(input_text)
    passage = text.read()
    corpus = passage.split()

    for i in range(len(corpus)):
        corpus[i] = remove_punc(corpus[i])

    chain_dict = make_chains(corpus)
    random_text = make_text(chain_dict)
    print_nicely(random_text)

if __name__ == "__main__":
    main()
