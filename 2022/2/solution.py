from stopwatch import Stopwatch
watch = Stopwatch(1)
watch.start()
firstSum = secondSum = 0
choiceValueP1 = {"X": 1, "Y": 2, "Z": 3}
outcomeValueP1 = {
  "A X": 3, "B X": 0, "C X": 6,
  "A Y": 6, "B Y": 3, "C Y": 0,
  "A Z": 0, "B Z": 6, "C Z": 3
  }
choiceValueP2 = {
  "A X": 3, "B X": 1, "C X": 2,
  "A Y": 1, "B Y": 2, "C Y": 3,
  "A Z": 2, "B Z": 3, "C Z": 1
  }
outcomeValueP2 = {"X": 0, "Y":3, "Z": 6}
with open("input.txt", "r") as file:
  for line in file:
    firstSum += choiceValueP1[line[2]] + outcomeValueP1[line[:3]]
    secondSum += outcomeValueP2[line[2]] + choiceValueP2[line[:3]]
watch.stop()
print("First Answer:", firstSum)
print("Second Answer:", secondSum)
print("Time taken:", watch)
