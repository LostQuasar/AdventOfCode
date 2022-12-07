def findCalories(file):
  calories = []
  elf = []
  for line in file:
    if line != '\n':
      elf.append(int(line))
    else: 
      calories.append(sum(elf))
      elf = []
  calories.append(sum(elf))
  calories.sort(reverse=True)
  return calories

with open("test.txt","r") as file:
  calories = findCalories(file)
  part1Test = [calories[0], 24000]
  part2Test = [sum(calories[:3]), 45000]
  if part1Test[0] != part1Test[1]:
    print("Part test 1 should be", part1Test[1], "is", part1Test[0])
  if part2Test[0] != part2Test[1]:
    print("Part test 2 should be", part2Test[1], "is", part2Test[0])

with open("input.txt","r") as file:
  calories = findCalories(file)
  print("Part 1 Answer:", calories[0])  
  print("Part 2 Answer:", sum(calories[:3]))
