#!/usr/bin/env python

import sys
import random
import twitter
import os

api = twitter.Api(consumer_key=os.environ.get('TWITTER_CONSUMER_KEY'),
                  consumer_secret=os.environ.get('TWITTER_CONSUMER_SECRET'),
                  access_token_key=os.environ.get('TWITTER_ACCESS_TOKEN_KEY'),
                  access_token_secret=os.environ.get('TWITTER_ACCESS_TOKEN_SECRET'))





def read_file(input_file):
    text = open(input_file)
    passage = text.read()
    corpus = passage.split()

    for i in range(len(corpus)):
        corpus[i] = remove_punc(corpus[i])

    return corpus


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_dict = {}

    for i in range(len(corpus) - 2):
        markov_dict.setdefault((corpus[i], corpus[i + 1]), []).append(corpus[i + 2])

    return markov_dict

def make_text(chain1, chain2):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    first_words = ['a']

    while not first_words[0][0].isupper():
        first_words, third_word = random.choice(chain1.items())
        #print first_words[0]
    
    sentence = [first_words[0], first_words[1], third_word[0]]
    
    how_long = (len(sentence[0]) + len(sentence[1]) + len(sentence[2]))
    toggle = 0

    while how_long <= 120:
        key = (sentence[-2], sentence[-1])
        toggle += 1
        if toggle % 2 == 1:
            if key in chain2:
                random_next_word = random.choice(chain2[key])
                print "from dic 2"
            else:
                continue
        else:
            if key in chain1:
                random_next_word = random.choice(chain1[key])
                print "from dic 1"
            else:
                continue

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

    return final[0].upper() + final[1:]


def remove_punc(word):
    word = word.strip("\"#$%&'()*+-/:;<=>@[\\]^_`{|}~1234567890")
    return word

def post_to_twitter(sentence):
    print sentence
    confirm = raw_input("Tweet? Y or N: ")
    if confirm == "Y":
        status = api.PostUpdate(sentence)
        print status.text
    else:
        pass

def main():
    args = sys.argv

    input_text1 = args[1]
    input_text2 = args[2]

    corpus1 = read_file(input_text1)
    corpus2 = read_file(input_text2)

    chain_dict1 = make_chains(corpus1)
    chain_dict2 = make_chains(corpus2)

    random_text = make_text(chain_dict1, chain_dict2)
    final_tweet = print_nicely(random_text)
    post_to_twitter(final_tweet)



if __name__ == "__main__":
    main()
