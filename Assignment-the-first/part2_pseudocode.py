#!/usr/bin/env python

def rev_comp(seq: str) -> str:
    '''Takes a DNA sequence and returns its reverse complement as a string'''
    return rc_seq 
Input: ACTGAAT
Expected output: ATTCAGT

# create list containing all the 24 possible indexes 
possible_indexes = []

# set up variables
header1 = ''
record1 = ''

header4 = ''
record4 = ''

index1 = ''
index2 = ''

while True:
    # open R1 file. 
        # Read line by line in a for loop and save the current header in header1.
        if header1 = '':
            break
        # Save the rest of the current record in record1.

    # open R4 file. 
        # Read line by line in a for loop and save the current header in header4. 
        # Save the rest of the current record in record4.

    # open R2 file. 
        # Read line by line in a for loop. 
        # Isolate the sequence line and save it in index1.

    # open R3 file. 
        # Read line by line in a for loop. 
        # Isolate the sequence line and save it in index2. 
        # Call rev_comp function on index2. Save output to rc_index2
        # Append index1 and index2 to the header (assigned previously).
        # if rc_index2 contains 'N' or does not meet quality score cutoff, write the current header1 + record1 into 'unknown_R1.fastq' and header4 + record4 into 'unknown_R4.fastq'
        # elif rc_index2 == index1 and index1 in possible_indexes, write the current header1 + record1 into 'matched_<index>_R1.fastq' and header4 + record4 into 'matched_<index>_R4.fastq'
        # else, write the current header1 + record1 into 'unmatched_R1.fastq' and header4 + record4 into 'unmatched_R4.fastq' 
    
    # clear variables
    header1 = ''
    record1 = ''

    header4 = ''
    record4 = ''

    index1 = ''
    index2 = ''
