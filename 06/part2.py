filename="input.txt"

def get_problems():
   
    problems=[]
    with open(filename, "r") as f:
        for line in f:
            if line.strip() == "":
                continue
            problems.append(line)
            
    return problems
       
def get_separating_cols(operator_line):
    cols=[]
    for i in range(len(operator_line)):
        ch = operator_line[i]
        if ch=="+" or ch=="*":
            cols.append(i)
    return cols
    
def add(a,b):
    return a+b
    
def mult(a,b):
    return a*b

def solve_problems(probs, cols):
    finalresult=0
    for i in range(len(cols)):
        curr_col = cols[i]
        if i < len(cols)-1:
            next_col = cols[i+1]
        else:
            next_col = len(probs[0]) + 10 # an arbitrary number thats larger than the length of first row
            
        print("curr_col:",curr_col,"next_col:",next_col)
        
        if probs[-1][curr_col] == "+":
            op = add
            result = 0
        else:
            op = mult
            result = 1
            
        for col in range(curr_col, next_col-1):
            print("col:",col)
            num=""
            col_exists = False
            for row in range(len(probs)-1):
                if col >= len(probs[row]) or probs[row][col]=="\n":
                    continue
                col_exists = True
                print(probs[row][col])
                num+=probs[row][col]
                
            if not col_exists:
                # we've reached the end of the problem sheet
                break

            num=int(num)
            result = op(result, num)
            print("result:",result)
            
        finalresult+=result
        print("finalresult:",finalresult)
      
    return finalresult
       
                
def main():
    probs = get_problems()
    cols = get_separating_cols(probs[-1])
    print("separating cols:",cols)
    print(solve_problems(probs, cols))
    
if __name__=="__main__":
    main()
    