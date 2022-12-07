def find_marker(lines, length):
  index = length
  stack = list(lines[:length])
  for char in lines[length:]:
    unique = 0
    for letter in stack:
      if stack.count(letter) == 1:
        unique +=1
    if unique == length:
      return index
    del stack[0]
    stack.insert(length, char)
    index +=1

with open("test.txt", 'r') as file:
  lines = file.read()
  part1Test = [find_marker(lines, 4), 5]
  part2Test = [find_marker(lines, 14), 23]
  if part1Test[0] != part1Test[1]:
    print("Part 1 test should be", part1Test[1], "is", part1Test[0])
  if part2Test[0] != part2Test[1]:
    print("Part 2 test should be", part2Test[1], "is", part2Test[0])

with open("input.txt", 'r') as file:
  lines = file.read()
  print("Part 1 answer:", find_marker(lines, 4))
  print("Part 2 answer:", find_marker(lines, 14))
