from stopwatch import Stopwatch
watch = Stopwatch(1)
watch.start()
firstSum = 0
secondSum = 0
i = 0
priority = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
group = []
with open("input.txt", "r") as file:
  for line in file:
    line = line.replace("\n", "")
    half = len(line)//2
    for item in line[:half]:
      if item in line[half:]:
        firstSum += priority.index(item)
        break

    group.append(line)
    i += 1
    if i == 3:
      for item in group[0]:
        if item in group[1] and item in group[2]:
          secondSum += priority.index(item)
          break
      group = []
      i = 0

watch.stop()
print("First Answer:", firstSum)
print("Second Answer:", secondSum)
print("Time taken:", watch)
