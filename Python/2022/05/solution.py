def get_values(lines):
  crates, moves = lines.split('\n\n')
  crates = crates.split('\n')
  moves = moves.split('\n')[:-1]
  stacks_amnt = int(crates[-1].replace(' ','')[-1])
  stacks = []
  for _ in range(stacks_amnt):
    stacks.append([])
  for row in crates[:-1]:
    for index in range(stacks_amnt):
      value = row[1 + index * 4]
      if value != ' ':
        stacks[index].append(value)
  top = ''
  return moves, stacks_amnt, stacks, top

def part1(lines):
  moves, stacks_amnt, stacks, top = get_values(lines)
  for move in moves:
    move = move.split(' ')
    l, m, n = int(move[1]), int(move[3]) - 1, int(move[5]) - 1
    pickup = stacks[m][:l]
    del stacks[m][:l]
    for crate in pickup:
      stacks[n].insert(0, crate)
  for num in range(stacks_amnt):
    top += stacks[num][0] 
  return top

def part2(lines):
  moves, stacks_amnt, stacks, top = get_values(lines)
  for move in moves:
    move = move.split(' ')
    l, m, n = int(move[1]), int(move[3]) - 1, int(move[5]) - 1
    pickup = stacks[m][:l]
    del stacks[m][:l]
    pickup.reverse()
    for crate in pickup:
      stacks[n].insert(0, crate)
  for num in range(stacks_amnt):
    top += stacks[num][0]
  return top

with open("test.txt", 'r') as file:
  lines = file.read()
  part1Sol = [part1(lines), "CMZ"]
  part2Sol = [part2(lines), "MCD"]
  if part1Sol[0] != part1Sol[1]:
    print("Part 1 test should be", part1Sol[1], "is", part1Sol[0])
  if part2Sol[0] != part2Sol[1]:
    print("Part 2 test should be", part2Sol[1], "is", part2Sol[0])

with open("input.txt", 'r') as file:
  lines = file.read()
  print("Part 1 answer:", part1(lines))
  print("Part 2 answer:", part2(lines))
