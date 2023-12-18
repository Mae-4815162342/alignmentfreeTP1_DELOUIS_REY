from xor import xorshift

def stream_kmers(file, k):
  """ Transforms a file of nucleotid sequences into its kmer representation
  :param Array file: file of sequences
  :param int k: the number of nucleotides involved into each kmer
  :return generator kmer: the integer representation of each of the kmers
  """
  for seq in file:
    kmer = 0
    kmer_rev_comp = 0
    mask = (1<<(2*k)) - 1
    for i in range(len(seq)):
      nuc = ((ord(seq[i]) >> 1) & 0b11)
      kmer <<= 2
      kmer = kmer + nuc
      if i >= (k - 1):
        # computing complementary nucleotid 
        nuc_comp = ((nuc + 0b10) & 0b11) << ((k - 1)*2)
        kmer_rev_comp += nuc_comp
        # we return the minimum of reverse complement and original sequence to keep the smallest key
        yield min(kmer, kmer_rev_comp)
        # we delete the data
        kmer_rev_comp >>= 2
        kmer &= mask
      else:
        # computing complementary nucleotid 
        nuc_comp = ((nuc + 0b10) & 0b11) << (i*2)
        kmer_rev_comp += nuc_comp

def stream_kmers_xor(file, k):
  """ Transforms a file of nucleotid sequences into its shifted kmer representation
  :param Array file: file of sequences
  :param int k: the number of nucleotides involved into each kmer
  :return generator kmer: the integer representation of each of the kmers shifted through xorshift
  """
  for seq in file:
    kmer = 0
    kmer_rev_comp = 0
    mask = (1<<(2*k)) - 1
    for i in range(len(seq)):
      nuc = ((ord(seq[i]) >> 1) & 0b11)
      kmer <<= 2
      kmer = kmer + nuc
      if i >= (k - 1):
        # computing complementary nucleotid
        nuc_comp = ((nuc + 0b10) & 0b11) << ((k - 1)*2)
        kmer_rev_comp += nuc_comp
        # we return the minimum of reverse complement and original sequence to keep the smallest key
        yield xorshift(min(kmer, kmer_rev_comp))
        # we delete the data
        kmer_rev_comp >>= 2
        kmer &= mask
      else:
        # computing complementary nucleotid
        nuc_comp = ((nuc + 0b10) & 0b11) << (i*2)
        kmer_rev_comp += nuc_comp

def kmer2str(val, k):
  """ Transform a kmer integer into a its string representation
  :param int val: An integer representation of a kmer
  :param int k: The number of nucleotides involved into the kmer.
  :return str: The kmer string formatted
  """
  letters = ['A', 'C', 'T', 'G']
  str_val = []
  for i in range(k):
    str_val.append(letters[val & 0b11])
    val >>= 2

  str_val.reverse()
  return "".join(str_val)


# Tests: the input sequence, put through the two methods, must be found in output
seqs=['AGTCTGAGTGC']
k = len(seqs[0])
values = stream_kmers(seqs, k)
out_seq=''
for val in values:
  out_seq = kmer2str(val, k)
assert(seqs[0] == out_seq)

seqs=['AAAA']
k = len(seqs[0])
values = stream_kmers(seqs, k)
outseq=''
for val in values:
  out_seq = kmer2str(val, k)
assert(seqs[0] == out_seq)
