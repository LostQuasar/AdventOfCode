from stopwatch import Stopwatch
s = Stopwatch(1)
s.start()

elfList = []
with open("input.txt","r") as file:
  elf = []
  for line in file:
    if line != '\n':
      elf.append(int(line))
    else: 
      elfList.append(elf)
      elf = []

calories = []
for elf in elfList:
  calories.append(sum(elf))
calories.sort(reverse=True)

print("First Answer:", calories[0])  
print("Second Answer:", sum(calories[:3]))

s.stop()
print("Time taken:", s)