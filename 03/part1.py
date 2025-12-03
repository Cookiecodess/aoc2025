filename = "input.txt"

def get_joltage(bank: str) -> int:
  largest_first = largest(0, len(bank)-1, bank)
  print("largest_first:",largest_first)
  largest_second = largest(largest_first+1, len(bank), bank)
  print("largest_second:",largest_second)
  return int(bank[largest_first] + bank[largest_second])
    
def largest(start, end, string):
  largest = start
  for i in range(start, end):
    if int(string[i]) > int(string[largest]):
      largest = i
  return largest

def main():
  sum = 0
  with open(filename, "r") as f:
    for bank in f:
      sum += get_joltage(bank.strip())
  print(sum)

if __name__ == "__main__":
  main()

