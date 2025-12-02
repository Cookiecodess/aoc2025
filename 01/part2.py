zeroes = 0
curr_pos = 50
filename = "input.txt"

def parse_instr(instr):
  dir = instr[0]
  clicks = int(instr[1:])
  return (dir, clicks)

def right_turn(curr_pos, clicks):
  normal_result = curr_pos + clicks
  new_dial_pos = normal_result % 100
  distance_to_first_zero = 100 - curr_pos
  zeroes = (clicks - distance_to_first_zero) // 100 + 1
  return (new_dial_pos, zeroes)

def left_turn(curr_pos, clicks):
  normal_result = curr_pos - clicks
  new_dial_pos = normal_result % 100
  distance_to_first_zero = curr_pos if curr_pos > 0 else 100
  zeroes = (clicks - distance_to_first_zero) // 100 + 1
  return (new_dial_pos, zeroes)

with open(filename, 'r') as f:
  # print("curr_pos, curr_zeroes")
  for instruction in f:
    curr_dir, curr_clicks = parse_instr(instruction)    
    turn_func = right_turn if curr_dir == 'R' else left_turn
    curr_pos, curr_zeroes  = turn_func(curr_pos, curr_clicks)
    #  print(curr_pos, curr_zeroes)
    zeroes+=curr_zeroes
    
print(zeroes)
