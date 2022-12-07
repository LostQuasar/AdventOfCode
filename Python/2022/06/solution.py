def find_marker(lines, length):
  i = length
  stack = list(lines[:length])
  for char in lines[length:]:
    j = 0
    for letter in stack:
      if stack.count(letter) == 1:
        j+=1
    if j == length:
      return i
    del stack[0]
    stack.insert(length, char)
    i+=1

with open("test.txt", 'r') as file:
  lines = file.read()
  part1Sol = [find_marker(lines, 4), 5]
  part2Sol = [find_marker(lines, 14), 23]
  if part1Sol[0] != part1Sol[1]:
    print("Part 1 test should be", part1Sol[1], "is", part1Sol[0])
  if part2Sol[0] != part2Sol[1]:
    print("Part 2 test should be", part2Sol[1], "is", part2Sol[0])

with open("input.txt", 'r') as file:
  lines = file.read()
  print("Part 1 answer:", find_marker(lines, 4))
  print("Part 2 answer:", find_marker(lines, 14))
