from builtins import all
import sys

def make_int(string):
    text, num = string.split("=")
    return int(num)

def cerror(string):
    CRED = '\033[91m'
    CEND = '\033[0m'
    print(CRED + string + CEND)

def parse_partition_sizes():
    fp = open("rust_out.txt", "r+")
    # Can assume first 5 are the 2 partition default
    l = fp.readlines()
    partition_lines = list(filter(lambda x: "size of" in x, l[4:]))
    partition_lines = [make_int(x) for x in partition_lines]
    print(f"Found {partition_lines} for a partition set.")
    fp.close()
    return partition_lines

def validate_elements_requirement_met(partitions, elements):
    sum_ = sum(partitions)
    if sum_ == int(elements):
        return ""
    return f"\nERROR! Expected sum of partition lens == num elements. Expected:{elements} got: {sum_}."

def validate_partition_lengths(partitions):
    num_sizes = len(set(partitions))
    if num_sizes in (1, 2):
        return ""
    return f"\nERROR! Expected only 1 or 2 partition sizes. Instead found this many sizes: {num_sizes}."

def validate_no_zeros(partitions):
   if all(partitions):
      return ""
   return f"\nERROR! Expected all partitions to have at least one element. Instead found these partition sizes: {partitions}."
 
def validate_correct(partitions, elements):
    # Checks that no partition is of size 0
    # and checks that there is a max of two partition sizes
    # where one size is only one larger than the other
    # and checks that the partition lengths will total
    # the num of elements
    msg = ""
    msg += validate_no_zeros(partitions)
    msg += validate_partition_lengths(partitions)
    msg += validate_elements_requirement_met(partitions, elements)
    return msg

num_elements = sys.argv[1]
partition_sizes = parse_partition_sizes()
msg = validate_correct(partition_sizes, num_elements)
if msg:    
    cerror(msg)
