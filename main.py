import math, queue
from collections import Counter

####### Problem 3 #######
# Example test cases
test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]
def MED(S, T):
    # Base case for recursion
    if (S == ""):
        return (len(T))
    elif (T == ""):
        return (len(S))
    elif(S[0] == T[0]):
            return (MED(S[1:], T[1:]))
    else:
            return (1 + min(MED(S, T[1:]), MED(S[1:], T)))

def fast_MED(S, T, MED=None):
    if MED is None:
        MED = {}

    if (S, T) in MED:
        return MED[(S, T)]

    if S == "":
        MED[(S, T)] = len(T)
    elif T == "":
        MED[(S, T)] = len(S)
    elif S[0] == T[0]:
        MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
    else:
        insert = fast_MED(S, T[1:], MED)
        delete = fast_MED(S[1:], T, MED)
        MED[(S, T)] = 1 + min(insert, delete)

    return MED[(S, T)]

def fast_align_MED(S, T):
    fMED = fast_MED(S, T)  # Get the memoized edit distance table
    S_align = []
    T_align = []
    i = len(S)
    j = len(T)

    while i > 0 or j > 0:
        # Case 1: characters match
        if i > 0 and j > 0 and S[i - 1] == T[j - 1]:
            S_align.insert(0, S[i - 1])
            T_align.insert(0, T[j - 1])
            i -= 1
            j -= 1

        # Case 2: substitution
        elif i > 0 and j > 0 and fMED[i][j] == fMED[i - 1][j - 1] + 1:
            S_align.insert(0, S[i - 1])
            T_align.insert(0, T[j - 1])
            i -= 1
            j -= 1

        # Case 3: insertion
        elif j > 0 and fMED[i][j] == fMED[i][j - 1] + 1:
            S_align.insert(0, '-')
            T_align.insert(0, T[j - 1])
            j -= 1

        # Case 4: deletion
        elif i > 0 and fMED[i][j] == fMED[i - 1][j] + 1:
            S_align.insert(0, S[i - 1])
            T_align.insert(0, '-')
            i -= 1

    return ''.join(S_align), ''.join(T_align)







