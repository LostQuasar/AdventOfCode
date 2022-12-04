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
  part1Sol = (part1(values), 514579)
  part2Sol = (part2(values), 241861950)
  if part1Sol[0] != part1Sol[1]:
    print("Part 1 should be", part1Sol[1], "is", part1Sol[0])
  if part2Sol[0] != part2Sol[1]:
    print("Part 2 should be", part2Sol[1], "is", part2Sol[0])

with open("input.txt","r") as file:
  values = [int(x) for x in file.readlines()]
  print("Part 1 Answer:", part1(values))  
  print("Part 2 Answer:", part2(values))
