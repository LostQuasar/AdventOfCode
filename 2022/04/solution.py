import re

def part1(lines):
  i = 0
  for line in lines:
    l, m, n, o = [int(x) for x in re.split("-|,",line)]
    if (l <= n and m >= o) or (l >= n and m <= o):
      i+=1
  return i

def part2(lines):
  i = 0
  for line in lines:
    l, m, n, o = [int(x) for x in re.split("-|,",line)]
    range1 = list(range(l, m+1))
    range2 = list(range(n, o+1))
    for num in range1:
      if num in range2:
        i+=1
        break
  return i

with open("test.txt", "r") as file:
  lines = [x.strip("\n") for x in file.readlines()]
  part1Sol = (part1(lines), 2)
  part2Sol = (part2(lines), 4)
  if part1Sol[0] != part1Sol[1]:
    print("Part 1 answer should be", part1Sol[1], "is", part1Sol[0])
  if part2Sol[0] != part2Sol[1]:
    print("Part 2 answer should be", part2Sol[1], "is", part2Sol[0])

with open("input.txt", "r") as file:
  lines = [x.strip("\n") for x in file.readlines()]
  print("Part 1 answer:", part1(lines))
  print("Part 2 answer:", part2(lines))
