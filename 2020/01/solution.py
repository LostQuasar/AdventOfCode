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
  assert part1(values) == 514579
  assert part2(values) == 241861950

with open("input.txt","r") as file:
  values = [int(x) for x in file.readlines()]
  print("Part 1 Answer:", part1(values))  
  print("Part 2 Answer:", part2(values))
