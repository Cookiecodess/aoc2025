filename = "input.txt"

def get_joltage(bank: str) -> int:
  num_batteries = 12
  digits = ""
  last_largest_i = -1
  for n in range(num_batteries-1, -1, -1):
    last_largest_i = largest(last_largest_i+1, len(bank)-n, bank)
    digit = bank[last_largest_i]
    print(last_largest_i, digit)
    digits += digit
  print(digits)
  return int(digits)

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

