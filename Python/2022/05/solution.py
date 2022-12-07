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
    amount, from_stack, to_stack = int(move[1]), int(move[3]) - 1, int(move[5]) - 1
    pickup = stacks[from_stack][:amount]
    del stacks[from_stack][:amount]
    for crate in pickup:
      stacks[to_stack].insert(0, crate)
  for index in range(stacks_amnt):
    top += stacks[index][0]


def part2(lines):
  moves, stacks_amnt, stacks, top = get_values(lines)
  for move in moves:
    move = move.split(' ')
    amount, from_stack, to_stack = int(move[1]), int(move[3]) - 1, int(move[5]) - 1
    pickup = stacks[from_stack][:amount]
    del stacks[from_stack][:amount]
    pickup.reverse()
    for crate in pickup:
      stacks[to_stack].insert(0, crate)
  for index in range(stacks_amnt):
    top += stacks[index][0]
  return top

with open("test.txt", 'r') as file:
  lines = file.read()
  part1Test = [part1(lines), "CMZ"]
  part2Test = [part2(lines), "MCD"]
  if part1Test[0] != part1Test[1]:
    print("Part 1 test should be", part1Test[1], "is", part1Test[0])
  if part2Test[0] != part2Test[1]:
    print("Part 2 test should be", part2Test[1], "is", part2Test[0])

with open("input.txt", 'r') as file:
  lines = file.read()
  print("Part 1 answer:", part1(lines))
  print("Part 2 answer:", part2(lines))
