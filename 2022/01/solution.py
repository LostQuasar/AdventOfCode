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
  try: 
    assert calories[0] == 24000
    assert sum(calories[:3]) == 45000
  except AssertionError:
    print("Answer 1 should be", 24000, "is", calories[0])
    print("Answer 2 should be", 45000, "is", sum(calories[:3]))
    
with open("input.txt","r") as file:
  calories = findCalories(file)
  print("Part 1 Answer:", calories[0])  
  print("Part 2 Answer:", sum(calories[:3]))
