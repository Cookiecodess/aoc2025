filename="input.txt"

def get_problems():
    problems=[]
    with open(filename, "r") as f:
        for line in f:
            if line.strip() == "":
                continue
            problems.append([x.strip() for x in line.split(" ") if x.strip() != ""])
            
    return problems
       
def sum(start, end, probs, col):
    total=0
    for i in range(start, end):
        total+= int(probs[i][col])
    return total
    
def mult(start, end, probs, col):
    total=1
    for i in range(start, end):
        total *= int(probs[i][col])
    return total
    
def solve_problems(problems):
    finalresult=0
    for col in range(len(problems[0])):
        if problems[-1][col] == "+":
            op = sum
        else:
            op = mult
        finalresult += op(0, len(problems)-1, problems, col)
        
    return finalresult
       
                
def main():
    probs = get_problems()
    print(probs)
    print(solve_problems(probs))
    
if __name__=="__main__":
    main()
    
main()