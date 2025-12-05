filename="input.txt"

def merge_range(a, b, ranges):
    ranges = ranges[:]

    if ranges == []:
        return [a,b]

    # dtermine where a stands 
    i=0
    while i < len(ranges):
        if a < ranges[i]:
            break 
        i+=1
    if i % 2 == 0:
        if i==len(ranges):
            # a > end of last range 
            return ranges + [a,b]
            
        # a < first of a range 
        if i-1>=0 and a==ranges[i-1]:
            # a == the end of the range right before ranges[i]
            if b < ranges[i]:
                ranges[i-1] = b 
            else:
                # b >= ranges[i]
                j=i
                while j < len(ranges):
                    if b < ranges[j]:
                        break 
                    j+=1
                if j % 2 == 0:
                    if j==len(ranges):
                        # j > end of last range
                        ranges = ranges[:i-1] + [b] 
                    else:
                        # b < first of a range 
                        ranges = ranges[:i-1] + [b] + ranges[j:]
                else:
                    # b < end of a range 
                    ranges = ranges[:i-1] + ranges[j:]
        else:
            # end of a range < a < first of a range
            # OR a < start of the first range
            if b < ranges[i]:
                ranges = ranges[:i] + [a,b] + ranges[i:]
            else:
                # b >= ranges[i]
                j=i
                while j < len(ranges):
                    if b < ranges[j]:
                        break 
                    j+=1
                if j % 2 == 0:
                    # b < first of a range 
                    if b==ranges[j-1]:
                        # b == end of the range right before ranges[j]
                        ranges = ranges[:i] + [a,b] + ranges[j:]
                    else:
                        # end of a range < b < first of a range
                        ranges = ranges[:i] + [a,b] + ranges[j:]
                else:
                    # b < end of a range 
                    ranges = ranges[:i] + [a] + ranges[j:]
    else:
        # a < end of a range 
        
        if b < ranges[i]:
            # change nothing
            return ranges
        else:
            # b >= ranges[i]
            j=i
            while j < len(ranges):
                if b < ranges[j]:
                    break 
                j+=1
            if j % 2 == 0:
                # b < first of a range 
                ranges = ranges[:i] + [b] + ranges[j:]
            else:
                # b < end of a range 
                ranges = ranges[:i] + ranges[j:]

    return ranges
            
            

def calc_fresh_ingredients_from_unique_ranges(unique_ranges):
    i=0
    fresh_ingreds=0
    while i<len(unique_ranges):
        fresh_ingreds += unique_ranges[i+1] - unique_ranges[i] + 1
        i+=2
    return fresh_ingreds

def main():
    with open(filename, 'r') as f:
        ranges_uniq = []
        for line in f:
            line = line.strip()
            if line=='':
                break
            dash_i = line.find('-')
            a = int(line[:dash_i])
            b = int(line[dash_i+1 :])
            before = ranges_uniq[:]
            ranges_uniq = merge_range(a, b, ranges_uniq)
            after = ranges_uniq[:]
            print(before==after)
            print()
    print(ranges_uniq)

    print(calc_fresh_ingredients_from_unique_ranges(ranges_uniq))

def test():
    ranges = [3,5, 6,10, 12,15, 18,20]
    ranges_to_add = [(1,3),(1,4),(1,5),(20,23),(19,23),(16,23)]
    for i in range(len(ranges_to_add)):
        x,y = ranges_to_add[i]
        print(ranges)
        print(x,y)
        print(merge_range(x,y, ranges))
        print()

if __name__=="__main__":
    main() 
