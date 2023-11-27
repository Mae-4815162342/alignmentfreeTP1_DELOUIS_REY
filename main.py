from loading import load_directory
from kmers import stream_kmers, kmer2str
import pandas as pd
import numpy as np

def jaccard(fileA, fileB, k):
    """ Computes the jaccard index between each file using
    similar kmers as unit.
    :param Array fileA: the list of sequences in file A
    :param Array fileB: the list of sequences in file B
    :param int k: the length of a kmer
    :return float j: jaccard distance between fileA and fileB
    """
    j = 0
    Intersection = 0
    dicoA = {}
    lenA = 0
    lenB = 0
    for kmer in stream_kmers(fileA, k):
      lenA += 1
      if kmer not in dicoA:
        dicoA[kmer] = 1
      else:
        dicoA[kmer] += 1
    for kmer in stream_kmers(fileB, k):
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
    
    filenames = list(files.keys())
    matrix = np.ones((len(filenames), len(filenames)))
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            jaccard_dist = jaccard(files[filenames[i]], files[filenames[j]], k)
            print(filenames[i], filenames[j], jaccard_dist)
            matrix[i,j] = jaccard_dist
            matrix[j,i] = jaccard_dist
    matrix_df = pd.DataFrame(matrix, columns=filenames, index=filenames)
    matrix_df.to_csv('distance_matrix.csv')


## TEST: comparing the same sequences should give a distance of 1
#for i in range(len(files)):
#  assert(jaccard(files[filenames[i]], files[filenames[i]], k) == 1.0)