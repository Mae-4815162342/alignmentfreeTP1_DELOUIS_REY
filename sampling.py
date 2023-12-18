from kmers import stream_kmers, stream_kmers_xor, kmer2str
from xor import reversed_xorshift
import heapq

def sampling(file, k, s):
  """Samples the s smaller kmers from file and puts them in a heapq object
  :param Array file: sequences from a genomic file
  :param int k: length of a kmer
  :param int s: number of samples to select
  :return heapq sketch: the selected kmers"""
  sketch = [float('-inf')] * s
  heapq.heapify(sketch)
  for kmer in stream_kmers(file, k):
    # select minimum
    elem = sketch[0]
    if -kmer > elem:
      heapq.heappushpop(sketch, -kmer)
  return sketch

# Test of sampling:
"""
fileA = ['AGTCAGTCGT',
        'TGACTGGGGGTAAACCGCGTTGCAC']
fileB = ['AGTCAGAACTGGGTGTTCGTCGTAAAAAAAAAAAACATGCTTAGC',
        'TGCATGCATTGTCTAGTCGTTGTCAGTTCTCTAGCTATTGCAC']
s = 10
k = 3
sketchA = sampling(fileA, k, s)
sketchB = sampling(fileB, k, s)

print('Simple sketch')
print('Sketch for A')
str_temp = ''
for value in sketchA:
  str_temp += f'{kmer2str(-value, k)} '
print(str_temp)

print('Sketch for B')
str_temp = ''
for value in sketchB:
  str_temp += f'{kmer2str(-value, k)} '
print(str_temp)
"""

def sampling_xor(file, k, s):
  """Samples the s smaller shifted kmers from file and puts them in a heapq object
  :param Array file: sequences from a genomic file
  :param int k: length of a kmer
  :param int s: number of samples to select
  :return heapq sketch: the selected shifted kmers"""
  sketch = [float('-inf')] * s
  heapq.heapify(sketch)
  for kmer in stream_kmers_xor(file, k):
    # select minimum
    elem = sketch[0]
    if -kmer > elem:
      heapq.heappushpop(sketch, -kmer)
  return sketch

# Test of sampling_xor:
"""
sketchA = sampling_xor(fileA, k, s)
sketchB = sampling_xor(fileB, k, s)

print('Shifted sketch')
print('Sketch for A')
str_temp = ''
for value in sketchA:
  str_temp += f'{kmer2str(-reversed_xorshift(value), k)} '
print(str_temp)

print('Sketch for B')
str_temp = ''
for value in sketchB:
  str_temp += f'{kmer2str(-reversed_xorshift(value), k)} '
print(str_temp)
"""