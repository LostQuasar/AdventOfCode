def part1(lines):
  count = 0
  for line in lines:
    rules, passwd = line.split(': ')
    rules = rules.split(' ')
    char_min, char_max = [int(x) for x in rules[0].split('-')]
    if char_min <= passwd.count(rules[1]) <= char_max:
      count+=1
  return count

def part2(lines):
  count = 0
  for line in lines:
    rules, passwd = line.split(': ')
    rules = rules.split(' ')
    char_min, char_max = [int(x) - 1 for x in rules[0].split('-')]
    char = rules[1]
    if (passwd[char_min] == char) ^ (passwd[char_max] == char):
      count+=1
  return count

with open("test.txt", 'r') as file:
  lines = [x.strip('\n') for x in file.readlines()]
  part1Sol = [part1(lines), 2]
  part2Sol = [part2(lines), 1]
  if part1Sol[0] != part1Sol[1]:
    print("Part 1 test should be", part1Sol[1], "is", part1Sol[0])
  if part2Sol[0] != part2Sol[1]:
    print("Part 2 test should be", part2Sol[1], "is", part2Sol[0])

with open("input.txt", 'r') as file:
  lines = [x.strip('\n') for x in file.readlines()]
  print("Part 1 answer:", part1(lines))
  print("Part 2 answer:", part2(lines))
