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

firstSum = secondSum = 0
with open("test.txt", "r") as file:
  for line in file:
    firstSum += choiceValueP1[line[2]] + outcomeValueP1[line[:3]]
    secondSum += outcomeValueP2[line[2]] + choiceValueP2[line[:3]]
  try:
    assert firstSum == 15
    assert secondSum == 12
  except AssertionError:
    print("Answer 1 should be", 15, "is", firstSum)
    print("Answer 2 should be", 12, "is", secondSum)


firstSum = secondSum = 0
with open("input.txt", "r") as file:
  for line in file:
    firstSum += choiceValueP1[line[2]] + outcomeValueP1[line[:3]]
    secondSum += outcomeValueP2[line[2]] + choiceValueP2[line[:3]]
  print("Part 1 Answer:", firstSum)
  print("Part 2 Answer:", secondSum)
