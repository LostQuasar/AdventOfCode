priority = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def part1(lines):
  sumVal = 0
  for line in lines:
    line = line.replace("\n", "")
    half = len(line)//2
    for item in line[:half]:
      if item in line[half:]:
        sumVal += priority.index(item)
        break
  return sumVal

def part2(lines):
  sumVal = 0
  i = 0
  group = []
  for line in lines:
    group.append(line)
    i += 1
    if i == 3:
      for item in group[0]:
        if item in group[1] and item in group[2]:
          sumVal += priority.index(item)
          break
      group = []
      i = 0
  return sumVal

with open("test.txt", "r") as file:
  lines = [x.replace("\n","") for x in file.readlines()]
  try: 
    assert part1(lines) == 157
    assert part2(lines) == 70
  except AssertionError:
    print("Answer 1 should be", 157, "is", part1(lines))
    print("Answer 2 should be", 70, "is", part2(lines))

with open("input.txt", "r") as file:
  lines = [x.replace("\n","") for x in file.readlines()]
  print("Part 1 Answer:", part1(lines))
  print("Part 2 Answer:", part2(lines))
