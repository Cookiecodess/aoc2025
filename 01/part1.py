zeroes = 0
curr_pos = 50

def parse_instr(instr):
  dir = instr[0]
  clicks = int(instr[1:])
  return (dir, clicks)

def right_turn(curr_pos, clicks):
  return (curr_pos + clicks) % 100

def left_turn(curr_pos, clicks):
  return (curr_pos - clicks) % 100

with open('input.txt', 'r') as f:
  for instruction in f:
    curr_dir, curr_clicks = parse_instr(instruction)    
    turn_func = right_turn if curr_dir == 'R' else left_turn
    curr_pos = turn_func(curr_pos, curr_clicks)
    if curr_pos == 0:
      zeroes+=1
    
print(zeroes)
