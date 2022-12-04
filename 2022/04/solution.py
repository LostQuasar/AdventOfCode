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
  try: 
    assert part1(lines) == 2
    assert part2(lines) == 4
  except AssertionError:
    print("Answer 1 should be", 2, "is", part1(lines))
    print("Answer 2 should be", 4, "is", part2(lines))

with open("input.txt", "r") as file:
  lines = [x.strip("\n") for x in file.readlines()]
  print("Part 1 Answer:", part1(lines))
  print("Part 2 Answer:", part2(lines))
