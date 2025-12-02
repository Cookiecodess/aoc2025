import math

filename = "input.txt"
checked_invals = set()

with open(filename, "r") as f:
  validstr = f.readline().strip()

validranges = [[int(range[0:range.find("-")]), int(range[range.find("-")+1:])] for range in validstr.split(",")]
print(validranges)

def calc_digits(num):
    return math.ceil(math.log10(num))
    
def sum_inval_in_range(r):
    first = r[0]
    last = r[1]
    print(first, last)
    dig_f = calc_digits(first)
    dig_l = calc_digits(last)
    if dig_f%2==1 and dig_l%2==1:
        return 0
    if dig_f%2==1:
        first = 10**(dig_l-1)
        dig_f += 1
    elif dig_l%2==1:
        last = int("9"*dig_f)
        dig_l -= 1
        
    half_digits = dig_f // 2
    sum = 0
    
    a = first // (10 ** half_digits)
    b = last // (10 ** half_digits)
    for n in range(a, b+1):
        n_twiced = int(str(n)*2)
        if (n_twiced>=first and n_twiced<=last) and n_twiced not in checked_invals: 
          checked_invals.add(n_twiced)         
          sum += n_twiced
          print(n_twiced, sum)
    return sum

def is_invalid(id):
  digit_count = math.ceil(math.log10(id))
  if digit_count % 2 == 1:
    return False

  second_half_index = digit_count // 2
  id = str(id)
  return id[:second_half_index] == id[second_half_index:]   

sum_of_invalids = 0

for r in validranges:
  sum_of_invalids += sum_inval_in_range(r)
  #print(sum_of_invalids)

print(sum_of_invalids )
