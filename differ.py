import sys
import markov


def differ(chain1, chain2):


	#intersection = set(chain1.keys()).intersection(set(chain2.keys())) 

	# difference = set(chain1.keys()).difference(set(chain2.keys())) 

	#print "Chains in text 1: %d" % len(chain1) 
	#print "Chains in text 2: %d" % len(chain2)
	

	#print "Keys in both sets: %d" % len(intersection)

	# l = [len(chain1), len(chain2)]
	# match_percentage = 100 - ((len(difference) * 100) /max(l))
	# print "Approx match percentage: %d" % match_percentage


def main():
    args = sys.argv

    input_text1 = args[1]
    input_text2 = args[2]

    corpus1 = markov.read_file(input_text1)
    corpus2 = markov.read_file(input_text2)

    chain_dict1 = markov.make_chains(corpus1)
    chain_dict2 = markov.make_chains(corpus2)

    diff = differ(chain_dict1, chain_dict2)


if __name__ == "__main__":
    main()