import math

filename = "input.txt"
checked_invals = set()


def calc_digits(num):
    return math.ceil(math.log10(num+1))    

def sum_inval_in_range(r):
    first, last = r
    print('first:',first, 'last:',last)
    digits = calc_digits(first)
        
    half_digits = digits // 2
    sum = 0

    print('digits:,',digits)
    print('half_digits:',half_digits)
    
    for i in range(1,half_digits+1):
        if (digits % i != 0):
            continue
        repeating_digits = i
        a = first // (10 ** (digits - repeating_digits))
        b = last // (10 ** (digits - repeating_digits))
        print('digits - repeating_digits:',digits- repeating_digits)
        print('a:',a,'b:',b)
        for n in range(a, b+1):
            n_full = int(str(n)*(digits // repeating_digits))
            print('n_full:',n_full)
            if (n_full>=first and n_full<=last) and n_full not in checked_invals: 
                checked_invals.add(n_full)         
                sum += n_full
                print(n_full,'is invalid,', 'sum:',sum)
    return sum


with open(filename, "r") as f:
    validstr = f.readline().strip()
    validranges_untidy = [(int(range[0:range.find("-")]), int(range[range.find("-")+1:])) for range in validstr.split(",")]
    validranges = []
    for first, last in validranges_untidy:
        dig_f = calc_digits(first)
        dig_l = calc_digits(last)
        if dig_f != dig_l:
            validranges.append((first, int("9"*dig_f)))
            validranges.append((10**(dig_l-1), last))
        else:
            validranges.append((first, last))

            
    print(validranges)

sum_of_invalids = 0

for r in validranges:
    sum_of_invalids += sum_inval_in_range(r)
    print()
    #print(sum_of_invalids)

print(sum_of_invalids )
