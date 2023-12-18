from loading import load_directory
from sampling import sampling, sampling_xor
import pandas as pd
import numpy as np

def jaccard_xor(fileA, fileB, k, s):
    """ Computes the jaccard index between each file using
    similar sampled xorshifted kmers as unit.
    :param Array fileA: the list of sequences in file A
    :param Array fileB: the list of sequences in file B
    :param int k: the length of a kmer
    :param int s: the number of kmers to select
    :return float j: jaccard distance between fileA and fileB
    """
    j = 0
    Intersection = 0
    dicoA = {}
    lenA = 0
    lenB = 0
    for kmer in sampling_xor(fileA, k, s):
      lenA += 1
      if kmer not in dicoA:
        dicoA[kmer] = 1
      else:
        dicoA[kmer] += 1
    for kmer in sampling_xor(fileB, k, s):
      lenB += 1
      if kmer in dicoA:
        Intersection += 1
        dicoA[kmer] -= 1
        if dicoA[kmer] == 0:
          del dicoA[kmer]
    Union = lenB + lenA - Intersection
    j = Intersection/Union
    return j


if __name__ == "__main__":
    # Load all the files in a dictionary
    files = load_directory("data")
    k = 21
    s = 1000
    
    filenames = list(files.keys())
    matrix = np.ones((len(filenames), len(filenames)))
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            jaccard_dist = jaccard_xor(files[filenames[i]], files[filenames[j]], k, s)
            print(filenames[i], filenames[j], jaccard_dist)
            matrix[i,j] = jaccard_dist
            matrix[j,i] = jaccard_dist
    matrix_df = pd.DataFrame(matrix, columns=filenames, index=filenames)
    matrix_df.to_csv(f'distance_matrix_xor_{s}.csv')
