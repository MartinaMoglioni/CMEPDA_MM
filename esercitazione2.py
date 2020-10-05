#!/usr/bi/env python3
import argparse
import logging
import time
import string
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG)

def process(file_path):
    start_time = time.time()

    logging.info("Reading input %s ...", file_path)
    with open(file_path) as input_file:
        text = input_file.read()
    num_chars = len(text)
    logging.info("Done, %d characters found", num_chars)

    #char_dict = {chr(x):0 for x in range(ord('a'), ord('z') + 1)}
    char_dict = {ch:0 for ch in string.ascii_lowercase}
    for ch in text:
        ch = ch.lower()
        if ch in char_dict:
            char_dict[ch] +=1

        '''try:
            char_dict[ch.lower()] +=1
        except KeyError:
            pass'''

    elapsed_time = time.time()-start_time
    logging.info("Done in %.3f seconds", elapsed_time)
    num_letters = sum(char_dict.values())
    for ch, num in char_dict.items():
        print(f"{ch}->{num/num_letters:.3f}")
    print(char_dict)

    plt.bar(list(char_dict.keys()), char_dict.values(), color='g')
    plt.grid()
    plt.show()














if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=str, help="Path to the imput file")
    args = parser.parse_args()

    file_path = args.infile
    process('pg1497.txt')
