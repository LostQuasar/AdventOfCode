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
  part1Sol = [firstSum, 15]
  part2Sol = [secondSum, 12]
  if part1Sol[0] != part1Sol[1]:
    print("Part 1 test should be", part1Sol[1], "is", part1Sol[0])
  if part2Sol[0] != part2Sol[1]:
    print("Part 2 test should be", part2Sol[1], "is", part2Sol[0])



firstSum = secondSum = 0
with open("input.txt", "r") as file:
  for line in file:
    firstSum += choiceValueP1[line[2]] + outcomeValueP1[line[:3]]
    secondSum += outcomeValueP2[line[2]] + choiceValueP2[line[:3]]
  print("Part 1 Answer:", firstSum)
  print("Part 2 Answer:", secondSum)
