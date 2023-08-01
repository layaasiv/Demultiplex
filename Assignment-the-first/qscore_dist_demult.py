#!/usr/bin/env python 

# import all necessary modules
import bioinfo
import argparse
import numpy
import gzip
import matplotlib.pyplot as plt

# set up argparse
def get_args():
    parser = argparse.ArgumentParser(description="A program to k-merize our data set at different sizes for k and plot the result")
    parser.add_argument("-o", "--outputfig", help="Name of the histogram plot png file", required=True)
    parser.add_argument("-f", "--file", help="File name to process", required=True)
    parser.add_argument("-s", "--seqlen", help="Length of sequence line (biological read or index)", required=True)
    return parser.parse_args()

# define variables
args = get_args()
file_name = args.file
out_png = args.outputfig
seq_len = int(args.seqlen)

# define all necessary functions
def init_list(lst: list, value: float=0.0) -> list:
    '''This function takes an empty list and will populate it with the value passed in "value". If no value is passed, 
    initializes list with 101 values of 0.0.'''
    for i in range(seq_len):
        lst.append(value)
    return lst

def populate_list(file: str) -> tuple[list, int]:
    """Takes a text file as argument. Converts quality score to a phred value, and sums all phred values at a particular 
    position and stores it in a list. Final list contains sum of phred scores per position across all reads in the files."""
    qscore_list: list = []
    qscore_list = init_list(qscore_list)
    with gzip.open(file,"rt") as fh:
        num_lines: int = 0
        for line in fh:
            num_lines+=1
            if num_lines%4 == 0:
                for a in range(seq_len):
                    phred_val = bioinfo.convert_phred(line[a])
                    qscore_list[a] += phred_val
    return qscore_list, num_lines

# populting qscore_list with sum of qscores at each base position and assigning values to global variables
qscore_list, num_lines = populate_list(file_name)

# calcultes mean qscore per base position and assign back to qscore_list
for i in range(seq_len): 
    avg_q = qscore_list[i]/(num_lines/4)
    qscore_list[i] = avg_q

# plot histogram
x = range(seq_len)
y = qscore_list

fig, ax = plt.subplots()

ax.set_xlabel('# Base Pair')
ax.set_ylabel('Mean Quality Score')
ax.set_title('Mean Quality Score per Base Position')

plt.bar(x, y)
plt.savefig(out_png)