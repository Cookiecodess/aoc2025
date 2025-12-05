filename='input.txt'
opt=0 # 0: dumber, 1: smarter
ERR_INVALID_OPT = 'invalid value for "opt" variable (used to set algorithm smartness)'

def get_freshranges_and_ids():
    ranges=[]
    ids=[]
    with open(filename, 'r') as f:
        scanning_id=False
        for line in f:
            line = line.strip()
            if line == "":
                scanning_id=True 
                continue
            if scanning_id:
                ids.append(int(line)) 
            else:
                # scanning ranges
                if opt==0:
                    dash_i = line.find('-')
                    ranges.append((int(line[:dash_i]), int(line[dash_i+1 :])))
                elif opt==1:
                    pass 
                else:
                    raise ValueError(ERR_INVALID_OPT)
    return (ranges, ids)

def is_fresh_ingredient(ingred_id: int, fresh_ranges) -> bool:
    if opt==0:
        for first, last in fresh_ranges:
            if ingred_id>=first and ingred_id<=last:
                return True 
        return False
    
    if opt==1:
        pass 
        return False

    raise ValueError(ERR_INVALID_OPT)
            
def calc_fresh_ingredients(fresh_ranges, ids):
    fresh_ingreds=0
    for id in ids:
        if is_fresh_ingredient(id, fresh_ranges):
            fresh_ingreds+=1
    return fresh_ingreds

def main():
    fresh_ranges, ids = get_freshranges_and_ids()
    fresh_ingredients = calc_fresh_ingredients(fresh_ranges, ids)
    print(fresh_ingredients)

if __name__=='__main__':
    main()
