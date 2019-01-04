"""
To replace UNK tokens generated by the seq2seq model by various methods as follow:
    1. corresponding words in the original sequence using Levenshtein distance alignment
"""

import sys
from levenshtein_align import levenshtein_align

def replace_unk_leven(ref_sent, hyp_sent):
    # method 1
    a = ref_sent.split()
    b = hyp_sent.split()

    aout, bout = levenshtein_align(a,b)

    fixed = []

    for i in range(len(bout)):
        if bout[i] == '<unk>':
            if '*' not in aout[i]:
                fixed.append(aout[i])
            else:
                fixed.append('<unk>')

        elif '*' not in bout[i]:
            fixed.append(bout[i])

        else:
            pass # just ***

    fixed_sent = ' '.join(fixed)
    return fixed_sent

def fix_output_file(ref_file, hyp_file, replace_method):
    """
    args:
        ref_file: path to reference gec file
        hyp_file: path to hypothesis gec file
        replace_method: callable to handle sentence1 and sentence2
    """
    with open(ref_file, 'r') as file:
        ref_sentences = file.readlines()
    with open(hyp_file, 'r') as file:
        hyp_sentences = file.readlines()

    if len(ref_sentences) != len(hyp_sentences):
        raise Exception('num sentences not match')

    for s1, s2 in zip(ref_sentences, hyp_sentences):
        s1 = s1.strip()
        s2 = s2.strip()
        fixed_s2 = replace_method(s1,s2)

        print(fixed_s2)

def main():
    if(len(sys.argv) != 3):
        print('Usage: python3 replace_unk.py original corrupted')
        return
    original = sys.argv[1]
    corrupted = sys.argv[2]

    fix_output_file(original, corrupted, replace_unk_leven)

if __name__ == '__main__':
    main()