# Author: Layaa Sivakumar <layaasiv@uoregon.edu>

# Check out some Python module resources:
#   - https://docs.python.org/3/tutorial/modules.html
#   - https://python101.pythonlibrary.org/chapter36_creating_modules_and_packages.html
#   - and many more: https://www.google.com/search?q=how+to+write+a+python+module

'''This module is a collection of useful bioinformatics functions
written during the Bioinformatics and Genomics Program coursework.
You should update this docstring to reflect what you would like it to say'''

__version__ = "0.3"         # Read way more about versioning here:
                            # https://en.wikipedia.org/wiki/Software_versioning


DNA_bases = set('ATCGNatcgn')
RNA_bases = set('AUCGNaucgn')

def convert_phred(letter: str) -> int:
    '''Converts a single character into a phred score'''
    dec = ord(letter)
    return (dec - 33)

def qual_score(phred_score: str) -> float:
    '''This function takes the phred scores of a sequence as a string. It converts each score 
    into a quality score and returns the average score for the sequence as a float.'''
    phred_sum = 0
    for letter in phred_score:
        phred = convert_phred(letter)
        phred_sum += phred
    return phred_sum/len(phred_score)

def validate_base_seq(seq: str, RNAflag: bool = False) -> bool:
    '''This function takes a string. Returns True if string is composed
    of only As, Ts (or Us if RNAflag), Gs, Cs. False otherwise. Case insensitive.'''
    set_seq = set(seq)
    return seq_set.issubset(RNAbases if RNAflag else DNAbases)


def gc_content(DNA: str) -> float:
    '''Returns GC content of a DNA or RNA sequence as a decimal between 0 and 1.'''
    DNA = DNA.upper()
    GC_content = (DNA.count('G') + DNA.count('C'))/len(DNA)
    return GC_content

def oneline_fasta(multi_line_fa: str) -> str:
    '''This function takes a fasta text file as an argument and creates a new fasta file with duplicate
    information but multi-line sequences are converted to one line such that format alternates between 
    header line and sequence line.'''
    seq = ''
    with open(multi_line_fa, 'r') as gh, open('one_line.fa', 'w') as wh:
        for line in gh:
            line = line.strip('\n')
            if line.startswith('>'):
                if seq == '':
                    header = line
                else:
                    wh.write(header + '\n' + seq + '\n')
                    seq = ''
                    header = line
            else:
                seq += line
        wh.write(header + '\n' + seq + '\n')

if __name__ == "__main__":
    # write tests for functions above, Leslie has already populated some tests for convert_phred
    assert convert_phred("I") == 40, "wrong phred score for 'I'"
    assert convert_phred("C") == 34, "wrong phred score for 'C'"
    assert convert_phred("2") == 17, "wrong phred score for '2'"
    assert convert_phred("@") == 31, "wrong phred score for '@'"
    assert convert_phred("$") == 3, "wrong phred score for '$'"
    print("Your convert_phred function is working! Nice job")

    assert qual_score("JJJ") == 41.0, 'wrong avg qual score for "JJJ"'
    assert qual_score("AC?") == 32.0, 'wrong avg qual score for "AC?"'
    assert qual_score("@=") == 29.5, 'wrong avg qual score for "@="'
    print("qual_score function works!")

    assert validate_base_seq('ACTGTTA') == True, 'False for ACTGTTA'
    assert validate_base_seq('ACUUGA') == False, 'True for ACUUGA when RNAflag=False'
    assert validate_base_seq('ACUUGA', RNAflag=True) == True, 'False for ACUUGA when RNAflag=True'
    assert validate_base_seq('actgcg') == True, 'False for actgcg (not case insensitive)'
    assert validate_base_seq('acugcu', RNAflag=True) == True, 'False for acugcu (not case insensitive)'
    print("validate_base_seq function works!")

    assert gc_content('ACTGCTCCCA') == 0.6, 'wrong gc content for "ACTGCTCCCA"'
    assert gc_content('AAAAATTTTT') == 0.0, 'wrong gc content for "AAAAATTTTT"'
    assert gc_content('GGGGCCCGCGC') == 1.0, 'wrong gc content for "GGGGCCCGCGC"'
    print("gc_content fucntion works!")