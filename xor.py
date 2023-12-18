# functions of reverse from https://gist.github.com/PhoeniXkrypT/22b978dee79f3092d63f:
###
def reverse_right_shift(value, shift, mult=0xffffffff):
    output, i = 0, 0
    while i * shift < 32:
        compartment = int(bin(0xffffffff << (32 - shift))[-32:], 2) >> (shift * i)
        part_output = value & compartment
        value ^= part_output >> shift & mult
        output |= part_output
        i += 1
    return output

def reverse_left_shift(value, shift, mult=0xffffffff):
    output, i = 0, 0
    while i * shift < 32:
        compartment = int(bin((0xffffffff >> (32- shift)) << (shift * i))[-32:], 2)
        part_output = value & compartment
        value ^= part_output << shift & mult
        output |= part_output
        i += 1
    return output
###

def xorshift(x):
  """Applies xorshift to x
  :param int x: the number to shift
  :return int x: the shifted value of x
  """
  x ^= x << 3
  x ^= x >> 7
  x ^= x << 5
  return x

def reversed_xorshift(x):
  """Reverses xorshift from x
  :param int x: the number to unshift
  :return int x: the original value of x
  """
  x = reverse_left_shift(x, 5)
  x = reverse_right_shift(x, 7)
  x = reverse_left_shift(x, 3)
  return x