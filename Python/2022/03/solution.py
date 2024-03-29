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
  part1Test = [part1(lines), 157]
  part2Test = [part2(lines), 70]
  if part1Test[0] != part1Test[1]:
    print("Part 1 test be", part1Test[1], "is", part1Test[0])
  if part2Test[0] != part2Test[1]:
    print("Part 2 test be", part2Test[1], "is", part2Test[0])

with open("input.txt", "r") as file:
  lines = [x.replace("\n","") for x in file.readlines()]
  print("Part 1 Answer:", part1(lines))
  print("Part 2 Answer:", part2(lines))
