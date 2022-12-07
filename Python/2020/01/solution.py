def part1(values):
  found = False
  output = 0
  for num1 in values:
    for num2 in values:
      if num1 == num2:
        break
      if num1 + num2 == 2020:
        output = num1 * num2
        found = True
    if found:
      break
  return output

def part2(values):
  found = False
  output = 0
  for num1 in values:
    for num2 in values:
      for num3 in values:
        if num1 == num2 or num2 == num3 or num1 == num3:
          break
        if num1 + num2 + num3 == 2020:
          output = num1 * num2 * num3
          found = True
    if found:
      break
  return output

with open("test.txt", "r") as file:
  values = [int(x) for x in file.readlines()]
  part1Test = [part1(values), 514579]
  part2Test = [part2(values), 241861950]
  if part1Test[0] != part1Test[1]:
    print("Part 1 test should be", part1Test[1], "is", part1Test[0])
  if part2Test[0] != part2Test[1]:
    print("Part 2 test should be", part2Test[1], "is", part2Test[0])

with open("input.txt","r") as file:
  values = [int(x) for x in file.readlines()]
  print("Part 1 Answer:", part1(values))  
  print("Part 2 Answer:", part2(values))
