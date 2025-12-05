filename="test.txt"

def merge_range(a, b, ranges):
  if ranges == []:
    ranges += [a, b]
    return
  
  i=0
  while a>=ranges[i]:
      i+=1
  #print(i)
  
  if i % 2 == 0:
      # a < start of a range
      j = i
      while b>=ranges[j]:
          j+=1
      if j % 2 == 0:
          # b < start of a range
          ranges = ranges[:i] + [a,b] + ranges[j:]
      else:
          # b < end of a range
          ranges = ranges[:i] + [a] + ranges[j:]
  else:
      # a < end of a range
      j = i
      while b>=ranges[j]:
          j+=1
      if j % 2 == 0:
          # b < start of a range
          ranges = ranges[:i] + [b] + ranges[j:]
      else:
          # b < end of a range
          ranges = ranges[:i] + ranges[j:]
  return ranges

def main():
  with open(filename, 'r') as f:
    ranges_uniq = []
    for line in f:
      line = line.strip()
      dash_i = line.find('-')
      a = line[:dash_i] 
      b = line[dash_i+1 :]
      ranges_uniq = merge_range(a, b, ranges_uniq)
  print(ranges_uniq)
  
if __name__=="__main__":
  main() 
